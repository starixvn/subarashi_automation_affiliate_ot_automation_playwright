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

from src.jobs.common.get_data_baseline_click_statistics.landing_page.get_data_baseline_landing_page_yesterday import GetDataBaselineLandingPageYesterday

class TestSuites_01_Get_Data_Baseline_Landing_Page_Yesterday(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_landing_page_yesterday = GetDataBaselineLandingPageYesterday()
        self.get_data_baseline_landing_page_yesterday.setup()
        self.utils = self.get_data_baseline_landing_page_yesterday.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_landing_page_yesterday.tearDown()

    def TestCase_01_Get_Data_Baseline_Landing_Page_Yesterday(self):
        self.get_data_baseline_landing_page_yesterday.get_data_landing_page_yesterday()

