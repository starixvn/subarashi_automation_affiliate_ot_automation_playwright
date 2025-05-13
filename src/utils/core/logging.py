"""
Logging module for the automation framework.

This module provides a customized logging setup for the automation framework,
including colored console output, custom log levels, and file logging capabilities.
"""
import os
import logging
import sys
from datetime import datetime
from typing import Optional, Union

from config.constants.settings import (
    LOG_LEVEL,
    LOG_FORMAT,
    LOG_DATE_FORMAT,
    LOG_TO_CONSOLE,
    LOG_TO_FILE,
    LOG_OUTPUT_DIR,
    LOG_FILENAME_TEMPLATE
)

# Custom log levels
TRACE = 5
VERBOSE = 15
NOTICE = 25
SUCCESS = 35

# Register custom log levels with Python's logging module
logging.addLevelName(TRACE, "TRACE")
logging.addLevelName(VERBOSE, "VERBOSE")
logging.addLevelName(NOTICE, "NOTICE")
logging.addLevelName(SUCCESS, "SUCCESS")

# Default values from settings
DEFAULT_LOG_LEVEL = LOG_LEVEL
DEFAULT_LOG_FORMAT = LOG_FORMAT
DEFAULT_DATE_FORMAT = LOG_DATE_FORMAT
DEFAULT_LOG_DIR = LOG_OUTPUT_DIR

# Terminal color codes for different log levels
COLORS = {
    "TRACE": "\033[36;2m", # Cyan, bold
    "DEBUG": "\033[36m", # Cyan
    "VERBOSE": "\033[34;2m", # Blue, bold
    "INFO": "\033[34m", # Blue
    "NOTICE": "\033[32;2m", # Green, bold
    "SUCCESS": "\033[32m", # Green
    "WARNING": "\033[33m", # Yellow
    "ERROR": "\033[31m", # Red
    "CRITICAL": "\033[31;1m", # Red, bold
    "RESET": "\033[0m", # Reset color
}

class ColoredFormatter(logging.Formatter):
    """
    Custom formatter that adds ANSI colors to log output in the console.
    Colors are only used if the output is a terminal.
    """
    def __init__(self, fmt=None, datefmt=None, use_colors=True):
        """
        Initialize the formatter with optional color support.
        
        Args:
            fmt: Log message format string
            datefmt: Date format string
            use_colors: Whether to use colors in output
        """
        super().__init__(fmt, datefmt)
        self.use_colors = use_colors and sys.stdout.isatty()
    
    def format(self, record):
        """
        Format the log record with colors if enabled.
        
        Args:
            record: The log record to format
            
        Returns:
            The formatted log record
        """
        if self.use_colors:
            levelname = record.levelname
            if levelname in COLORS:
                record.levelname = f"{COLORS[levelname]}{levelname}{COLORS['RESET']}"
                record.msg = f"{COLORS[levelname]}{record.msg}{COLORS['RESET']}"
        return super().format(record)

class AutomationLogger(logging.Logger):
    """
    Custom logger class that adds trace, verbose, notice, and success methods
    to the standard Python logger.
    """
    def trace(self, msg, *args, **kwargs):
        """Log a message at TRACE level."""
        self.log(TRACE, msg, *args, **kwargs)
    
    def verbose(self, msg, *args, **kwargs):
        """Log a message at VERBOSE level."""
        self.log(VERBOSE, msg, *args, **kwargs)
    
    def notice(self, msg, *args, **kwargs):
        """Log a message at NOTICE level."""
        self.log(NOTICE, msg, *args, **kwargs)
    
    def success(self, msg, *args, **kwargs):
        """Log a message at SUCCESS level."""
        self.log(SUCCESS, msg, *args, **kwargs)

# Set our custom logger class as the default
logging.setLoggerClass(AutomationLogger)

def get_logger(
    name: str,
    level: Optional[Union[int, str]] = None,
    log_file: Optional[str] = None,
    log_format: Optional[str] = None,
    date_format: Optional[str] = None,
    use_colors: bool = True
) -> AutomationLogger:
    """
    Get a configured logger instance.
    
    Args:
        name: The name of the logger
        level: The minimum log level (string or int)
        log_file: Path to a log file if file logging is desired
        log_format: Custom format string for log messages
        date_format: Custom format string for timestamps
        use_colors: Whether to use colors in console output
        
    Returns:
        A configured logger instance
    """
    logger = logging.getLogger(name)
    
    if level is None:
        level = os.getenv("LOG_LEVEL", DEFAULT_LOG_LEVEL)
    
    if isinstance(level, str):
        level = getattr(logging, level.upper(), logging.INFO)
    
    logger.setLevel(level)
    
    if logger.handlers:
        return logger
    
    log_format = log_format or DEFAULT_LOG_FORMAT
    date_format = date_format or DEFAULT_DATE_FORMAT
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColoredFormatter(log_format, date_format, use_colors))
    logger.addHandler(console_handler)
    
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format, date_format))
        logger.addHandler(file_handler)
    
    return logger

def configure_logging(
    log_level: Optional[Union[int, str]] = None,
    log_to_file: bool = None,
    log_to_console: bool = None,
    log_dir: Optional[str] = None,
    log_format: Optional[str] = None,
    date_format: Optional[str] = None,
    use_colors: bool = True
) -> None:
    """
    Configure the root logger with the specified settings.
    
    Args:
        log_level: The minimum log level (string or int)
        log_to_file: Whether to log to a file
        log_to_console: Whether to log to the console
        log_dir: Directory to store log files
        log_format: Custom format string for log messages
        date_format: Custom format string for timestamps
        use_colors: Whether to use colors in console output
    """
    if log_level is None:
        log_level = LOG_LEVEL
    
    if isinstance(log_level, str):
        log_level = getattr(logging, log_level.upper(), logging.INFO)
    
    if log_dir is None:
        log_dir = LOG_OUTPUT_DIR
    
    if log_to_file is None:
        log_to_file = LOG_TO_FILE
    
    if log_to_console is None:
        log_to_console = LOG_TO_CONSOLE
    
    if log_to_file and log_dir:
        os.makedirs(log_dir, exist_ok=True)
    
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    for handler in list(root_logger.handlers):
        root_logger.removeHandler(handler)
    
    log_format = log_format or DEFAULT_LOG_FORMAT
    date_format = date_format or DEFAULT_DATE_FORMAT
    
    if log_to_console:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColoredFormatter(log_format, date_format, use_colors))
        root_logger.addHandler(console_handler)
    
    if log_to_file and log_dir:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = LOG_FILENAME_TEMPLATE.replace("{timestamp}", timestamp)
        log_file = os.path.join(log_dir, log_filename)
        
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(logging.Formatter(log_format, date_format))
        root_logger.addHandler(file_handler)
    
    # Use % formatting for log messages instead of f-strings
    level_name = logging.getLevelName(log_level)
    root_logger.info("Logging configured with level: %s", level_name)
    if log_to_file and log_dir:
        root_logger.info("Log file: %s", log_file)

# Create a default logger for general use
default_logger = get_logger("automation") 