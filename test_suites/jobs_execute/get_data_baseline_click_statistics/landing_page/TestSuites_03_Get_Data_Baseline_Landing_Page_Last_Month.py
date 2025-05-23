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

from src.jobs.common.get_data_baseline_click_statistics.landing_page.get_data_baseline_landing_page_last_month import GetDataBaselineLandingPageLastMonth

class TestSuites_03_Get_Data_Baseline_Landing_Page_Last_Month(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_landing_page_last_month = GetDataBaselineLandingPageLastMonth()
        self.get_data_baseline_landing_page_last_month.setup()
        self.utils = self.get_data_baseline_landing_page_last_month.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_landing_page_last_month.tearDown()

    def TestCase_01_Get_Data_Baseline_Landing_Page_Last_Month(self):
        self.get_data_baseline_landing_page_last_month.get_data_landing_page_last_month()

