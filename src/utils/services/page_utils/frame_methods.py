from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_type,
    truncate_string,
    ExtractTestCaseFailed
)
from playwright.sync_api import Page
import time

logger = get_logger(__name__)

class FrameMethods(ExtractTestCaseFailed):
    
    def __init__(self, page: Page):
        validate_not_none(page, "page")
        self.page = page
    
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def input_on_frame(self, frame_xpath, element, text, idxChildFrame=None):  
        try:
            validate_not_none(element, "element")
            
            logger.debug(f"Filling text in element '{element}' on frame")
            if idxChildFrame == None:
                if frame_xpath == "":
                    logger.debug("Using main page locator")
                    element_obj = self.page.locator(element)
                else:
                    logger.debug(f"Using frame locator with xpath: {frame_xpath}")
                    frame = self.page.frame_locator(frame_xpath)
                    element_obj = frame.locator(element)
            else:
                logger.debug(f"Using child frame at index {idxChildFrame}")
                frames = self.page.frames
                childframe = frames[1].child_frames
                element_obj = childframe[idxChildFrame].locator(element)

            element_obj.fill("")
            element_obj.fill(text)
            logger.debug(f"Element '{element}' on frame filled with text")
        except Exception as e:
            logger.error(f"Failed to input text in frame element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def click_on_frame(self, frame_xpath, element, idxChildFrame=None, idxLatestFrame=None):
        try:
            validate_not_none(element, "element")
            
            logger.debug(f"Clicking element '{element}' on frame")

            if idxChildFrame == None and idxLatestFrame == None:
                if frame_xpath == "":
                    logger.debug("Using main page locator")
                    element_obj = self.page.locator(element)
                    element_obj.click()
                else:
                    logger.debug(f"Using frame locator with xpath: {frame_xpath}")
                    frame = self.page.frame_locator(frame_xpath)
                    frame.locator(element).click()
            elif idxLatestFrame == None:
                logger.debug(f"Using child frame at index {idxChildFrame}")
                frames = self.page.frames
                childframe = frames[1].child_frames
                childframe[idxChildFrame].locator(element).focus()
                childframe[idxChildFrame].locator(element).click()
            else:
                logger.debug(f"Using frame at index {idxLatestFrame}")
                frames = self.page.frames[idxLatestFrame]
                
                frames.locator(element).focus()
                frames.locator(element).click()
            logger.debug(f"Element {element} on frame clicked")
        except Exception as e:
            logger.error(f"Failed to click frame element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_text_on_frame(self, frame_xpath, element, idxChildFrame=None, idxLatestFrame=None):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Getting text of element '{element}' on frame")
            
            if idxChildFrame == None and idxLatestFrame == None:
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

            text = element_obj.inner_text()
            logger.debug(f"Retrieved text: {truncate_string(text, 100)}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text of frame element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def wait_for_element_on_frame(self, frame_xpath, element, state='visible', timeout=30, idxChildFrame=None, idxLatestFrame=None):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Waiting for element '{element}' on frame to be {state}")
            
            start_time = time.time()
            retry_interval = 0.5
            
            while time.time() - start_time < timeout:
                try:
                    if idxChildFrame == None and idxLatestFrame == None:
                        if frame_xpath == "":
                            element_obj = self.page.locator(element)
                        else:
                            frame = self.page.frame_locator(frame_xpath)
                            element_obj = frame.locator(element)
                    elif idxLatestFrame == None:
                        frames = self.page.frames
                        childframe = frames[1].child_frames
                        element_obj = childframe[idxChildFrame].locator(element)
                    else:
                        frames = self.page.frames[idxLatestFrame]
                        element_obj = frames.locator(element)
                    
                    if state == 'visible' and element_obj.is_visible():
                        logger.debug(f"Element '{element}' on frame is now visible")
                        return True
                    elif state == 'hidden' and not element_obj.is_visible():
                        logger.debug(f"Element '{element}' on frame is now hidden")
                        return True
                    elif state == 'enabled' and element_obj.is_enabled():
                        logger.debug(f"Element '{element}' on frame is now enabled")
                        return True
                    elif state == 'attached' and element_obj.count() > 0:
                        logger.debug(f"Element '{element}' on frame is now attached")
                        return True
                    elif state == 'detached' and element_obj.count() == 0:
                        logger.debug(f"Element '{element}' on frame is now detached")
                        return True
                    
                    time.sleep(retry_interval)
                except Exception as e:
                    logger.debug(f"Exception while waiting for element on frame: {str(e)}")
                    time.sleep(retry_interval)
            
            logger.error(f"Element '{element}' on frame not in state '{state}' after {timeout} seconds")
            return False
        except Exception as e:
            logger.error(f"Failed to wait for element on frame: {str(e)}")
            return False