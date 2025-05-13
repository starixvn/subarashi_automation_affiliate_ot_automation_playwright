import re
import os

from src.utils.core import (
    get_logger
)

logger = get_logger(__name__)

TC_NAME = []

class ExtractTestCaseFailed:
    def extract_TestCaseFailed(self, error):
        try:
            test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
            TC_NAME.append(test_case)
            logger.error(f"Test case failed: {test_case}")
            logger.error(f"Error: {str(error)}")
            assert True == False 
        except Exception as e:
            logger.critical(f"Failed in error handling: {str(e)}")
            assert True == False
