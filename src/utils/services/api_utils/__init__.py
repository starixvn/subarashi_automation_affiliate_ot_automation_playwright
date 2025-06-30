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
    validate_type,
    ExtractTestCaseFailed,
    TC_NAME
)

from src.utils.services.api_utils.request_methods import RequestMethods
from src.utils.services.api_utils.assertion_methods import AssertionMethods
from src.utils.services.api_utils.extraction_methods import ExtractionMethods

logger = get_logger(__name__)

class api(RequestMethods, AssertionMethods, ExtractionMethods):
    TcName = TC_NAME
    
    @log_exceptions(log_level="ERROR")
    def __init__(self, api: APIRequestContext):
        try:
            validate_not_none(api, "api")
            validate_type(api, APIRequestContext, "api")
            
            # Initialize all parent classes
            RequestMethods.__init__(self)
            AssertionMethods.__init__(self)
            ExtractionMethods.__init__(self)
            
            # Set the API context for all classes
            self.api = api
            
            logger.debug("API client initialized")
        except Exception as e:
            logger.error(f"Failed to initialize API client: {str(e)}")
            self.extract_TestCaseFailed(e)
