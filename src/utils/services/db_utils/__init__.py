import pyodbc
from typing import Optional
from config.constants.settings import (
    ENVIRONMENT,
    DB_USERNAME,
    DB_PASSWORD
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    DatabaseException,
    ValidationException,
    validate_not_none,
    validate_type,
    validate_not_empty,
    ExtractTestCaseFailed,
    TC_NAME
)

from src.utils.services.db_utils.connection_methods import ConnectionMethods
from src.utils.services.db_utils.query_methods import QueryMethods
from src.utils.services.db_utils.data_methods import DataMethods

logger = get_logger(__name__)

class db(ConnectionMethods, QueryMethods, DataMethods):
    dbconnect: Optional[pyodbc.Connection] = None
    dbcursor: Optional[pyodbc.Cursor] = None
    TcName = TC_NAME
    
    @log_exceptions(log_level="ERROR")
    def __init__(self):
        try:
            # Initialize all parent classes
            ConnectionMethods.__init__(self)
            QueryMethods.__init__(self)
            DataMethods.__init__(self)
            
            # Ensure all classes share the same connection attributes
            # This is handled by the shared inheritance of the same attributes
            logger.debug("Database handler initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize database handler: {str(e)}")
            self.extract_TestCaseFailed(e)
