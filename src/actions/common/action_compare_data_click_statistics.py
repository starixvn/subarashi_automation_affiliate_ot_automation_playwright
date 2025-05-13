from src.utils.services.utils import utilities
from config.constants.settings import *

from .action_common import Common
from src.interfaces.admin.customer.left_panel_elements import LeftPanelElements as elm_left_panel
from src.interfaces.admin.customer.submenu_elements import SubmenuElements as elm_submenu
from src.interfaces.admin.customer.statistics_elements import StatisticsElements as elm_statistics

class CompareDataClickStatistics(Common):
    def __init__(self):
        self.playwright = None

    def referUtils(self, Utils):
        self.utils = Utils
        
    def setup(self):
        self.utils = utilities()
        self.env = self.utils.env
        self.playwright = self.utils.page.page
        super().login_admin()

    def destroy(self):
        self.utils.destroy()
    
    def tearDown(self):
        self.utils.destroy()

    def get_data_referrers_in_customer(self):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, "12BETAFF001")
            self.utils.page.click(elm_left_panel.btn_search)
            self.playwright.wait_for_load_state("domcontentloaded")
            self.utils.page.click(elm_submenu.click_statistics)
            self.playwright.wait_for_load_state("domcontentloaded")
            self.utils.page
            
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

