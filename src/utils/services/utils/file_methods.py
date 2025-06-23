import os
import pandas as pd
import json
from os.path import dirname as d
from os.path import abspath
import re

from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_not_empty,
    FileException,
    ensure_directory_exists,
    truncate_string,
    ExtractTestCaseFailed
)

logger = get_logger(__name__)
root_dir = d(d(abspath(__file__)))

class FileMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def extract_FunctionName(self, txt):
        try:
            validate_not_none(txt, "txt")
            validate_not_empty(txt, "txt")
            
            logger.debug(f"Extracting function name from text")
            regex = f"""filename.*Actions.*{self.site}_(.*).py"""
            match = re.search(regex, txt)
            if not match:
                logger.warning(f"Could not extract function name from text: {truncate_string(txt, 100)}")
                return None
                
            func_name = match.group(1)
            logger.debug(f"Extracted function name: {func_name}")
            return func_name
        except Exception as e:
            logger.error(f"Error extracting function name: {str(e)}")
            raise
            
    @log_exceptions(log_level="DEBUG")
    def remove_file(self, path):
        try:
            validate_not_none(path, "path")
            validate_not_empty(path, "path")
            
            file_path = root_dir + os.sep + 'Excel' + os.sep + path
            logger.debug(f"Attempting to remove file: {file_path}")
            
            if os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"File removed: {file_path}")
            else:
                logger.warning(f"File does not exist: {file_path}")
        except Exception as e:
            logger.error(f"Failed to remove file '{path}': {str(e)}")
            raise FileException(
                message=f"Failed to remove file",
                file_path=path,
                details=str(e),
                operation="remove_file"
            )

    @log_exceptions(log_level="DEBUG")
    def open_excel_file(self, path, sheet_name=0):
        try:
            validate_not_none(path, "path")
            validate_not_empty(path, "path")
            
            file_path = root_dir + os.sep + 'TestResult' + os.sep + 'export_excel' + os.sep + path
            logger.debug(f"Opening Excel file: {file_path}, sheet: {sheet_name}")
            
            if '.xlsx' in path:
                logger.debug("Processing as XLSX file with openpyxl engine")
                df = pd.read_excel(file_path, engine='openpyxl', sheet_name=sheet_name, header=None)
                df = df.dropna(axis=1, how='all')
                logger.debug(f"Successfully loaded Excel file with {len(df)} rows")
                return df
            elif '.xls' in path:
                logger.debug("Processing as XLS file")
                df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
                df = df.dropna(axis=1, how='all')
                logger.debug(f"Successfully loaded Excel file with {len(df)} rows")
                return df
            else:
                logger.warning(f"Unsupported file format for path: {path}")
                return None
        except Exception as e:
            logger.error(f"Failed to open Excel file '{path}': {str(e)}")
            return None

    @log_exceptions(log_level="DEBUG")
    def read_cell(self, sheet, row_index, column_index, startrow=2):
        try:
            validate_not_none(sheet, "sheet")
            logger.debug(f"Reading cell - row: {row_index}, column: {column_index}, startrow: {startrow}")
            
            if row_index == -1:
                logger.debug(f"Reading entire column {column_index} from row {startrow}")
                result = sheet.iloc[startrow:, column_index].tolist()
                logger.debug(f"Retrieved {len(result)} values from column")
                return result
            elif column_index == -1:
                logger.debug(f"Reading entire row {row_index}")
                result = sheet.iloc[row_index].tolist()
                logger.debug(f"Retrieved {len(result)} values from row")
                return result
            else:
                logger.debug(f"Reading single cell value")
                result = str(sheet.iloc[row_index, column_index])
                logger.debug(f"Cell value: {result}")
                return result
        except Exception as e:
            logger.error(f"Failed to read cell: {str(e)}")
            return None
        
    @log_exceptions(log_level="DEBUG")
    def get_row_index_by_column_value(self, df, col_index, value):
        try:
            validate_not_none(df, "df")
            validate_not_none(col_index, "col_index")
            validate_not_none(value, "value")
            
            logger.debug(f"Finding row with value '{value}' in column {col_index}")
            row_index = df[df[col_index] == value].index[0]
            logger.debug(f"Found value at row index: {row_index}")
            return row_index
        except IndexError:
            logger.warning(f"Value '{value}' not found in column {col_index}")
            return None
        except Exception as e:
            logger.error(f"Error searching for value in column: {str(e)}")
            return None

    @log_exceptions(log_level="DEBUG")
    def get_last_rows(self, sheet):
        try:
            validate_not_none(sheet, "sheet")
            
            logger.debug("Getting number of rows in sheet")
            row_count = len(sheet)
            logger.debug(f"Sheet has {row_count} rows")
            return row_count
        except Exception as e:
            logger.error(f"Failed to get row count: {str(e)}")
            return None

    @log_exceptions(log_level="DEBUG")
    def get_last_columns(self, sheet):
        try:
            validate_not_none(sheet, "sheet")
            
            logger.debug("Getting number of columns in the last row")
            col_count = len(sheet.iloc[-1])
            logger.debug(f"Last row has {col_count} columns")
            return col_count
        except Exception as e:
            logger.error(f"Failed to get column count: {str(e)}")
            return None
            
    @log_exceptions(log_level="DEBUG")
    def does_key_exist_in_json_file(self, pathJsonFile, strKey):
        try:
            validate_not_none(pathJsonFile, "pathJsonFile")
            validate_not_empty(pathJsonFile, "pathJsonFile")
            validate_not_none(strKey, "strKey")
            
            logger.debug(f"Checking if key '{strKey}' exists in JSON file: {pathJsonFile}")
            
            with open(pathJsonFile, 'r') as file:
                Data = json.load(file)
                file.close()

            exists = strKey in Data
            logger.debug(f"Key '{strKey}' {'exists' if exists else 'does not exist'} in file")
            return exists
        except FileNotFoundError:
            logger.error(f"JSON file not found: {pathJsonFile}")
            raise FileException(
                message="JSON file not found",
                file_path=pathJsonFile
            )
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {pathJsonFile}: {str(e)}")
            raise FileException(
                message=f"Invalid JSON in file",
                file_path=pathJsonFile,
                details=str(e)
            )
        except Exception as e:
            logger.error(f"Error checking key in JSON file: {str(e)}")
            raise
        
    @log_exceptions(log_level="DEBUG")
    def write_data_to_json_file(self, pathJsonFile, strData):
        try:
            validate_not_none(pathJsonFile, "pathJsonFile")
            validate_not_empty(pathJsonFile, "pathJsonFile")
            validate_not_none(strData, "strData")
            
            logger.debug(f"Writing data to JSON file: {pathJsonFile}")
            
            directory = os.path.dirname(pathJsonFile)
            if directory and not os.path.exists(directory):
                logger.debug(f"Creating directory: {directory}")
                ensure_directory_exists(directory)
                
            with open(pathJsonFile, 'w') as file:
                json.dump(strData, file, indent=4)
                file.close()
                
            logger.info(f"Data written to JSON file: {pathJsonFile}")
        except Exception as e:
            logger.error(f"Failed to write data to JSON file {pathJsonFile}: {str(e)}")
            raise FileException(
                message="Failed to write JSON file",
                file_path=pathJsonFile,
                details=str(e)
            )

    @log_exceptions(log_level="DEBUG")
    def read_data_from_json_file(self, pathJsonFile):
        try:
            validate_not_none(pathJsonFile, "pathJsonFile")
            validate_not_empty(pathJsonFile, "pathJsonFile")
            
            logger.debug(f"Reading data from JSON file: {pathJsonFile}")
            
            if not os.path.exists(pathJsonFile):
                logger.error(f"JSON file not found: {pathJsonFile}")
                raise FileException(
                    message="JSON file not found",
                    file_path=pathJsonFile
                )
                
            with open(pathJsonFile, 'r') as file:
                Data = json.load(file)
                file.close()
                
            logger.debug(f"Successfully read JSON data from file: {pathJsonFile}")
            return Data
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {pathJsonFile}: {str(e)}")
            raise FileException(
                message="Invalid JSON in file",
                file_path=pathJsonFile,
                details=str(e)
            )
        except Exception as e:
            logger.error(f"Error reading JSON file {pathJsonFile}: {str(e)}")
            raise
        
    @log_exceptions(log_level="DEBUG")
    def append_data_to_json_file(self, pathJsonFile, data):
        try:
            validate_not_none(pathJsonFile, "pathJsonFile")
            validate_not_empty(pathJsonFile, "pathJsonFile")
            validate_not_none(data, "data")
            
            logger.debug(f"Appending data to JSON file: {pathJsonFile}")
            
            if not os.path.exists(pathJsonFile):
                logger.error(f"JSON file not found: {pathJsonFile}")
                raise FileException(
                    message="JSON file not found",
                    file_path=pathJsonFile
                )
                
            with open(pathJsonFile, "r") as file:
                existing_data = json.load(file)
                file.close()
                
            existing_data.update(data)

            with open(pathJsonFile, 'w') as file:
                json.dump(existing_data, file, indent=4)    
                file.close()
                
            logger.info(f"Data appended to JSON file: {pathJsonFile}")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {pathJsonFile}: {str(e)}")
            raise FileException(
                message="Invalid JSON in file",
                file_path=pathJsonFile,
                details=str(e)
            )
        except Exception as e:
            logger.error(f"Error appending data to JSON file: {str(e)}")
            raise
