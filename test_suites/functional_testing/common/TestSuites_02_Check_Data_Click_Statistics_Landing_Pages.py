# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
import inspect
import pytest
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Add based on your function you define
from src.actions.common.compare_data.click_statistics_landing_page.compare_data_landing_page import CompareDataLandingPage
from src.utils.core.decorators import measure_test_execution_time

@pytest.mark.compare
@pytest.mark.functional
class TestSuites_02_Check_Data_Click_Statistics_Landing_Pages(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        CompareDataLandingPage.clear_cache()
        self.check_data_landing_page = CompareDataLandingPage()
        self.check_data_landing_page.setup()
        self.utils = self.check_data_landing_page.utils
        self.check_data_landing_page.preload_all_data()

    @classmethod
    def tearDownClass(self):
        CompareDataLandingPage.clear_cache()
        self.check_data_landing_page.tearDown()

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_01_Check_Data_Landing_Pages_Filter_By_Date_Device_Page_Language(self):
        self.check_data_landing_page.check_data_landing_pages_filter_by_date_device_page_language(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_02_Check_Data_Landing_Pages_Statistics_Match(self):
        self.check_data_landing_page.check_data_landing_pages_statistics_match(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_03_Check_Data_Landing_Pages_Click_Statistics_And_Compare(self):
        self.check_data_landing_page.check_data_landing_pages_click_statistics_and_compare(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_04_Check_Data_Landing_Pages_Signups_And_FDM(self):
        self.check_data_landing_page.check_data_signups_and_fdm(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_05_Check_Data_Landing_Pages_SubTable_Display_And_Match(self):
        self.check_data_landing_page.verify_page_website_url_match(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_06_Check_Data_Landing_Pages_Monthly_Total_Validation(self):
        self.check_data_landing_page.verify_signups_fdm_statistics_match(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_07_Check_Data_Landing_Pages_Click_Unique_Validation(self):
        self.check_data_landing_page.verify_total_clicks_has_unique_clicks(inspect.currentframe().f_code.co_name)


