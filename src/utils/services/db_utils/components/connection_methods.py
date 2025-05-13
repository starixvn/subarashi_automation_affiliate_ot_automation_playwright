import pyodbc
from config.constants.settings import (
    ENVIRONMENT,
    DB_USERNAME,
    DB_PASSWORD
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_not_empty
)
from src.utils.services.db_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)

Database = {
    'Username': {'local': DB_USERNAME},
    'Password': {'local': DB_PASSWORD}
}
env = ENVIRONMENT
_env = 'local'

class ConnectionMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def connect(self, ServerName, DatabaseName):
        try:
            validate_not_none(ServerName, "ServerName")
            validate_not_empty(ServerName, "ServerName")
            validate_not_none(DatabaseName, "DatabaseName")
            validate_not_empty(DatabaseName, "DatabaseName")
            
            self.prevent_config_env()
            connectString = f"Driver={{SQL Server}};SERVER={ServerName};DATABASE={DatabaseName};UID={Database['Username'][_env]};PWD={Database['Password'][_env]}"
            logger.debug(f"Connecting to database: {ServerName}/{DatabaseName}")
            
            self.dbconnect = pyodbc.connect(connectString)
            self.dbconnect.setencoding('utf-8')
            self.cursor = self.dbconnect.cursor()
            logger.info(f"Connected to database: {ServerName}/{DatabaseName}")
        except Exception as e:
            logger.error(f"Failed to connect to database {ServerName}/{DatabaseName}: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    def close(self):
        try:
            if self.dbconnect is not None:
                logger.debug("Closing database connection")
                self.dbcursor.close()
                self.dbconnect.close()
                logger.debug("Database connection closed")
        except Exception as e:
            logger.error(f"Error closing database connection: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def prevent_config_env(self):
        try:
            if env != _env:
                logger.warning(f"Environment check: current env '{env}' is not equal to expected env '{_env}'")
                return 2
            logger.debug(f"Environment check passed: '{env}'")
        except Exception as e:
            logger.error(f"Environment check failed: {str(e)}")
            self.extract_TestCaseFailed(e)
