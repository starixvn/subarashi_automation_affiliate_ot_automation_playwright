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

from src.jobs.common.get_data_baseline_click_statistics.referrers.get_data_baseline_referrers_yesterday_by_mobile import GetDataBaselineReferrersYesterdayByMobile

class TestSuites_05_Get_Data_Baseline_Referrers_Yesterday_By_Mobile(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.get_data_baseline_referrers_yesterday_by_mobile = GetDataBaselineReferrersYesterdayByMobile()
        self.get_data_baseline_referrers_yesterday_by_mobile.setup()
        self.utils = self.get_data_baseline_referrers_yesterday_by_mobile.utils

    @classmethod
    def tearDownClass(self):
        self.get_data_baseline_referrers_yesterday_by_mobile.tearDown()

    def TestCase_01_Get_Data_Baseline_Referrers_Yesterday_By_Mobile(self):
        self.get_data_baseline_referrers_yesterday_by_mobile.get_data_referrers_yesterday_by_mobile()


