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

class QueryMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def query(self, query, querytype = 'select'):
        try:
            validate_not_none(query, "query")
            validate_not_empty(query, "query")
            validate_type(querytype, str, "querytype")
            
            self.prevent_config_env()
            logger.debug(f"Executing {querytype} query: {query}")
            self.cursor.execute(query)
            
            if querytype.lower() == 'select':
                data = self.cursor.fetchall()
                logger.debug(f"Query returned {len(data)} rows")
                return data
            else:
                self.dbconnect.commit()
                logger.debug("Query executed and changes committed")
        except Exception as e:
            logger.error(f"Query execution failed: {str(e)}")
            self.dbconnect.rollback()
            logger.debug("Transaction rolled back")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def query_and_get_all(self, query, debug = 0):
        try:
            validate_not_none(query, "query")
            validate_not_empty(query, "query")
            
            self.prevent_config_env()
            logger.debug(f"Executing query and getting all data: {query}")
            table = self.query(query)
            
            dictReturn = []
            columnNames = [column[0] for column in self.cursor.description]
            for row in table:
                tempstr = []
                for att in row:
                    tempstr.append(str(att))
                dictReturn.append(dict(zip(columnNames, tempstr)))
            
            if debug:
                logger.debug(f"Query result: {dictReturn}")
            
            return dictReturn
        except Exception as e:
            logger.error(f"Failed to execute query and get all data: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def get_value_in_column(self, query, columnname, debug = 0):
        try:
            validate_not_none(query, "query")
            validate_not_empty(query, "query")
            validate_not_none(columnname, "columnname")
            validate_not_empty(columnname, "columnname")
            
            self.prevent_config_env()
            logger.debug(f"Getting values for column '{columnname}' with query: {query}")
            table = self.query(query)
            
            vals = []
            for row in table:
                vals.append(str(row.__getattribute__(columnname)))
            
            if debug:
                logger.debug(f"Column values: {vals}")
            
            return vals
        except Exception as e:
            logger.error(f"Failed to get values for column '{columnname}': {str(e)}")
            self.extract_TestCaseFailed(e)
