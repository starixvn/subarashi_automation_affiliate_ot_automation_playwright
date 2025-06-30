# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
import inspect
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
import pytest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Add based on your function you define
from src.actions.common.compare_data.click_statistics_marketing_page.compare_data_marketing_page import CompareDataMarketingPage
from src.utils.core.decorators import measure_test_execution_time

@pytest.mark.compare
class TestSuites_03_Check_Data_Click_Statistics_Marketing_Pages(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        CompareDataMarketingPage.clear_cache()
        self.check_data_marketing_page = CompareDataMarketingPage()
        self.check_data_marketing_page.setup()
        self.utils = self.check_data_marketing_page.utils
        self.check_data_marketing_page.preload_all_data()

    @classmethod
    def tearDownClass(self):
        CompareDataMarketingPage.clear_cache()
        self.check_data_marketing_page.tearDown()

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_01_Check_Data_Marketing_Pages_Filter_By_Date_Language(self):
        self.check_data_marketing_page.check_data_marketing_pages_filter_by_date_language(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_02_Check_Data_Marketing_Pages_Collapsed_Expanded_Match(self):
        self.check_data_marketing_page.check_data_marketing_pages_collapsed_expanded_match(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_03_Check_Data_Marketing_Pages_Click_Statistics_Compare(self):
        self.check_data_marketing_page.check_data_marketing_pages_click_statistics_compare(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_04_Check_Data_Marketing_Pages_Signups_And_FDM(self):
        self.check_data_marketing_page.check_data_signups_and_fdm(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_05_Check_Data_Marketing_Pages_Monthly_Total_Validation(self):
        self.check_data_marketing_page.verify_signups_fdm_statistics_match(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_06_Check_Data_Marketing_Pages_Click_Unique_Validation(self):
        self.check_data_marketing_page.verify_total_clicks_has_unique_clicks(inspect.currentframe().f_code.co_name) 