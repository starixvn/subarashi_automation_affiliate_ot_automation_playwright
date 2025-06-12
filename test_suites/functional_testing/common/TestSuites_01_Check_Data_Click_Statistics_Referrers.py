# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
import inspect
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Add based on your function you define
from src.actions.common.compare_data.click_statictis_referrers.compare_data_referrers import CompareDataReferrers
from src.utils.core.decorators import measure_test_execution_time

class TestSuites_01_Check_Data_Click_Statistics_Referrers(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        CompareDataReferrers.clear_cache()
        self.check_data_referrers = CompareDataReferrers()
        self.check_data_referrers.setup()
        self.utils = self.check_data_referrers.utils
        self.check_data_referrers.preload_all_data()

    @classmethod
    def tearDownClass(self):
        CompareDataReferrers.clear_cache()
        self.check_data_referrers.tearDown()

    @measure_test_execution_time
    def TestCase_01_Check_Data_Referrers_Filter_By_Date_And_Device(self):
        self.check_data_referrers.check_data_referrers_filter_by_date_and_device(inspect.currentframe().f_code.co_name)
    
    @measure_test_execution_time
    def TestCase_02_Check_Data_Referrers_Click_Statistics_And_Compare(self):
        self.check_data_referrers.check_data_referrers_click_statistics_and_compare(inspect.currentframe().f_code.co_name)

    @measure_test_execution_time
    def TestCase_03_Check_Data_Referrers_Signups_And_FDM(self):
        self.check_data_referrers.check_data_signups_and_fdm(inspect.currentframe().f_code.co_name)

    @measure_test_execution_time
    def TestCase_04_Check_Data_Referrers_SubTable_Display_And_Match(self):
        self.check_data_referrers.verify_site_url_website_url_match(inspect.currentframe().f_code.co_name)
    
    @measure_test_execution_time
    def TestCase_05_Check_Data_Referrers_Monthly_Total_Validation(self):
        self.check_data_referrers.verify_signups_fdm_statistics_match(inspect.currentframe().f_code.co_name)

    @measure_test_execution_time
    def TestCase_06_Check_Data_Referrers_Click_Unique_Validation(self):
        self.check_data_referrers.verify_total_clicks_has_unique_clicks(inspect.currentframe().f_code.co_name)
