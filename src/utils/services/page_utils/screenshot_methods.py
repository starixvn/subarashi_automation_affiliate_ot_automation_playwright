import datetime
from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    ExtractTestCaseFailed
)
from playwright.sync_api import Page


logger = get_logger(__name__)

class ScreenshotMethods(ExtractTestCaseFailed):
    
    def __init__(self, page: Page):
        validate_not_none(page, "page")
        self.page = page
    
    @log_exceptions(log_level="DEBUG")
    def screenshot(self, path=0):
        try:
            if bool(path):
                logger.debug(f"Taking screenshot with custom name: {path}")
                screenshot_path = 'Image\\' + path + ".png"
            else:
                timestamp = str(datetime.datetime.now()).replace(':', '.')
                screenshot_path = f'Image\\Image_{timestamp}.png'
                logger.debug(f"Taking screenshot with auto-generated name")
                
            self.page.screenshot(path=screenshot_path)
            logger.debug(f"Screenshot saved to: {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to take screenshot: {str(e)}")
            self.extract_TestCaseFailed(e)
