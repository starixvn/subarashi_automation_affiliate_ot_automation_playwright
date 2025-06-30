import re
import os
from typing import Optional, Any

from src.utils.core.logging import get_logger

logger = get_logger(__name__)

TC_NAME = []

class ExtractTestCaseFailed:
    def extract_TestCaseFailed(self, error):
        try:
            logger.error(f"Test case failure: {error}")
            if os.getenv('PYTEST_CURRENT_TEST'):
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                TC_NAME.append(test_case)
                logger.error(f"Test case failed: {test_case}")
                logger.debug(f"TC_NAME now contains {len(TC_NAME)} failures: {TC_NAME}")
            else:
                logger.error("Failed to extract test case name from environment variable")
            
            logger.error(f"Error: {str(error)}")
            assert True == False
        except Exception as e:
            logger.critical(f"Failed in error handling: {str(e)}")
            assert True == False 