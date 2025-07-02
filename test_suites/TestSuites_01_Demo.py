# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
import inspect
import pytest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Add based on your function you define
from src.actions.action_demo import ActionDemo
from src.utils.core.decorators import measure_test_execution_time

class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        DemoFunc = ActionDemo()
        DemoFunc.setup()
        self.DemoFunc = DemoFunc
        self.utils = DemoFunc.utils

    @classmethod
    def tearDownClass(self):
        self.DemoFunc.tearDown()
    
    @pytest.mark.demo
    @measure_test_execution_time
    def TestCase_001_Verify_UI_Message_Page(self):
        self.DemoFunc.verify_ui_message_page(inspect.currentframe().f_code.co_name)