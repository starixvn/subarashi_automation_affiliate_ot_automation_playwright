from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_type,
    ExtractTestCaseFailed
)
import time

logger = get_logger(__name__)

class VerificationMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def does_element_exist(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Checking existence of element '{element}'")
            
            element_obj = self.page.locator(element)
            is_visible = element_obj.is_visible()
            logger.debug(f"Element '{element}' visibility status: {is_visible}")
            return is_visible
        except Exception as e:
            logger.error(f"Failed to check element existence: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def does_element_exist_on_frame(self, frame_xpath, element, idxChildFrame=None, idxLatestFrame=None):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Checking existence of element '{element}' on frame")
            
            if idxChildFrame == None and idxLatestFrame == None:
                if frame_xpath == "":
                    logger.debug("Using main page locator")
                    element_obj = self.page.locator(element)
                else:
                    logger.debug(f"Using frame locator with xpath: {frame_xpath}")
                    frame = self.page.frame_locator(frame_xpath)
                    element_obj = frame.locator(element)
            elif idxLatestFrame == None:
                logger.debug(f"Using child frame at index {idxChildFrame}")
                frames = self.page.frames
                childframe = frames[1].child_frames
                element_obj = childframe[idxChildFrame].locator(element)
            else:
                logger.debug(f"Using frame at index {idxLatestFrame}")
                frames = self.page.frames[idxLatestFrame]
                element_obj = frames.locator(element)
            
            is_visible = element_obj.is_visible()
            logger.debug(f"Element '{element}' visibility status: {is_visible}")
            return is_visible
        except Exception as e:
            logger.debug(f"Exception when checking element existence: {str(e)}")
            return False
            
    @log_exceptions(log_level="DEBUG")
    def verify_element_exist(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Verifying element '{element}' exists")
            
            exists = bool(self.wait_element("", element))
            logger.debug(f"Element existence: {exists}")
            assert exists == True
            logger.debug("Element existence verification successful")
        except Exception as e:
            logger.error(f"Element existence verification failed: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def wait_element(self, frame_xpath, element, state = 'visible', idxChildFrame=None) -> bool:
        try:
            validate_not_none(element, "element")
            logger.debug(f"Waiting for element '{element}' to be {state}")
            
            if frame_xpath=="" and idxChildFrame==None:
                result = bool(self.page.wait_for_selector(element, state=state))
                logger.debug(f"Element wait result: {result}")
                return result
            else:
                if idxChildFrame == None:
                    frame = self.page.frame_locator(frame_xpath)
                    element_obj = frame.locator(element)
                    element_obj.wait_for(state=state)
                    return True
                else:
                    frames = self.page.frames
                    childframe = frames[1].child_frames
                    element_obj = childframe[idxChildFrame].locator(element)
                    element_obj.wait_for(state=state)
                    return True
        except Exception as e:
            logger.error(f"Failed to wait for element: {str(e)}")
            self.extract_TestCaseFailed(e)
            return False
            
    @log_exceptions(log_level="DEBUG")
    def wait_load_page(self, state="load"):
        try:
            logger.debug(f"Waiting for page to reach '{state}' state")
            self.page.wait_for_load_state(state=state)
            logger.debug(f"Page reached '{state}' state")
        except Exception as e:
            logger.error(f"Failed to wait for page load state '{state}': {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    def is_visible(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Checking visibility of element '{element}'")
            result = self.page.locator(element).is_visible()
            logger.debug(f"Element '{element}' visibility: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to check element visibility: {str(e)}")
            return False

    @log_exceptions(log_level="DEBUG")
    def is_enabled(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Checking if element '{element}' is enabled")
            result = self.page.locator(element).is_enabled()
            logger.debug(f"Element '{element}' enabled status: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to check if element is enabled: {str(e)}")
            return False

    @log_exceptions(log_level="DEBUG")
    def wait_for_element_ready(self, selector, timeout=30, visible=True, enabled=True, stable=True):
        try:
            validate_not_none(selector, "selector")
            logger.debug(f"Waiting for element '{selector}' to be ready")
            
            start_time = time.time()
            retry_interval = 0.5
            
            while time.time() - start_time < timeout:
                try:
                    element = self.page.locator(selector)
                    
                    if element.count() == 0:
                        logger.debug(f"Element '{selector}' not found, retrying...")
                        time.sleep(retry_interval)
                        continue
                    
                    if visible and not element.is_visible():
                        logger.debug(f"Element '{selector}' not visible, retrying...")
                        time.sleep(retry_interval)
                        continue
                    
                    if enabled and not element.is_enabled():
                        logger.debug(f"Element '{selector}' not enabled, retrying...")
                        time.sleep(retry_interval)
                        continue
                    
                    if stable:
                        rect1 = element.bounding_box()
                        time.sleep(0.2)
                        rect2 = element.bounding_box()
                        
                        if rect1 and rect2 and (abs(rect1['x'] - rect2['x']) > 2 or abs(rect1['y'] - rect2['y']) > 2):
                            logger.debug(f"Element '{selector}' position unstable, retrying...")
                            time.sleep(retry_interval)
                            continue
                    
                    logger.debug(f"Element '{selector}' is ready")
                    return True
                    
                except Exception as e:
                    logger.debug(f"Exception while checking element readiness: {str(e)}")
                    time.sleep(retry_interval)
                    retry_interval = min(retry_interval * 1.5, 2.0)
            
            logger.error(f"Element '{selector}' not ready after {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"Failed to wait for element ready: {str(e)}")
            return False

    @log_exceptions(log_level="DEBUG")
    def wait_for_one_of_elements(self, selectors, timeout=30):
        try:
            validate_type(selectors, list, "selectors")
            if not selectors:
                logger.error("Empty selectors list provided")
                return None
            
            logger.debug(f"Waiting for one of {len(selectors)} elements to appear")
            
            start_time = time.time()
            while time.time() - start_time < timeout:
                for selector in selectors:
                    if self.page.locator(selector).is_visible():
                        logger.debug(f"Element '{selector}' appeared first")
                        return selector
                time.sleep(0.5)
            
            logger.warning(f"None of the elements appeared within {timeout} seconds")
            return None
        except Exception as e:
            logger.error(f"Failed to wait for one of elements: {str(e)}")
            return None

    @log_exceptions(log_level="DEBUG")
    def wait_for_network_idle(self, timeout=30, idle_time=500):
        try:
            logger.debug(f"Waiting for network to be idle for {idle_time}ms")
            self.page.wait_for_load_state("networkidle", timeout=timeout * 1000)
            logger.debug("Network is now idle")
            return True
        except Exception as e:
            logger.error(f"Failed to wait for network idle: {str(e)}")
            return False
