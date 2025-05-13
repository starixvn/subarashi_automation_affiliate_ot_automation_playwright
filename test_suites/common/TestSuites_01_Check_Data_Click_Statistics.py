# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Add based on your function you define
from actions.common.action_common import Common
from actions.common.action_compare_data_click_statistics import CompareDataClickStatistics

class TestSuites_01_Check_Data_Click_Statistics(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        CheckDataClickStatistics = CompareDataClickStatistics()
        CheckDataClickStatistics.setup()
        self.CheckDataClickStatistics = CheckDataClickStatistics
        self.utils = CheckDataClickStatistics.utils

    @classmethod
    def tearDownClass(self):
        self.CheckDataClickStatistics.tearDown()

    def TestCase_01_Check_Data_Click_Statistics(self):
        self.CheckDataClickStatistics.get_data_referrers_in_customer()

