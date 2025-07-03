import sys
import pytest
import os
import pandas as pd
import re
from typing import Optional, TYPE_CHECKING
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
    save_json_file,
    ExtractTestCaseFailed,
    TC_NAME
)

from src.utils.services.utils.browser_methods import BrowserMethods
from src.utils.services.utils.assertion_methods import AssertionMethods
from src.utils.services.utils.file_methods import FileMethods
from src.utils.services.utils.google_methods import GoogleMethods
from src.utils.services.utils.report_methods import ReportMethods
from src.utils.services.utils.crypto_methods import CryptoMethods

if TYPE_CHECKING:
    from src.utils.services.page_utils import ui
    from src.utils.services.api_utils import api
    from src.utils.services.db_utils import db

logger = get_logger(__name__)

class utilities(BrowserMethods, AssertionMethods, FileMethods, GoogleMethods, ReportMethods):
    tcsF = TC_NAME
    FuncName = None
    page: Optional['ui'] = None
    api: Optional['api'] = None  
    db: Optional['db'] = None
    
    @log_exceptions(log_level="INFO")
    def __init__(self):
        try:
            BrowserMethods.__init__(self)
            
            logger.debug(f"Clearing TC_NAME. Previously had {len(TC_NAME)} failures: {TC_NAME}")
            TC_NAME.clear()
            logger.debug(f"TC_NAME cleared successfully. Now empty: {TC_NAME}")
            
            current_test = os.getenv('PYTEST_CURRENT_TEST')
            if current_test:
                match = re.search('TestSuites_([0-9]{2}|DemoSite)_(.*).py', current_test)
                if match:
                    self.FuncName = str(match.group(2)).replace("_"," ")
                else:
                    self.FuncName = "Unknown Test Suite"
            else:
                self.FuncName = "Direct Initialization"
                
            logger.info(f"Initializing utilities for test suite: {self.FuncName}")
            
            self.env = ENVIRONMENT
            self.site = SITE
            self.debug = DEBUG_MODE
            
            if DEBUG_MODE:
                logger.debug(f"🔧 DEBUG MODE ENABLED")
                logger.debug(f"   Environment: {ENVIRONMENT}")
                logger.debug(f"   Site: {SITE}")
                logger.debug(f"   Browser enabled: {ENABLE_BROWSER}")
                logger.debug(f"   Database enabled: {ENABLE_DB}")
            
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
            # self.send_message_to_team()  
            # self.send_message_to_telegram()
            self.send_message_to_slack()
            if ENABLE_BROWSER:
                if ENABLE_TRACE:
                    logger.debug(f"Stopping tracing and saving to {TRACE_PATH}")
                    self.context.tracing.stop(path=TRACE_PATH)
                logger.debug("Closing browser and stopping Playwright")
                self.browser.close()
                self.playwright.stop()
            
            logger.debug("Clearing test case lists")
            self.tcsF.clear()
            if hasattr(self, 'page') and self.page:
                self.page.TcName.clear()
            if hasattr(self, 'api') and self.api:
                self.api.TcName.clear()
            if hasattr(self, 'db') and self.db:
                self.db.TcName.clear()
                
            logger.info("Resources cleaned up successfully")
        except Exception as e:
            logger.error(f"Error during cleanup: {str(e)}")
            
    decrypt = CryptoMethods.decrypt
