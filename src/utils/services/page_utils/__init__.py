import sys
import os
import re
from typing import Optional
from config.constants.settings import (
    TIMEOUT,
    SITE
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    BrowserException,
    ElementException,
    ElementNotFoundException,
    TimeoutException,
    validate_not_none,
    validate_type,
    validate_url,
    validate_not_empty,
    truncate_string,
    FileException,
    ExtractTestCaseFailed,
    TC_NAME
)
site = SITE.upper()
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
from playwright.sync_api import Page, expect

from src.utils.services.page_utils.navigation_methods import NavigationMethods
from src.utils.services.page_utils.element_methods import ElementMethods
from src.utils.services.page_utils.extraction_methods import ExtractionMethods
from src.utils.services.page_utils.frame_methods import FrameMethods
from src.utils.services.page_utils.verification_methods import VerificationMethods
from src.utils.services.page_utils.file_methods import FileMethods
from src.utils.services.page_utils.screenshot_methods import ScreenshotMethods
from src.utils.services.page_utils.waits import SmartWaits

logger = get_logger(__name__)

class ui(
    NavigationMethods, 
    ElementMethods, 
    ExtractionMethods, 
    FrameMethods,
    VerificationMethods,
    FileMethods,
    ScreenshotMethods,
    SmartWaits
):
    TcName = TC_NAME
    page: Page
    
    @log_exceptions(log_level="ERROR")
    def __init__(self, page: Page):
        try:
            validate_not_none(page, "page")
            validate_type(page, Page, "page")
            
            NavigationMethods.__init__(self, page)
            ElementMethods.__init__(self, page)
            ExtractionMethods.__init__(self, page)
            FrameMethods.__init__(self, page)
            VerificationMethods.__init__(self, page)
            FileMethods.__init__(self, page)
            ScreenshotMethods.__init__(self, page)
            SmartWaits.__init__(self, page)
            
            self.page.set_default_timeout(TIMEOUT*1000)
            self.page.set_default_navigation_timeout(TIMEOUT*1000)
            logger.debug("UI handler initialized with configured timeouts and all method classes")
        except Exception as e:
            logger.error(f"Failed to initialize UI handler: {str(e)}")
            self.extract_TestCaseFailed(e)
