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
