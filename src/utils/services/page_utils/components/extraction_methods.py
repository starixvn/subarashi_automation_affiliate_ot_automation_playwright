import re
from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_type,
    truncate_string
)
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed
from lxml import html

logger = get_logger(__name__)

class ExtractionMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def get_attribute(self, elemment, name):
        try:
            validate_not_none(elemment, "elemment")
            validate_not_none(name, "name")
            
            logger.debug(f"Getting attribute '{name}' from element '{elemment}'")
            attr_value = self.page.get_attribute(selector=elemment, name=name)
            logger.debug(f"Got attribute value: {attr_value}")
            return attr_value
        except Exception as e:
            logger.error(f"Failed to get attribute '{name}' from element '{elemment}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_text(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Getting text of element '{element}'")
            
            text = self.page.inner_text(element)
            logger.debug(f"Retrieved text: {truncate_string(text, 100)}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text of element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_textHTML(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Getting inner HTML of element '{element}'")
            
            html = self.page.inner_html(element)
            return html
        except Exception as e:
            logger.error(f"Failed to get HTML of element '{element}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def match_by_regex(self, regex):
        try:
            validate_not_none(regex, "regex")
            logger.debug(f"Matching regex pattern '{regex}' in page content")
            
            result = bool(re.search(regex, self.page.inner_html()))
            logger.debug(f"Regex match result: {result}")
            return result
        except Exception as e:
            logger.error(f"Failed to match regex pattern '{regex}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def extract_by_regex(self, regex, group = None):
        try:
            validate_not_none(regex, "regex")
            logger.debug(f"Extracting content with regex pattern '{regex}'")
            
            match = re.search(regex, self.page.content())
            if bool(group):
                logger.debug(f"Extracting group {group} from match")
                result = match.group(group)
            else:
                logger.debug("Returning full match string")
                result = match.string
                
            return result
        except Exception as e:
            logger.error(f"Failed to extract with regex pattern '{regex}': {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_text_element_based_on_index(self, element, index):
        try:
            validate_not_none(element, "element")
            validate_type(index, int, "index")
            logger.debug(f"Getting text of element '{element}' at index {index}")
            
            text = self.get_element(element).nth(index).inner_text()
            logger.debug(f"Retrieved text: {truncate_string(text, 100)}")
            return text
        except Exception as e:
            logger.error(f"Failed to get text of element '{element}' at index {index}: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def get_attribute_element_based_on_index(self, element, index, name):
        try:
            validate_not_none(element, "element")
            validate_type(index, int, "index")
            validate_not_none(name, "name")
            logger.debug(f"Getting attribute '{name}' of element '{element}' at index {index}")
            
            attribute = self.get_element(element).nth(index).get_attribute(name)
            logger.debug(f"Retrieved attribute value: {attribute}")
            return attribute
        except Exception as e:
            logger.error(f"Failed to get attribute '{name}' of element '{element}' at index {index}: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    def extract_document(self, element):
        try:
            validate_not_none(element, "element")
            logger.debug(f"Extracting document from element")
            
            text = self.page.inner_html(element)
            document = html.fromstring(text)
            logger.debug("Document extracted successfully")
            return document
        except Exception as e:
            logger.error(f"Failed to extract document: {str(e)}")
            return html.fromstring(element)
