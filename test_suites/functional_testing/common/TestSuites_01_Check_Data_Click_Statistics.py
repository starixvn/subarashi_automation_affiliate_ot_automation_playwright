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

# Add based on your function you define
from src.actions.common.compare_data.compare_data_click_statictis import CompareDataClickStatistics

class TestSuites_01_Check_Data_Click_Statistics(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.check_data_click_statistics = CompareDataClickStatistics()
        self.check_data_click_statistics.setup()
        self.utils = self.check_data_click_statistics.utils

    @classmethod
    def tearDownClass(self):
        self.check_data_click_statistics.tearDown()

    def TestCase_01_Check_Data_Referrers_In_Customer(self):
        self.check_data_click_statistics.check_data_referrers_in_customer(inspect.currentframe().f_code.co_name)

