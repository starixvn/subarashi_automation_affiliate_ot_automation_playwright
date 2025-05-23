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

from src.jobs.common.get_data_baseline_click_statistics.referrers.get_data_baseline_referrers_last_month import GetDataBaselineReferrersLastMonth

class TestSuites_03_Get_Data_Baseline_Referrers_Last_Month(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_referrers_last_month = GetDataBaselineReferrersLastMonth()
        self.get_data_baseline_referrers_last_month.setup()
        self.utils = self.get_data_baseline_referrers_last_month.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_referrers_last_month.tearDown()

    def TestCase_01_Get_Data_Baseline_Referrers_Last_Month(self):
        self.get_data_baseline_referrers_last_month.get_data_referrers_last_month()

