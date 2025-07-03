from playwright.sync_api import sync_playwright, Browser, BrowserContext, Page
from typing import Optional, TYPE_CHECKING
from config.constants.settings import (
    TIMEOUT,
    HEADLESS_MODE,
    BROWSER,
    ENABLE_BROWSER,
    ENABLE_TRACE,
    TRACE_PATH,
    DEBUG_MODE
)
from src.utils.core import (
    get_logger,
    log_exceptions,
    ExtractTestCaseFailed
)

if TYPE_CHECKING:
    from src.utils.services.page_utils import ui
    from src.utils.services.api_utils import api

logger = get_logger(__name__)

class BrowserMethods(ExtractTestCaseFailed):
    
    def __init__(self):
        self.playwright: Optional[any] = None
        self.browser: Optional[Browser] = None
        self.context: Optional[BrowserContext] = None
        self.page: Optional['ui'] = None
        self.api: Optional['api'] = None
        self.debug: bool = DEBUG_MODE
    
    @log_exceptions(log_level="INFO")
    def initialize_browser(self):
        try:
            if not ENABLE_BROWSER:
                logger.debug("Browser sessions are disabled")
                return

            logger.debug("Browser sessions are enabled, initializing Playwright")
            if DEBUG_MODE:
                logger.debug(f"🚀 Browser Configuration:")
                logger.debug(f"   Browser: {BROWSER}")
                logger.debug(f"   Headless: {HEADLESS_MODE}")
                logger.debug(f"   Timeout: {TIMEOUT}s")
                logger.debug(f"   Trace enabled: {ENABLE_TRACE}")
                logger.debug(f"   Debug mode: {DEBUG_MODE}")
                
            self.playwright = sync_playwright().start()
            
            headless_value = HEADLESS_MODE
            
            self.browser = self.playwright[BROWSER.lower()].launch(
                headless=headless_value,
                slow_mo=1000 if self.debug else 0
            )
            self.context = self.browser.new_context()
            
            if ENABLE_TRACE:
                logger.debug("Tracing is enabled, starting trace collection")
                self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
            
            self.context.set_default_timeout(TIMEOUT * 1000)
            page = self.context.new_page()

            from src.utils.services.page_utils import ui
            from src.utils.services.api_utils import api
            
            self.page = ui(page)
            self.api = api(self.context.request)
            logger.info(f"Browser {BROWSER} launched successfully in {['headful', 'headless'][headless_value]} mode")
        except Exception as e:
            logger.error(f"Failed to initialize browser: {str(e)}")
            raise
            
    @log_exceptions(log_level="DEBUG")
    def clear_browser(self):
        try:
            logger.debug("Clearing browser cookies")
            self.context.clear_cookies()
            logger.debug("Browser cookies cleared successfully")
        except Exception as e:
            logger.error(f"Failed to clear browser cookies: {str(e)}")
            raise
            
    @log_exceptions(log_level="INFO")
    def close_browser(self):
        try:
            if not ENABLE_BROWSER:
                return

            if ENABLE_TRACE:
                logger.debug(f"Stopping tracing and saving to {TRACE_PATH}")
                self.context.tracing.stop(path=TRACE_PATH)
            logger.debug("Closing browser and stopping Playwright")
            self.browser.close()
            self.playwright.stop()
            logger.debug("Browser resources released")
        except Exception as e:
            logger.error(f"Error during browser cleanup: {str(e)}")
