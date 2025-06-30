import time
from typing import Callable, Optional
from playwright.sync_api import Page, Locator

from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_type,
    validate_not_empty,
    ExtractTestCaseFailed
)

logger = get_logger(__name__)

class SmartWaits(ExtractTestCaseFailed):
    
    def __init__(self, page: Page, default_timeout: int = 30):
        validate_not_none(page, "page")
        validate_type(default_timeout, int, "default_timeout")
        self.page = page
        self.default_timeout = default_timeout
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_element_ready(self, selector: str, timeout: Optional[int] = None) -> bool:
        try:
            validate_not_none(selector, "selector")
            validate_not_empty(selector, "selector")
            
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug(f"Smart wait: Waiting for element '{selector}' to be ready")
            
            element = self.page.locator(selector)
            element.wait_for(state="attached", timeout=timeout * 1000)
            
            element.wait_for(state="visible", timeout=5000)
            
            self._wait_for_element_stable(element)
            
            elapsed = time.time() - start_time
            logger.debug(f"Smart wait: Element ready in {elapsed:.2f}s")
            return True
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: Element not ready after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_text_to_appear(self, text: str, timeout: Optional[int] = None) -> bool:
        try:
            validate_not_none(text, "text")
            validate_not_empty(text, "text")
            
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug(f"Smart wait: Waiting for text '{text}' to appear")
            
            self.page.wait_for_function(
                f"document.body.innerText.includes('{text}')",
                timeout=timeout * 1000
            )
            
            elapsed = time.time() - start_time
            logger.debug(f"Smart wait: Text appeared in {elapsed:.2f}s")
            return True
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: Text not found after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_page_loaded(self, timeout: Optional[int] = None) -> bool:
        try:
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug("Smart wait: Waiting for page to load completely")
            
            self.page.wait_for_load_state("domcontentloaded", timeout=timeout * 1000)
            
            self.page.wait_for_load_state("networkidle", timeout=timeout * 1000)
            
            elapsed = time.time() - start_time
            logger.debug(f"Smart wait: Page loaded in {elapsed:.2f}s")
            return True
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: Page load timeout after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_url_change(self, current_url: str, timeout: Optional[int] = None) -> bool:
        try:
            validate_not_none(current_url, "current_url")
            validate_not_empty(current_url, "current_url")
            
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug(f"Smart wait: Waiting for URL to change from '{current_url}'")
            
            self.page.wait_for_function(
                f"window.location.href !== '{current_url}'",
                timeout=timeout * 1000
            )
            
            elapsed = time.time() - start_time
            new_url = self.page.url
            logger.debug(f"Smart wait: URL changed to '{new_url}' in {elapsed:.2f}s")
            return True
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: URL didn't change after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_condition(self, condition: Callable[[], bool], 
                          description: str = "condition", 
                          timeout: Optional[int] = None,
                          poll_interval: float = 0.5) -> bool:
        try:
            validate_not_none(condition, "condition")
            validate_not_none(description, "description")
            validate_type(poll_interval, (int, float), "poll_interval")
            
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug(f"Smart wait: Waiting for {description}")
            
            while time.time() - start_time < timeout:
                if condition():
                    elapsed = time.time() - start_time
                    logger.debug(f"Smart wait: {description} completed in {elapsed:.2f}s")
                    return True
                time.sleep(poll_interval)
            
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: {description} timeout after {elapsed:.2f}s")
            raise TimeoutError(f"Condition '{description}' not met within {timeout}s")
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: {description} failed after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def wait_for_ajax_complete(self, timeout: Optional[int] = None) -> bool:
        try:
            timeout = timeout or self.default_timeout
            start_time = time.time()
            
            logger.debug("Smart wait: Waiting for AJAX requests to complete")
            
            self.page.wait_for_function(
                "typeof jQuery === 'undefined' || jQuery.active === 0",
                timeout=timeout * 1000
            )
            
            elapsed = time.time() - start_time
            logger.debug(f"Smart wait: AJAX completed in {elapsed:.2f}s")
            return True
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"Smart wait: AJAX timeout after {elapsed:.2f}s: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    def adaptive_wait(self, base_seconds: float = 1.0, reason: str = "operation") -> None:
        try:
            validate_type(base_seconds, (int, float), "base_seconds")
            validate_not_none(reason, "reason")
            
            start = time.time()
            
            self.page.evaluate("document.readyState")
            response_time = time.time() - start
            
            if response_time > 0.5:
                actual_wait = base_seconds * 1.5
                logger.debug(f"Adaptive wait: Slow system detected, waiting {actual_wait:.1f}s for {reason}")
            elif response_time < 0.1:
                actual_wait = base_seconds * 0.7
                logger.debug(f"Adaptive wait: Fast system detected, waiting {actual_wait:.1f}s for {reason}")
            else:
                actual_wait = base_seconds
                logger.debug(f"Adaptive wait: Normal timing, waiting {actual_wait:.1f}s for {reason}")
            
            time.sleep(actual_wait)
            
        except Exception as e:
            logger.error(f"Adaptive wait failed: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="DEBUG")
    def _wait_for_element_stable(self, element: Locator, stability_time: float = 0.5) -> bool:
        try:
            validate_not_none(element, "element")
            validate_type(stability_time, (int, float), "stability_time")
            
            previous_box = None
            stable_start = time.time()
            
            while time.time() - stable_start < stability_time:
                current_box = element.bounding_box()
                
                if previous_box is not None:
                    if (current_box and previous_box and 
                        abs(current_box['x'] - previous_box['x']) < 2 and
                        abs(current_box['y'] - previous_box['y']) < 2):
                        return True
                    else:
                        stable_start = time.time()
                
                previous_box = current_box
                time.sleep(0.1)
            
            return True
            
        except Exception as e:
            logger.error(f"Element stability check failed: {str(e)}")
            self.extract_TestCaseFailed(e)

@log_exceptions(log_level="DEBUG")
def smart_wait_for_element(page: Page, selector: str, timeout: int = 30) -> bool:
    validate_not_none(page, "page")
    validate_not_none(selector, "selector")
    validate_not_empty(selector, "selector")
    
    waits = SmartWaits(page, timeout)
    return waits.wait_for_element_ready(selector, timeout)

@log_exceptions(log_level="DEBUG")
def smart_wait_for_text(page: Page, text: str, timeout: int = 30) -> bool:
    validate_not_none(page, "page")
    validate_not_none(text, "text")
    validate_not_empty(text, "text")
    
    waits = SmartWaits(page, timeout)
    return waits.wait_for_text_to_appear(text, timeout)

@log_exceptions(log_level="DEBUG")
def smart_wait_page_load(page: Page, timeout: int = 30) -> bool:
    validate_not_none(page, "page")
    
    waits = SmartWaits(page, timeout)
    return waits.wait_for_page_loaded(timeout)

@log_exceptions(log_level="DEBUG")
def replace_sleep(page: Page, seconds: float, reason: str = "wait") -> None:
    validate_not_none(page, "page")
    validate_type(seconds, (int, float), "seconds")
    validate_not_none(reason, "reason")
    
    waits = SmartWaits(page)
    waits.adaptive_wait(seconds, reason) 