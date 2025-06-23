import re
import os
from typing import Optional, Any

from src.utils.core.logging import get_logger

logger = get_logger(__name__)

TC_NAME = []

class TestCaseTracker:
    @staticmethod
    def extract_test_case_name() -> str:
        try:
            current_test = os.getenv('PYTEST_CURRENT_TEST')
            if current_test:
                match = re.search('::(TestCase.*) ', current_test)
                if match:
                    return match.group(1).replace("_", " ")
            return "Unknown Test Case"
        except Exception:
            return "Unknown Test Case"
    
    @staticmethod
    def add_failure(test_case: str):
        if test_case not in TC_NAME:
            TC_NAME.append(test_case)
    
    @staticmethod
    def get_failures():
        return TC_NAME.copy()
    
    @staticmethod
    def clear_failures():
        TC_NAME.clear()

class ExtractTestCaseFailed:
    def extract_TestCaseFailed(self, error: Exception):
        try:
            logger.error(f"Test case failure: {error}")
            test_case = TestCaseTracker.extract_test_case_name()
            TestCaseTracker.add_failure(test_case)
            logger.error(f"Test case failed: {test_case}")
            logger.error(f"Error: {str(error)}")
            raise AssertionError(f"Test case '{test_case}' failed: {str(error)}") from error
        except Exception as e:
            logger.critical(f"Failed in error handling: {str(e)}")
            raise RuntimeError(f"Critical framework error: {str(e)}") from e 