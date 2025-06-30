from playwright.sync_api import APIRequestContext
from typing import Optional
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    ExtractTestCaseFailed
)

logger = get_logger(__name__)

class RequestMethods(ExtractTestCaseFailed):
    
    def __init__(self):
        self.api: Optional[APIRequestContext] = None
    
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def get(self, url, path=None, header=None, param=None, debug=None):
        try:
            if bool(debug):
                logger.debug(f'Url: {url}')
                logger.debug(f'Header: {header}')
                logger.debug(f'Param: {param}')
                
            if bool(path):
                full_url = url + path
            else:
                full_url = url
                
            logger.debug(f"Making GET request to {full_url}")
            res = self.api.get(url=full_url, 
                               headers=header,
                               params=param)
            
            logger.debug(f"GET request to {full_url} returned status code {res.status}")
            return res
        except Exception as e:
            logger.error(f"GET request to {url} failed: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def post(self, url, path=None, header=None, data=None, params=None, formData=None, multipart=None, debug=None):
        try:
            if bool(path):
                full_url = url + path
            else:
                full_url = url
                
            logger.debug(f"Making POST request to {full_url}")
            res = self.api.post(url=full_url, 
                                headers=header,
                                data=data,
                                params=params,
                                form=formData,
                                multipart=multipart)
                                
            if bool(debug):
                logger.debug(f"Response: {res.text()}")
                
            logger.debug(f"POST request to {full_url} returned status code {res.status}")
            return res
        except Exception as e:
            logger.error(f"POST request to {url} failed: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def put(self, url, path=None, header=None, data=None, params=None, debug=None):
        try:
            if path:
                full_url = url + path
            else:
                full_url = url
                
            logger.debug(f"Making PUT request to {full_url}")
            res = self.api.put(url=full_url, headers=header, data=data, params=params)
            
            if debug:
                logger.debug(f"Response: {res.text()}")
                
            logger.debug(f"PUT request to {full_url} returned status code {res.status}")
            return res
        except Exception as e:
            logger.error(f"PUT request to {url} failed: {str(e)}")
            self.extract_TestCaseFailed(e)
    
    @log_exceptions(log_level="ERROR")
    @monitor_performance()
    def delete(self, url, path=None, header=None, params=None, debug=None):
        try:
            if path:
                full_url = url + path
            else:
                full_url = url
                
            logger.debug(f"Making DELETE request to {full_url}")
            res = self.api.delete(url=full_url, headers=header, params=params)
            
            if debug:
                logger.debug(f"Response: {res.text()}")
                
            logger.debug(f"DELETE request to {full_url} returned status code {res.status}")
            return res
        except Exception as e:
            logger.error(f"DELETE request to {url} failed: {str(e)}")
            self.extract_TestCaseFailed(e)
