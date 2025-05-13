from google.oauth2 import service_account
from googleapiclient import discovery
import os
from os.path import dirname as d
from os.path import abspath

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

logger = get_logger(__name__)
root_dir = d(d(abspath(__file__)))

class GoogleMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def prepare_google_api(self):
        try:
            logger.debug("Preparing Google Sheets API client")
            SERVICE_ACCOUNT_FILE_PATH = root_dir + os.sep + 'config' + os.sep + 'client_secret.json'
            
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
            print(e)  # Keep existing print behavior for compatibility
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
            
    @log_exceptions(log_level="INFO")
    @monitor_performance()
    def update_result_to_ggsheet(self, spread_sheet_id, checklist, auto_testcase, sub_auto_testcases, auto_status, sheet_name="Checklist"):
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
            
            for i in range(2, len(values)):
                if len(values[i]) >= 11:
                    if values[i][2] == checklist and values[i][11] == auto_testcase: 
                        logger.debug(f"Match found at row {i+1}")
                        match_found = True
                        rangeUpdateResult = f'{sheet_name}!M{str(i+1)}:O{str(i+1)}'
                        dataUpdateResult = {
                            'values': [
                                        [sub_auto_testcases, auto_status, toDate]
                                    ]
                        }
                        update_response = service.spreadsheets().values().update(
                            spreadsheetId=spread_sheet_id, 
                            range=rangeUpdateResult,
                            valueInputOption='USER_ENTERED', 
                            body=dataUpdateResult
                        ).execute()
                        
                        logger.info(f"Updated test result in Google Sheet at range: {rangeUpdateResult}")
                        break
                        
            if not match_found:
                logger.warning(f"No matching checklist/test case found for '{checklist}' / '{auto_testcase}'")
                
            return values
        except Exception as e:
            logger.error(f"Failed to update test result to Google Sheet: {str(e)}")
            print(e)  # Keep existing print behavior for compatibility
            return None
