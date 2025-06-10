import sys
import os
from pathlib import Path

project_root = Path(__file__).parent.parent.parent.resolve()
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from src.utils.core import (
    AutomationException,
    ValidationException,
    ConfigException,
    TimeoutException,
    ElementNotFoundException,
    ElementStateException,
    NavigationException,
    APIException,
    FileException,
    BrowserException,
    DatabaseException,
    IoException,
    NotificationException,
    
    retry,
    log_exceptions,
    monitor_performance,
    convert_exceptions,
    
    get_logger,
    TRACE,
    VERBOSE,
    NOTICE,
    SUCCESS,
    
    validate_not_none,
    validate_type,
    validate_instance,
    validate_not_empty,
    validate_min_length,
    validate_max_length,
    validate_in_range,
    validate_in_options,
    validate_pattern,
    validate_email,
    validate_url,
    validate_file_exists,
    validate_directory_exists,
    
    ensure_directory_exists,
    load_json_file,
    save_json_file,
    truncate_string
)

from src.utils.services import api, db, ui, utilities

__all__ = [
    # Exceptions
    'AutomationException',
    'ValidationException',
    'ConfigException',
    'TimeoutException',
    'ElementNotFoundException',
    'ElementStateException',
    'NavigationException',
    'APIException',
    'FileException',
    'BrowserException',
    'DatabaseException',
    'IoException',
    'NotificationException',
    
    # Decorators
    'retry',
    'log_exceptions',
    'monitor_performance',
    'convert_exceptions',
    
    # Logging
    'get_logger',
    'TRACE',
    'VERBOSE',
    'NOTICE',
    'SUCCESS',
    
    # Validation
    'validate_not_none',
    'validate_type',
    'validate_instance',
    'validate_not_empty',
    'validate_min_length',
    'validate_max_length',
    'validate_in_range',
    'validate_in_options',
    'validate_pattern',
    'validate_email',
    'validate_url',
    'validate_file_exists',
    'validate_directory_exists',
    
    # Utilities
    'ensure_directory_exists',
    'load_json_file',
    'save_json_file',
    'truncate_string',
    
    # Service classes
    'api',
    'db',
    'ui',
    'utilities'
] 