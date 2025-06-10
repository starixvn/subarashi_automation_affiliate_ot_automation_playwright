from google.oauth2 import service_account
from googleapiclient import discovery
import os
from os.path import dirname as d
from os.path import abspath
from pathlib import Path
from config.constants.settings import ENVIRONMENT
environment = ENVIRONMENT

from src.utils.core.logging import get_logger
from src.utils.core.exceptions import FileException

from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_not_empty,
    FileException
)
from src.utils.services.utils.components.extract_testcase_failed import ExtractTestCaseFailed
from datetime import datetime
from src.utils.core.decorators import track_last_checklist

logger = get_logger(__name__)
project_root = str(Path(__file__).resolve().parents[5])

class GoogleMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def prepare_google_api(self):
        try:
            logger.debug("Preparing Google Sheets API client")
            SERVICE_ACCOUNT_FILE_PATH = os.path.join(project_root, 'config', 'secrets', 'client_secret.json')
            
            if not os.path.exists(SERVICE_ACCOUNT_FILE_PATH):
                logger.error(f"Service account file not found: {SERVICE_ACCOUNT_FILE_PATH}")
                raise FileException(
                    message="Google API service account file not found",
                    file_path=SERVICE_ACCOUNT_FILE_PATH
                )
                
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            logger.debug(f"Loading credentials from: {SERVICE_ACCOUNT_FILE_PATH}")
            creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE_PATH, scopes=SCOPES)
            client = discovery.build('sheets', 'v4', credentials=creds)
            logger.debug("Google Sheets API client initialized successfully")
            return client
        except Exception as e:
            logger.error(f"Failed to prepare Google API client: {str(e)}")
            return None
            
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def google_sheet_get_value(self, spread_sheet_id, sheet_name):
        try:
            validate_not_none(spread_sheet_id, "spread_sheet_id")
            validate_not_empty(spread_sheet_id, "spread_sheet_id")
            validate_not_none(sheet_name, "sheet_name")
            validate_not_empty(sheet_name, "sheet_name")
            
            logger.debug(f"Getting values from Google Sheet: {spread_sheet_id}, sheet: {sheet_name}")
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return []
                
            request = service.spreadsheets().values().get(
                spreadsheetId=spread_sheet_id, 
                range=sheet_name, 
                valueRenderOption='UNFORMATTED_VALUE'
            )
            result = request.execute().get('values', [])
            logger.debug(f"Retrieved {len(result)} rows from Google Sheet")
            return result
        except Exception as e:
            logger.error(f"Failed to get Google Sheet values: {str(e)}")
            print(e)
            return []

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def google_sheet_get_all_information(self, spread_sheet_id, sheet_name):
        try:
            validate_not_none(spread_sheet_id, "spread_sheet_id")
            validate_not_empty(spread_sheet_id, "spread_sheet_id") 
            validate_not_none(sheet_name, "sheet_name")
            validate_not_empty(sheet_name, "sheet_name")
            
            logger.debug(f"Getting all information from Google Sheet: {spread_sheet_id}, sheet: {sheet_name}")
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return None
                
            request = service.spreadsheets().values().get(
                spreadsheetId=spread_sheet_id, 
                range=sheet_name, 
                valueRenderOption='UNFORMATTED_VALUE'
            )
            result = request.execute()
            logger.debug(f"Retrieved complete sheet information")
            return result
        except Exception as e:
            logger.error(f"Failed to get Google Sheet information: {str(e)}")
            return None

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def google_sheet_update_sheet(self, spread_sheet_id, sheet_name, DataList):
        try:
            validate_not_none(spread_sheet_id, "spread_sheet_id")
            validate_not_empty(spread_sheet_id, "spread_sheet_id")
            validate_not_none(sheet_name, "sheet_name") 
            validate_not_empty(sheet_name, "sheet_name")
            validate_not_none(DataList, "DataList")
            
            logger.debug(f"Updating Google Sheet: {spread_sheet_id}, sheet: {sheet_name}")
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return
                
            full_sheet = self.google_sheet_get_all_information(spread_sheet_id, sheet_name)
            if not full_sheet:
                logger.error("Failed to get sheet information for update")
                return
                
            full_sheet['values'] = DataList
            
            request = service.spreadsheets().values().update(
                spreadsheetId=spread_sheet_id, 
                range=full_sheet.get('range'), 
                valueInputOption='RAW', 
                body={"values": DataList}
            )
            response = request.execute()
            logger.info(f"Google Sheet updated successfully: {sheet_name}")
        except Exception as e:
            logger.error(f"Failed to update Google Sheet: {str(e)}")
            
    @log_exceptions(log_level="DEBUG")
    def google_sheet_get_column_index(self, sheet, column_name):
        try:
            validate_not_none(sheet, "sheet")
            validate_not_none(column_name, "column_name")
            
            logger.debug(f"Finding column index for column name: '{column_name}'")
            
            if not sheet or len(sheet) == 0 or len(sheet[0]) == 0:
                logger.warning("Sheet is empty or has no headers")
                return -1
                
            for i in range(0, len(sheet[0])):
                if sheet[0][i] == column_name:
                    logger.debug(f"Found column '{column_name}' at index {i}")
                    return i
                    
            logger.warning(f"Column '{column_name}' not found in sheet")
            return -1
        except Exception as e:
            logger.error(f"Error finding column index: {str(e)}")
            return -1
            
    @track_last_checklist
    @log_exceptions(log_level="INFO")
    @monitor_performance()
    def update_result_to_ggsheet(self, spread_sheet_id, checklist, auto_testcase, sub_auto_testcases, auto_status, sheet_name="Checklist", duration=None):
        try:
            validate_not_none(spread_sheet_id, "spread_sheet_id")
            validate_not_empty(spread_sheet_id, "spread_sheet_id")
            validate_not_none(checklist, "checklist")
            validate_not_none(auto_testcase, "auto_testcase")
            validate_not_none(sub_auto_testcases, "sub_auto_testcases")
            validate_not_none(auto_status, "auto_status")
            
            logger.info(f"Updating test result to Google Sheet: {spread_sheet_id}, sheet: {sheet_name}")
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return None
                
            request = service.spreadsheets().values().get(
                spreadsheetId=spread_sheet_id, 
                range=sheet_name, 
                valueRenderOption='UNFORMATTED_VALUE'
            )
            values = request.execute().get('values', [])

            today = datetime.now()
            toDate = datetime.strftime(today, "%m/%d/%Y %H:%M:%S")
            
            if not values:
                logger.warning('No data found in sheet.')
                return None
                
            logger.debug(f"Searching for matching checklist '{checklist}' and test case '{auto_testcase}'")
            match_found = False
            
            env_column_map = {
                "local": "G",
                "uat": "H",
                "prod": "I"
            }
            sub_testcase_column = "F"
            date_column = "J"
            latest_env_run_column = "K"
            
            for i in range(1, len(values)):
                if len(values[i]) >= 5: 
                    if values[i][2] == checklist and values[i][4] == auto_testcase:
                        match_found = True
                        
                        sub_testcase_range = f'{sheet_name}!{sub_testcase_column}{str(i+1)}'
                        sub_testcase_data = {
                            'values': [[sub_auto_testcases]]
                        }
                        
                        status_column = env_column_map[environment]
                        status_range = f'{sheet_name}!{status_column}{str(i+1)}'
                        status_data = {
                            'values': [[auto_status]]
                        }
                        
                        date_range = f'{sheet_name}!{date_column}{str(i+1)}'
                        date_data = {
                            'values': [[toDate]]
                        }
                        latest_env_run_range = f'{sheet_name}!{latest_env_run_column}{str(i+1)}'
                        latest_env_run_data = {
                            'values': [[environment.upper()]]
                        }
                        
                        service.spreadsheets().values().update(
                            spreadsheetId=spread_sheet_id, 
                            range=sub_testcase_range,
                            valueInputOption='USER_ENTERED', 
                            body=sub_testcase_data
                        ).execute()
                        
                        service.spreadsheets().values().update(
                            spreadsheetId=spread_sheet_id, 
                            range=status_range,
                            valueInputOption='USER_ENTERED', 
                            body=status_data
                        ).execute()
                        
                        service.spreadsheets().values().update(
                            spreadsheetId=spread_sheet_id, 
                            range=date_range,
                            valueInputOption='USER_ENTERED', 
                            body=date_data
                        ).execute()
                        
                        service.spreadsheets().values().update(
                            spreadsheetId=spread_sheet_id, 
                            range=latest_env_run_range,
                            valueInputOption='USER_ENTERED', 
                            body=latest_env_run_data
                        ).execute()
                        break
                        
            if not match_found:
                logger.warning(f"No matching checklist/test case found for '{checklist}' / '{auto_testcase}'")
                
            if duration is not None and match_found:
                duration_column = "L"
                duration_range = f'{sheet_name}!{duration_column}{str(i+1)}'
                duration_data = {
                    'values': [[duration]]
                }
                
                service.spreadsheets().values().update(
                    spreadsheetId=spread_sheet_id, 
                    range=duration_range,
                    valueInputOption='USER_ENTERED', 
                    body=duration_data
                ).execute()
            
            return values
        except Exception as e:
            logger.error(f"Failed to update test result to Google Sheet: {str(e)}")
            print(e)
            return None

    @log_exceptions(log_level="INFO")
    @monitor_performance()
    def update_duration_only(self, spread_sheet_id, auto_testcase, duration, sheet_name="Checklist"):
        try:
            validate_not_none(spread_sheet_id, "spread_sheet_id")
            validate_not_empty(spread_sheet_id, "spread_sheet_id")
            validate_not_none(auto_testcase, "auto_testcase")
            validate_not_none(duration, "duration")
            
            logger.info(f"Updating duration for test case '{auto_testcase}': {duration}")
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return
            
            request = service.spreadsheets().values().get(
                spreadsheetId=spread_sheet_id, 
                range=sheet_name, 
                valueRenderOption='UNFORMATTED_VALUE'
            )
            values = request.execute().get('values', [])
            
            if not values:
                logger.warning('No data found in sheet.')
                return
            
            duration_column = "L"
            auto_testcase_column_index = 4
            
            matching_rows = []
            for i in range(1, len(values)):
                if len(values[i]) > auto_testcase_column_index and values[i][auto_testcase_column_index] == auto_testcase:
                    matching_rows.append(i + 1)
            
            if not matching_rows:
                logger.warning(f"No rows found for test case '{auto_testcase}'")
                return
            
            if len(matching_rows) == 1:
                duration_range = f'{sheet_name}!{duration_column}{matching_rows[0]}'
                duration_data = {
                    'values': [[duration]]
                }
                service.spreadsheets().values().update(
                    spreadsheetId=spread_sheet_id, 
                    range=duration_range,
                    valueInputOption='USER_ENTERED', 
                    body=duration_data
                ).execute()
                logger.info(f"Updated duration for '{auto_testcase}' at row {matching_rows[0]}")
            else:
                first_row = min(matching_rows)
                last_row = max(matching_rows)
                
                sheet_id = self.get_sheet_id_by_name(spread_sheet_id, sheet_name)
                if sheet_id is None:
                    logger.error(f"Could not find sheet ID for sheet name: {sheet_name}")
                    return
                
                duration_range = f'{sheet_name}!{duration_column}{first_row}'
                duration_data = {
                    'values': [[duration]]
                }
                service.spreadsheets().values().update(
                    spreadsheetId=spread_sheet_id, 
                    range=duration_range,
                    valueInputOption='USER_ENTERED', 
                    body=duration_data
                ).execute()
                
                col_index = self.column_letter_to_index(duration_column)
                merge_request = {
                    "requests": [
                        {
                            "mergeCells": {
                                "range": {
                                    "sheetId": sheet_id,
                                    "startRowIndex": first_row - 1,
                                    "endRowIndex": last_row,
                                    "startColumnIndex": col_index,
                                    "endColumnIndex": col_index + 1
                                },
                                "mergeType": "MERGE_ALL"
                            }
                        }
                    ]
                }
                service.spreadsheets().batchUpdate(
                    spreadsheetId=spread_sheet_id,
                    body=merge_request
                ).execute()
                
                logger.info(f"Updated and merged duration for '{auto_testcase}' from row {first_row} to {last_row}")
            
        except Exception as e:
            logger.error(f"Failed to update duration to Google Sheet: {str(e)}")
            print(e)

    def get_sheet_id_by_name(self, spreadsheet_id, sheet_name):
        try:
            service = self.prepare_google_api()
            if not service:
                logger.error("Failed to initialize Google API service")
                return None
                
            spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
            
            for sheet in spreadsheet.get('sheets', []):
                if sheet.get('properties', {}).get('title') == sheet_name:
                    return sheet.get('properties', {}).get('sheetId')
                    
            logger.warning(f"Sheet '{sheet_name}' not found in spreadsheet")
            return None
            
        except Exception as e:
            logger.error(f"Error getting sheet ID: {str(e)}")
            return None

    def column_letter_to_index(self, column_letter):
        
        result = 0
        for char in column_letter:
            result = result * 26 + (ord(char.upper()) - ord('A') + 1)
        return result - 1
