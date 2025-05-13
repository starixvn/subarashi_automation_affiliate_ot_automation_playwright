import re
import os
from typing import Optional
from playwright.sync_api import Page

from src.utils.core import (
    get_logger
)

logger = get_logger(__name__)

TC_NAME = []

class ExtractTestCaseFailed:
    page: Optional[Page] = None
    
    def extract_TestCaseFailed(self, error):
        try:
            logger.error(f"Test case failure: {error}")
            if os.getenv('PYTEST_CURRENT_TEST'):
                test_case = str(re.search('::(TestCase.*) ', os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_"," ")
                TC_NAME.append(test_case)
                logger.error(f"Test case failed: {test_case}")
            else:
                logger.error("Failed to extract test case name from environment variable")
            
            logger.error(f"Error: {str(error)}")
            assert True == False 
        except Exception as e:
            logger.critical(f"Failed in error handling: {str(e)}")
            assert True == False
