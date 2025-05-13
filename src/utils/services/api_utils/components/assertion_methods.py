from playwright.sync_api import APIResponse
import re

from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    validate_type,
    APIException
)
from src.utils.services.api_utils.components.extract_testcase_failed import ExtractTestCaseFailed

logger = get_logger(__name__)

class AssertionMethods(ExtractTestCaseFailed):
    def set_auth(self, token):
        try:
            validate_not_none(token, "token")
            validate_type(token, str, "token")
            logger.debug("Setting Authorization token")
            self.api.headers.update({"Authorization": f"Bearer {token}"})
        except Exception as e:
            logger.error(f"Failed to set authorization token: {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def assert_status_code(self, res: APIResponse, expected_status_code):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            validate_not_none(expected_status_code, "expected_status_code")
            validate_type(expected_status_code, int, "expected_status_code")
            
            logger.debug(f"Asserting status code: Expected {expected_status_code}, Actual {res.status}")
            assert res.status == expected_status_code, f"Expected status code {expected_status_code}, but got {res.status}"
        except AssertionError as e:
            logger.error(f"Status code assertion failed: {str(e)}")
            raise APIException(
                message=f"Status code assertion failed",
                status_code=res.status,
                details=f"Expected status code {expected_status_code}, but got {res.status}",
                original_exception=e
            )

    @log_exceptions(log_level="ERROR")
    def assert_response_contains(self, res: APIResponse, expected_content):
        try:
            validate_not_none(res, "res")
            validate_type(res, APIResponse, "res")
            validate_not_none(expected_content, "expected_content")
            
            response_text = res.text()
            logger.debug(f"Asserting response contains: '{expected_content}'")
            assert expected_content in response_text, f"Expected content '{expected_content}' not found in response"
        except AssertionError as e:
            logger.error(f"Response content assertion failed: {str(e)}")
            raise APIException(
                message=f"Response content assertion failed",
                details=f"Expected content '{expected_content}' not found in response",
                original_exception=e
            )
    
    @log_exceptions(log_level="ERROR")
    def get_cookie(self, cookie_name):
        try:
            validate_not_none(cookie_name, "cookie_name")
            validate_type(cookie_name, str, "cookie_name")
            
            logger.debug(f"Getting cookie with name: {cookie_name}")
            return self.api.cookies().get(cookie_name)
        except Exception as e:
            logger.error(f"Failed to get cookie '{cookie_name}': {str(e)}")
            self.extract_TestCaseFailed(e)

    @log_exceptions(log_level="ERROR")
    def set_cookie(self, cookie_name, cookie_value):
        try:
            validate_not_none(cookie_name, "cookie_name")
            validate_type(cookie_name, str, "cookie_name")
            validate_not_none(cookie_value, "cookie_value")
            
            logger.debug(f"Setting cookie: {cookie_name}={cookie_value}")
            self.api.add_cookie(name=cookie_name, value=cookie_value)
        except Exception as e:
            logger.error(f"Failed to set cookie '{cookie_name}': {str(e)}")
            self.extract_TestCaseFailed(e)
