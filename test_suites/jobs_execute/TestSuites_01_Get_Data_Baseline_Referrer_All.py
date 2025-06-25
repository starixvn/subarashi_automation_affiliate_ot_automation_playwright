# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
import pytest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

from src.jobs.common.get_data_baseline_click_statistics.referrers.get_data_baseline_referrer_all import GetDataBaselineReferrerAll

@pytest.mark.jobs
class TestSuites_Get_Data_Baseline_Referrer_All(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_referrer_all = GetDataBaselineReferrerAll()
        self.get_data_baseline_referrer_all.setup()
        self.utils = self.get_data_baseline_referrer_all.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_referrer_all.tearDown()

    @pytest.mark.jobs
    def TestCase_01_Get_Data_Baseline_Referrer_All(self):
        self.get_data_baseline_referrer_all.get_all_referrer_data()
