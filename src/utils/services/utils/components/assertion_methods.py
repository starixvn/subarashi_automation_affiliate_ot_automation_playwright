import re
import os
from src.utils.core import (
    get_logger,
    log_exceptions,
    validate_not_none,
    ExtractTestCaseFailed,
    TC_NAME
)

logger = get_logger(__name__)

class AssertionMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    def should_be_equal(self, actual, expect): 
        try:
            validate_not_none(actual, "actual")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting equality: expected '{expect}', actual '{actual}'")
            if actual != expect:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Equality assertion failed: {test_case}")
                logger.error(f"Expected: {expect}, Actual: {actual}")
                TC_NAME.append(test_case)
            
            assert actual == expect
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise

    @log_exceptions(log_level="DEBUG")
    def should_be_lower_than(self, value, expect): 
        try:
            validate_not_none(value, "value")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting '{value}' is lower than or equal to '{expect}'")
            if value > expect:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Lower than assertion failed: {test_case}")
                logger.error(f"Expected value to be <= {expect}, Actual: {value}")
                TC_NAME.append(test_case)
            
            assert value <= expect
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise

    @log_exceptions(log_level="DEBUG")
    def should_be_greater_than_or_equal(self, value, expect): 
        try:
            validate_not_none(value, "value")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting '{value}' is greater than or equal to '{expect}'")
            if value < expect:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Greater than assertion failed: {test_case}")
                logger.error(f"Expected value to be >= {expect}, Actual: {value}")
                TC_NAME.append(test_case)
            
            assert value >= expect
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise
        
    @log_exceptions(log_level="DEBUG")
    def should_be_not_equal(self, actual, expect):  
        try:
            validate_not_none(actual, "actual")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting '{actual}' is not equal to '{expect}'")
            if actual == expect:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Not equal assertion failed: {test_case}")
                logger.error(f"Expected values to be different, but both are: {actual}")
                TC_NAME.append(test_case)
            
            assert actual != expect
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise

    @log_exceptions(log_level="DEBUG")
    def should_not_contain(self, originalData, expect):  
        try:
            validate_not_none(originalData, "originalData")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting '{originalData}' does not contain '{expect}'")
            if expect in originalData:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Not contain assertion failed: {test_case}")
                logger.error(f"Expected '{originalData}' to not contain '{expect}'")
                TC_NAME.append(test_case)
            
            assert expect not in originalData
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise

    @log_exceptions(log_level="DEBUG")
    def should_contain(self, originalData, expect):  
        try:
            validate_not_none(originalData, "originalData")
            validate_not_none(expect, "expect")
            
            logger.debug(f"Asserting '{originalData}' contains '{expect}'")
            if expect not in originalData:
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                logger.error(f"Contain assertion failed: {test_case}")
                logger.error(f"Expected '{originalData}' to contain '{expect}'")
                TC_NAME.append(test_case)
            
            assert expect in originalData
        except Exception as e:
            logger.error(f"Assertion error: {str(e)}")
            raise
