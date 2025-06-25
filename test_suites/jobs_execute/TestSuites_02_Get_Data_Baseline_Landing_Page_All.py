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

from src.jobs.common.get_data_baseline_click_statistics.landing_page.get_data_baseline_landing_page_all import GetDataBaselineLandingPageAll

@pytest.mark.jobs
class TestSuites_Get_Data_Baseline_Landing_Page_All(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_landing_page_all = GetDataBaselineLandingPageAll()
        self.get_data_baseline_landing_page_all.setup()
        self.utils = self.get_data_baseline_landing_page_all.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_landing_page_all.tearDown()
    
    @pytest.mark.jobs
    def TestCase_01_Get_Data_Baseline_Landing_Page_All(self):
        self.get_data_baseline_landing_page_all.get_all_landing_page_data()
