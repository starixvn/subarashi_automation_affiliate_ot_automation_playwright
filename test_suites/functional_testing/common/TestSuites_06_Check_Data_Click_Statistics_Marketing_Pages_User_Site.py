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

from src.actions.user.functional.statistics.marketing_page_tatistics.compare_data_with_admin_site import CompareDataWithAdminSite
from src.utils.core.decorators import measure_test_execution_time

@pytest.mark.compare
class TestSuites_06_Check_Data_Click_Statistics_Marketing_Pages_User_Site(unittest.TestCase):
    
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
    def TestCase_01_verify_marketing_pages_date_picker_filter(self):
        self.compare_data_with_admin.verify_page_filter_functionality(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_02_verify_marketing_pages_language_filter(self):
        self.compare_data_with_admin.verify_language_filter_functionality(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_03_verify_marketing_pages_collapsed_expanded_data_match(self):
        self.compare_data_with_admin.verify_sub_data_table_display(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_04_verify_marketing_pages_total_clicks_match_referrers(self):
        self.compare_data_with_admin.verify_total_clicks_match_referrers(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_05_verify_marketing_pages_total_clicks_match_landing_pages(self):
        self.compare_data_with_admin.verify_total_clicks_match_landing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_06_verify_marketing_pages_signups_match_referrers(self):
        self.compare_data_with_admin.verify_signups_match_referrers(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_07_verify_marketing_pages_signups_match_landing_pages(self):
        self.compare_data_with_admin.verify_signups_match_landing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_08_verify_marketing_pages_fdm_match_referrers(self):
        self.compare_data_with_admin.verify_fdm_match_referrers(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_09_verify_marketing_pages_fdm_match_landing_pages(self):
        self.compare_data_with_admin.verify_fdm_match_landing_pages(inspect.currentframe().f_code.co_name)

    @pytest.mark.compare
    @measure_test_execution_time
    def TestCase_10_verify_marketing_pages_total_clicks_has_unique_clicks(self):
        self.compare_data_with_admin.verify_total_clicks_has_unique_clicks(inspect.currentframe().f_code.co_name)
