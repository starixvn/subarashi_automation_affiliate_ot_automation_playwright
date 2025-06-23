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
from src.actions.common.action_common import Common

class Login_admin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        LoginFunc = Common()
        LoginFunc.setup()
        self.LoginFunc = LoginFunc
        self.utils = LoginFunc.utils

    @classmethod
    def tearDownClass(self):
        self.LoginFunc.tearDown()

    