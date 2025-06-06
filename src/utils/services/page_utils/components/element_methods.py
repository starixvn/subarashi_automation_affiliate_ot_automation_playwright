import time
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_type,
    validate_not_empty
)
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)

class ElementMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def input(self, element, text):
        try:
            validate_not_none(element, "element")
            
            logger.debug(f"Filling text in element '{element}'")
            self.page.fill(element, "")
            self.page.fill(element, text)
            logger.debug(f"Element '{element}' filled with text")
        except Exception as e:
            logger.error(f"Failed to input text in element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def click(self, element):
        try:
            validate_not_none(element, "element")
            
            logger.debug(f"Clicking element: {element}")
            self.page.click(element)
            logger.debug(f"Element {element} clicked")
        except Exception as e:
            logger.error(f"Failed to click element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_element(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Getting element with selector: {element}")
            return self.page.locator(element)
        except Exception as e:
            logger.error(f"Failed to get element with selector '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def select_options(self, element, values):
        try:
            validate_not_none(element, "element")
            validate_not_none(values, "values")
            
            logger.debug(f"Selecting options '{values}' in element '{element}'")
            self.page.select_option(element, values)
            logger.debug(f"Options selected in element '{element}'")
        except Exception as e:
            logger.error(f"Failed to select options in element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def press_key(self, key, element = "body"):
        try:
            validate_not_none(key, "key")
            logger.debug(f"Pressing key '{key}' on element '{element}'")
            
            self.page.press(element, key)
            logger.debug(f"Key '{key}' pressed successfully")
        except Exception as e:
            logger.error(f"Failed to press key '{key}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def click_element_based_on_index(self, element, index):
        try:
            validate_not_none(element, "element")
            validate_type(index, int, "index")
            logger.debug(f"Clicking element '{element}' at index {index}")
            
            result = self.get_element(element).nth(index).click()
            logger.debug(f"Successfully clicked element at index {index}")
            return result
        except Exception as e:
            logger.error(f"Failed to click element '{element}' at index {index}: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def select_multiple(self, element, values):
        try:
            validate_not_none(element, "element")
            validate_not_empty(values, "values")
            
            logger.info(f"Selecting multiple checkboxes with base element '{element}'")
            
            for value in values:
                logger.debug(f"Selecting value: {value}")
                checkbox_label_selector = element + f"[normalize-space(text())='{value}']"
                checkbox_selector = f'{checkbox_label_selector}/../input[@type="checkbox"]'
                
                logger.debug(f"Clicking checkbox with selector: {checkbox_selector}")
                self.page.click(checkbox_selector)
                
            logger.info(f"Successfully selected {len(values)} values")
        except Exception as e:
            logger.error(f"Failed to select multiple values: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def count_element(self, frame_xpath, element, idxChildFrame=None, idxLatestFrame=None):
        try :
            validate_not_none(frame_xpath, "frame_xpath")
            validate_not_none(element, "element")
            if idxChildFrame == None and idxLatestFrame == None:
                if frame_xpath == "":
                    element = self.page.locator(element)
                else:
                    frame = self.page.frame_locator(frame_xpath)
                    element = frame.locator(element)
            elif idxLatestFrame == None:
                frames = self.page.frames
                childframe = frames[1].child_frames
                element = childframe[idxChildFrame].locator(element)
            else:
                frames = self.page.frames[idxLatestFrame]
                element = frames.locator(element)
            
            logger.debug(f"Total count of elements: {element.count()}")

            return element.count()
        except Exception as e:
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="DEBUG")
    def scroll_to_element(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Scrolling to element '{element}'")
            self.page.locator(element).scroll_into_view_if_needed()
            logger.debug("Scroll to element completed")
            return True
        except Exception as e:
            logger.error(f"Failed to scroll to element: {str(e)}")
            self.extract_TestCaseFailed(e)
            return False

    @log_exceptions(log_level="DEBUG")
    def click_with_retry(self, element, max_attempts=3, retry_interval=1.0):
        try:
            validate_not_none(element, "element")
            
            for attempt in range(1, max_attempts + 1):
                try:
                    logger.debug(f"Clicking element '{element}' (attempt {attempt}/{max_attempts})")
                    
                    self.scroll_to_element(element)
                    
                    time.sleep(0.2)
                    
                    self.page.locator(element).click()
                    logger.debug(f"Element '{element}' clicked successfully")
                    return True
                except Exception as click_error:
                    if attempt == max_attempts:
                        raise click_error
                    logger.debug(f"Click attempt {attempt} failed: {str(click_error)}")
                    time.sleep(retry_interval)
            
            return False
        except Exception as e:
            logger.error(f"Failed to click element '{element}' after {max_attempts} attempts: {str(e)}")
            self.extract_TestCaseFailed(e)
            return False

    @log_exceptions(log_level="DEBUG")
    def hover(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Hovering over element '{element}'")
            self.page.locator(element).hover()
            logger.debug(f"Successfully hovered over '{element}'")
            return True
        except Exception as e:
            logger.error(f"Failed to hover over element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            return False