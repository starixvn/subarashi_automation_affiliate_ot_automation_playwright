from playwright.sync_api import APIResponse
import json
import re
from jsonpath_ng import parse

from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_type,
    ExtractTestCaseFailed
)

logger = get_logger(__name__)

class ExtractionMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="ERROR")
    def extract_text(self, res: APIResponse):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            
            logger.debug("Extracting text from response")
            return res.text()
        except Exception as e:
            logger.error(f"Failed to extract text from response: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def extract_status_code(self, res: APIResponse):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            
            logger.debug("Extracting status code from response")
            return res.status
        except Exception as e:
            logger.error(f"Failed to extract status code from response: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def extract_response_json(self, res: APIResponse):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            
            logger.debug("Extracting JSON from response")
            return res.json()
        except Exception as e:
            logger.error(f"Failed to extract JSON from response: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def match_by_regex(self, res: APIResponse, regex):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            validate_not_none(regex, "regex")
            validate_type(regex, str, "regex")
            
            logger.debug(f"Matching response by regex: {regex}")
            return bool(re.search(regex, res.text()))
        except Exception as e:
            logger.error(f"Failed to match response by regex: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def extract_json_string_to_dict(self, _json):
        try:
            validate_not_none(_json, "json")
            
            logger.debug("Converting JSON string to dictionary")
            return json.loads(_json)
        except Exception as e:
            logger.error(f"Failed to convert JSON string to dictionary: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def extract_by_jsonpath(self, res: APIResponse, jsonpath, index=0):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            validate_not_none(jsonpath, "jsonpath")
            validate_type(jsonpath, str, "jsonpath")
            validate_type(index, int, "index")
            
            logger.debug(f"Extracting data using JSONPath: {jsonpath}, index: {index}")
            json_data = json.loads(res.text())
            expression = parse(jsonpath)
            match = expression.find(json_data)
            return match[index].value
        except Exception as e:
            logger.error(f"Failed to extract data using JSONPath: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def match_by_jsonpath(self, res: APIResponse, jsonpath):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            validate_not_none(jsonpath, "jsonpath")
            validate_type(jsonpath, str, "jsonpath")
            
            logger.debug(f"Matching response by JSONPath: {jsonpath}")
            json_data = json.loads(res.text())
            expression = parse(jsonpath)
            match = expression.find(json_data)
            return bool(match)
        except Exception as e:
            logger.error(f"Failed to match response by JSONPath: {str(e)}")
            self.extract_TestCaseFailed(e)
