import datetime
from src.utils.core import (
    get_logger,
    log_exceptions
)
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)

class ScreenshotMethods(ExtractTestCaseFailed):
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
