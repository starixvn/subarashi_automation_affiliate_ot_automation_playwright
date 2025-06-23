from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_url,
    validate_type,
    ExtractTestCaseFailed
)

from config.constants.settings import (
    TIMEOUT
)

logger = get_logger(__name__)

class NavigationMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="INFO")
    @monitor_performance()
    def navigate(self, url):
        try:
            validate_not_none(url, "url")
            validate_url(url, "url")
            
            logger.info(f"Navigating to URL: {url}")
            self.page.set_viewport_size({"width": 1800, "height": 800})
            self.page.goto(url)
            logger.debug(f"Successfully navigated to {url}")
        except Exception as e:
            logger.error(f"Navigation to {url} failed: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    def get_current_url(self):
        try:
            url = self.page.url
            logger.debug(f"Current URL: {url}")
            return url
        except Exception as e:
            logger.error(f"Failed to get current URL: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def reload(self):
        try:
            logger.debug("Reloading current page")
            self.page.reload()
            logger.debug("Page reloaded successfully")
        except Exception as e:
            logger.error(f"Failed to reload page: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def back_window(self):
        try:
            logger.debug("Bringing page to front")
            self.page.bring_to_front()
            logger.debug("Page brought to front successfully")
        except Exception as e:
            logger.error(f"Failed to bring page to front: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def sleep(self, time):
        try:
            validate_type(time, (int, float), "time")
            logger.debug(f"Waiting for {time}ms")
            self.page.wait_for_timeout(time)
        except Exception as e:
            logger.error(f"Sleep operation failed: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def open_new_page_by_click(self, element):
        try:
            validate_not_none(element, "element")
            logger.info(f"Opening new page by clicking element '{element}'")
            
            with self.page.context.expect_page() as page_info:
                logger.debug("Clicking element")
                self.page.click(element)
                
            new_page = page_info.value
            logger.debug("Waiting for new page to load")
            new_page.wait_for_load_state()
            
            logger.debug("Configuring new page")
            new_page.set_default_timeout(TIMEOUT*1000)
            new_page.set_default_navigation_timeout(TIMEOUT*1000)
            new_page.set_viewport_size({"width": 1800, "height": 800})
            
            logger.debug("Creating UI handler for new page")
            from src.utils.services.page_utils import ui
            self.new_pages = ui(new_page)
            logger.info("New page opened successfully")
        except Exception as e:
            logger.error(f"Failed to open new page: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    def close_page(self):
        try:
            logger.debug("Closing page")
            self.page.close()
            logger.debug("Page closed successfully")
        except Exception as e:
            logger.error(f"Failed to close page: {str(e)}")
            self.extract_TestCaseFailed(e)
