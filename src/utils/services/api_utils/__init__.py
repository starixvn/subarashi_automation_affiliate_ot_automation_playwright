from playwright.sync_api import APIRequestContext, APIResponse
import json
from jsonpath_ng import parse
import re
import os
from typing import Optional

from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    convert_exceptions,
    APIException,
    retry,
    validate_not_none,
    validate_url,
    validate_type
)

from src.utils.services.api_utils.components.request_methods import RequestMethods
from src.utils.services.api_utils.components.assertion_methods import AssertionMethods
from src.utils.services.api_utils.components.extraction_methods import ExtractionMethods
from src.utils.services.api_utils.components.extract_testcase_failed import TC_NAME,ExtractTestCaseFailed

logger = get_logger(__name__)

class api(RequestMethods, AssertionMethods, ExtractionMethods):
    TcName = TC_NAME
    api: APIRequestContext
    
    def __init__(self, api: APIRequestContext):
        try:
            validate_not_none(api, "api")
            validate_type(api, APIRequestContext, "api")
            browser_api = api
            self.api = browser_api
            logger.debug("API client initialized")
        except Exception as e:
            logger.error(f"Failed to initialize API client: {str(e)}")
            self.extract_TestCaseFailed(e)
