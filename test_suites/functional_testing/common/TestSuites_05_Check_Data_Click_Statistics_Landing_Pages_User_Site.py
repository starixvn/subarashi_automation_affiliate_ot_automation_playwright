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
from src.actions.user.functional.statistics.landing_pages_statistics.compare_data_with_admin_site import CompareDataWithAdminSite
from src.utils.core.decorators import measure_test_execution_time

@pytest.mark.compare
@pytest.mark.functional
class TestSuites_05_Check_Data_Click_Statistics_Landing_Pages_User_Site(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        CompareDataWithAdminSite.clear_cache()
        cls.compare_data_with_admin = CompareDataWithAdminSite()
        cls.compare_data_with_admin.setup()
        cls.utils = cls.compare_data_with_admin.utils
        cls.compare_data_with_admin.preload_all_data()

    @classmethod
    def tearDownClass(cls):
        cls.compare_data_with_admin.tearDown()
        CompareDataWithAdminSite.clear_cache()

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_01_Verify_Landing_Pages_Data_Accuracy_By_Page_Filter(self):
        self.compare_data_with_admin.verify_page_filter_accuracy(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_02_Verify_Landing_Pages_Data_Accuracy_By_Date_Picker(self):
        self.compare_data_with_admin.verify_date_picker_accuracy(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_03_Verify_Landing_Pages_Data_Accuracy_By_Language_Filter(self):
        self.compare_data_with_admin.verify_language_filter_accuracy(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_04_Verify_Landing_Pages_Data_Accuracy_By_Device_Filter(self):
        self.compare_data_with_admin.verify_device_filter_accuracy(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_05_Verify_Total_Clicks_Landing_Pages_Equals_Referrers(self):
        self.compare_data_with_admin.verify_total_clicks_vs_referrers(inspect.currentframe().f_code.co_name)
    
    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_06_Verify_Total_Clicks_Landing_Pages_Equals_Marketing_Pages(self):
        self.compare_data_with_admin.verify_total_clicks_vs_marketing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_07_Verify_Signups_Landing_Pages_Equals_Referrers(self):
        self.compare_data_with_admin.verify_signups_vs_referrers(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_08_Verify_Signups_Landing_Pages_Equals_Marketing_Pages(self):
        self.compare_data_with_admin.verify_signups_vs_marketing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_09_Verify_FDM_Landing_Pages_Equals_Referrers(self):
        self.compare_data_with_admin.verify_fdm_vs_referrers(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_10_Verify_FDM_Landing_Pages_Equals_Marketing_Pages(self):
        self.compare_data_with_admin.verify_fdm_vs_marketing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_11_Verify_Sub_Data_Table_Display_When_Clicking_Pages(self):
        self.compare_data_with_admin.verify_sub_data_table_display(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_12_Verify_Sub_Data_Table_Values_Match_Main_Table(self):
        self.compare_data_with_admin.verify_sub_data_table_values_match(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_13_Verify_Total_Clicks_Implies_Unique_Clicks_Data(self):
        self.compare_data_with_admin.verify_total_unique_clicks_relationship(inspect.currentframe().f_code.co_name) 