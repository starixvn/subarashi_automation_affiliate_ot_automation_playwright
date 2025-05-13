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
    validate_not_empty
)

# Import các components
from src.utils.services.db_utils.components.connection_methods import ConnectionMethods
from src.utils.services.db_utils.components.query_methods import QueryMethods
from src.utils.services.db_utils.components.data_methods import DataMethods
from src.utils.services.db_utils.components.extract_testcase_failed import TC_NAME,ExtractTestCaseFailed

logger = get_logger(__name__)

class db(ConnectionMethods, QueryMethods, DataMethods):
    """
    Database client kế thừa từ tất cả các component.
    Giữ nguyên interface như file db_utils.py gốc.
    """
    dbconnect: Optional[pyodbc.Connection] = None
    dbcursor: Optional[pyodbc.Cursor] = None
    TcName = TC_NAME
