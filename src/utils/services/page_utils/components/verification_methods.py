from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_type
)
from typing import Optional, Union, Any
from playwright.sync_api import Locator, Page
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed

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
