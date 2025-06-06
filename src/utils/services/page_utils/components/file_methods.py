import os
from src.utils.core import (
    get_logger,
    log_exceptions,
    monitor_performance,
    validate_not_none,
    validate_not_empty,
    FileException
)
from src.utils.services.page_utils.components.extract_testcase_failed import ExtractTestCaseFailed
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
logger = get_logger(__name__)

class FileMethods(ExtractTestCaseFailed):
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def save_excel(self, element):
        try:
            validate_not_none(element, "element")
            logger.info(f"Saving Excel file from element '{element}'")
            
            with self.page.expect_download() as download_info:
                logger.debug("Clicking element to trigger download")
                self.page.locator(element).click()
                
            download = download_info.value
            file_name = download.suggested_filename
            save_path = os.path.join(root_dir + os.sep + 'TestResult' + os.sep + 'export_excel'+ os.sep + file_name)
            
            logger.debug(f"Saving downloaded file to: {save_path}")
            download.save_as(save_path)
            
            if os.path.exists(save_path):
                logger.info(f"File successfully saved: {file_name}")
                return file_name
            else:
                logger.error(f"Download failed. File not found: {save_path}")
                raise FileException(
                    message="Download failed",
                    file_path=save_path,
                    details="File not saved to expected location"
                )
        except Exception as e:
            logger.error(f"Failed to save Excel file: {str(e)}")
            self.extract_TestCaseFailed(e)
            
    @log_exceptions(log_level="DEBUG")
    @monitor_performance()
    def uploadfile(self, element, filechooser_list):
        try:
            validate_not_none(element, "element")
            validate_not_empty(filechooser_list, "filechooser_list")
            
            data_upload_path = os.path.join(root_dir, 'DataSet', 'DataUpload')
            logger.info(f"Uploading {len(filechooser_list)} files using element '{element}'")
            
            for filechooser in filechooser_list:
                logger.debug(f"Uploading file: {filechooser}")
                with self.page.expect_file_chooser() as fc_info:
                    self.page.locator(element).click()
                    file_chooser = fc_info.value
                    file_path = os.path.join(data_upload_path, filechooser)
                    
                    if not os.path.exists(file_path):
                        logger.error(f"Upload file not found: {file_path}")
                        raise FileException(
                            message="Upload file not found",
                            file_path=file_path
                        )
                    
                    logger.debug(f"Setting file path: {file_path}")
                    file_chooser.set_files(file_path)
                    
            logger.info("File upload completed successfully")
        except Exception as e:
            logger.error(f"Failed to upload files: {str(e)}")
            self.extract_TestCaseFailed(e)
    
