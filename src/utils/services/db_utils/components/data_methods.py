import os
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_not_empty,
    validate_type
)
from src.utils.services.db_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) + "\\"

class DataMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def insert_data_to_table(self, table_name, params, debug = 0):
        try:
            validate_not_none(table_name, "table_name")
            validate_not_empty(table_name, "table_name")
            validate_not_none(params, "params")
            
            self.prevent_config_env()
            logger.debug(f"Inserting data into table '{table_name}'")
            
            try:
                column_name = ""
                value = ""
                for val in params:
                    column_name += val+", "
                    if params[val] is None:
                        value += "null, "
                    elif str(params[val]).lower() == "null":
                        value += "null, "
                    elif "today" in str(params[val]).lower():
                        tempstr = str(params[val]).lower().replace('today', "GETDATE()")
                        value += tempstr+", "
                    elif "first_day_of_month" in str(params[val]).lower():
                        tempstr = str(params[val]).lower().replace('first_day_of_month', "DATEADD(MM,DATEDIFF(MM, 0, GETDATE()),0)")
                        value += tempstr+", "
                    elif "last_day_of_month" in str(params[val]).lower():
                        tempstr = str(params[val]).lower().replace('last_day_of_month', "DATEADD(MM,DATEDIFF(MM, -1, GETDATE()),-1)")
                        value += tempstr+", "
                    else:
                        value += "'"+str(params[val]) +"', "
                
                column_name = column_name[:-2]
                value = value[:-2]
                sql_query = 'insert into '+ table_name +'('+ column_name +') values ('+ value +')'
                
                if debug:
                    logger.debug(f"Generated SQL query: {sql_query}")
                
                self.query(sql_query)
            except Exception as e:
                logger.error(f"Error during insert operation: {str(e)}")
                self.dbconnect.rollback()
                logger.debug("Transaction rolled back")
                raise
            else:
                self.dbconnect.commit()
                logger.debug("Insert completed and committed")
        except Exception as e:
            logger.error(f"Failed to insert data into table '{table_name}': {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def insert_data_from_file(self, sql_file, number_of_times, list_of_data):
        try:
            validate_not_none(sql_file, "sql_file")
            validate_not_empty(sql_file, "sql_file")
            validate_not_none(number_of_times, "number_of_times")
            validate_type(number_of_times, int, "number_of_times")
            validate_not_none(list_of_data, "list_of_data")
            
            self.prevent_config_env()
            file_path = ROOT_DIR + sql_file
            logger.debug(f"Reading SQL from file: {file_path}")
            
            f = open(file_path, "r")
            query = f.read()
            f.close()
            
            result = []
            
            if number_of_times > 10:
                logger.warning(f"Number of times limited to 10 (was {number_of_times})")
                number_of_times = 10
                
            if len(list_of_data) > 0:
                logger.debug("Replacing parameters in SQL query")
                i = 1
                while i < len(list_of_data):
                    query = query.replace(list_of_data[i][0], list_of_data[i][1])
                    i += 1
                    
                logger.debug(f"Executing SQL query {number_of_times} times")
                j = 0
                while j < number_of_times:
                    try:
                        logger.debug(f"Execution {j+1}/{number_of_times}")
                        self.cursor.execute(query)
                        data = self.cursor.fetchall()
                    except Exception as e:
                        logger.error(f"Error during execution {j+1}: {str(e)}")
                        self.dbconnect.rollback()
                        logger.debug("Transaction rolled back")
                    else:
                        self.dbconnect.commit()
                        logger.debug("Execution completed and committed")
                        
                    for row in data:
                        result = [row[0], row[1]]
                        if row[0] > 0:
                            break
                    j += 1
                    
            logger.debug(f"Insert from file completed with result: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to insert data from file '{sql_file}': {str(e)}")
            self.extract_TestCaseFailed(e)
