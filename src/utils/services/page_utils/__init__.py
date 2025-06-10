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
    FileException
)
site = SITE.upper()
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
from playwright.sync_api import Page, expect

from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed, TC_NAME
from src.utils.services.page_utils.components.navigation_methods import NavigationMethods
from src.utils.services.page_utils.components.element_methods import ElementMethods
from src.utils.services.page_utils.components.extraction_methods import ExtractionMethods
from src.utils.services.page_utils.components.frame_methods import FrameMethods
from src.utils.services.page_utils.components.verification_methods import VerificationMethods
from src.utils.services.page_utils.components.file_methods import FileMethods
from src.utils.services.page_utils.components.screenshot_methods import ScreenshotMethods

logger = get_logger(__name__)

class ui(
    NavigationMethods, 
    ElementMethods, 
    ExtractionMethods, 
    FrameMethods,
    VerificationMethods,
    FileMethods,
    ScreenshotMethods
):
    TcName = TC_NAME
    page: Page
    
    @log_exceptions(log_level="ERROR")
    def __init__(self, page: Page):
        try:
            validate_not_none(page, "page")
            validate_type(page, Page, "page")
            
            self.page = page
            self.page.set_default_timeout(TIMEOUT*1000)
            self.page.set_default_navigation_timeout(TIMEOUT*1000)
            logger.debug("UI handler initialized with configured timeouts")
        except Exception as e:
            logger.error(f"Failed to initialize UI handler: {str(e)}")
            self.extract_TestCaseFailed(e)
