from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_type,
    truncate_string
)
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)

class FrameMethods(ExtractTestCaseFailed):
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
            
    # Và nhiều phương thức frame khác
