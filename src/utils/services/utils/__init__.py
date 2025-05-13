import sys
import pytest
import os
import pandas as pd
import re
from config.constants.settings import (
    ENABLE_BROWSER,
    ENABLE_TRACE,
    TRACE_PATH,
    ENVIRONMENT,
    SITE,
    ENABLE_DB,
    DEBUG_MODE
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    FileException,
    BrowserException,
    APIException,
    ValidationException,
    NotificationException,
    validate_not_none,
    validate_type,
    validate_not_empty,
    ensure_directory_exists,
    truncate_string,
    load_json_file,
    save_json_file
)

from src.utils.services.utils.components.browser_methods import BrowserMethods
from src.utils.services.utils.components.assertion_methods import AssertionMethods
from src.utils.services.utils.components.file_methods import FileMethods
from src.utils.services.utils.components.google_methods import GoogleMethods
from src.utils.services.utils.components.report_methods import ReportMethods
from src.utils.services.utils.components.crypto_methods import CryptoMethods
from src.utils.services.utils.components.extract_testcase_failed import TC_NAME

logger = get_logger(__name__)

class utilities(BrowserMethods, AssertionMethods, FileMethods, GoogleMethods, ReportMethods):
    """
    Core utilities class that combines all utility components.
    """
    tcsF = TC_NAME
    FuncName = None
    
    @log_exceptions(log_level="INFO")
    def __init__(self):
        try:
            self.FuncName = str(re.search('TestSuites_([0-9]{2}|DemoSite)_(.*).py', os.getenv('PYTEST_CURRENT_TEST')).group(2)).replace("_"," ")
            logger.info(f"Initializing utilities for test suite: {self.FuncName}")
            
            self.env = ENVIRONMENT
            self.site = SITE
            self.debug = DEBUG_MODE if 'DEBUG_MODE' in globals() else False
            
            if ENABLE_BROWSER:
                self.initialize_browser()
                
            if ENABLE_DB:
                logger.debug("Database connections are enabled, initializing DB")
                from src.utils.services.db_utils import db
                self.db = db()
                
        except Exception as e:
            logger.error(f"Failed to initialize utilities: {str(e)}")
            raise

    @log_exceptions(log_level="INFO")
    @monitor_performance()
    def destroy(self):
        try:
            logger.info("Cleaning up resources and sending reports")
            self.send_message_to_team()  
            self.send_message_to_telegram()
            if ENABLE_BROWSER:
                if ENABLE_TRACE:
                    logger.debug(f"Stopping tracing and saving to {TRACE_PATH}")
                    self.context.tracing.stop(path=TRACE_PATH)
                logger.debug("Closing browser and stopping Playwright")
                self.browser.close()
                self.playwright.stop()
            
            logger.debug("Clearing test case lists")
            self.tcsF.clear()
            if hasattr(self, 'page'):
                self.page.TcName.clear()
            if hasattr(self, 'api'):
                self.api.TcName.clear()
            if hasattr(self, 'db'):
                self.db.TcName.clear()
                
            logger.info("Resources cleaned up successfully")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")
            
    decrypt = CryptoMethods.decrypt
