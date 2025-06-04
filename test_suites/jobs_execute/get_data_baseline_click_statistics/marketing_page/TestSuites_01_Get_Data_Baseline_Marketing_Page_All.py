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

from src.jobs.common.get_data_baseline_click_statistics.marketing_page.get_data_baseline_marketing_page_all import GetDataBaselineMarketingPageAll


class TestSuites_Get_Data_Baseline_Marketing_Page_All(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_marketing_page_all = GetDataBaselineMarketingPageAll()
        self.get_data_baseline_marketing_page_all.setup()
        self.utils = self.get_data_baseline_marketing_page_all.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_marketing_page_all.tearDown()

    def TestCase_01_Get_Data_Baseline_Marketing_Page_All(self):
        self.get_data_baseline_marketing_page_all.get_all_marketing_page_data()