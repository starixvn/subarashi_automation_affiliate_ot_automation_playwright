import time
import re
from playwright.sync_api import Page
from src.utils.services.utils import utilities
from config.constants.settings import *
from src.interfaces.admin.authentication.login import LoginElements as elm_login_admin
from src.interfaces.admin.common.menu_elements import MenuElements as elm_menu
from src.interfaces.admin.common.common_elements import CommonElements as elm_common
from src.interfaces.admin.common.header_elements import HeaderElements as elm_header
from src.interfaces.admin.customer.left_panel_elements import LeftPanelElements as elm_left_panel
from src.interfaces.user.ui.header.header_elements import HeaderElements as elm_header

class Common():    
    def __init__(self):
        self.playwright = None

    def referUtils(self, Utils):
        self.utils = Utils
        
    def setup(self):
        self.utils = utilities()
        self.env = self.utils.env
        self.playwright = self.utils.page.page
        self.login_admin()

    def destroy(self):
        self.utils.destroy()
    
    def tearDown(self):
        self.utils.destroy()

    def login_admin(self):
        try:
            PASSWORD = utilities.decrypt(
                ciphertext=ADMIN_12BET_ENCRYPTED_PASSWORD[self.env],
                password=ADMIN_12BET_PASSWORD[self.env],
                salt=ADMIN_12BET_SALT_PASSWORD[self.env]
            )
            self.utils.page.navigate(ADMIN_12BET_URL[self.env])
            self.utils.page.input(elm_login_admin.inp_username, ADMIN_12BET_USERNAME[self.env])
            self.utils.page.input(elm_login_admin.inp_password, PASSWORD)
            self.utils.page.click(elm_login_admin.btn_login)
            self.utils.page.verify_element_exist(elm_menu.nav_menu_list)
            time.sleep(3)
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def sso_login(self, affiliatename):
        try:
            super().selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, affiliatename)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_for_element_ready(elm_left_panel.div_affiliate_label, visible=True, enabled=True)
            time.sleep(2)
            self.utils.page.open_new_page_by_click(elm_left_panel.lnk_affiliate)
            self.utils.page.new_pages.wait_for_element_ready(elm_header.a_my_account, visible=True, enabled=True)
            username_text = re.sub(r'\b([A-Z0-9]{10,})\b', self.utils.page.get_text(elm_header.a_my_account)).group(1)
            self.utils.should_be_equal(username_text, affiliatename)

        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def close_page_new_page(self):
        try:
            self.utils.page.new_pages.close_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def selectMenu(self, mainMenu):
        try:
            self.utils.page.click("//a[@id='"+ mainMenu +"']")
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_date_picker(self, element, date_value='05-16-2025'):
        try:
            month = date_value.split("-")[0]
            day = date_value.split("-")[1]
            year = date_value.split("-")[2]
            
            self.utils.page.click(element)
            self.utils.page.wait_for_element_ready(element, visible=True, enabled=True)
            time.sleep(1)
            
            year_selector = f"{element}//div[contains(@class, 'rdr-DateRange')]//span[contains(@class, 'rdr-MonthAndYear-year')]//select"
            self.utils.page.select_options(year_selector, year)
            time.sleep(1)
            month_selector = f"{element}//div[contains(@class, 'rdr-DateRange')]//span[contains(@class, 'rdr-MonthAndYear-month')]//select"
            month_index = int(month) - 1
            self.utils.page.select_options(month_selector, str(month_index))
            time.sleep(1)
            day_selector = f"{element}//div[contains(@class, 'rdr-Days')]//span[contains(@class, 'rdr-Day') and not(contains(@class, 'is-passive')) and text()='{int(day)}']"
            self.utils.page.click(day_selector)
            self.utils.page.wait_load_page()
            time.sleep(1)
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_month_picker(self, element, month_year='05-2025'):
        try:
            month = month_year.split("-")[0]
            year = month_year.split("-")[1]
            self.utils.page.wait_for_element_ready(element, visible=True, enabled=True)
            self.utils.page.click(element)
            self.utils.page.wait_for_element_ready("//select[contains(@class, 'mp-select-year')]", visible=True, enabled=True)
            self.utils.page.wait_load_page()
            
            year_selector = "//select[contains(@class, 'mp-select-year')]"
            self.utils.page.select_options(year_selector, year)
            
            month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month_name = month_names[int(month) - 1]
            
            month_button = f"//button[contains(@class, 'mp-btn-month') and text()='{month_name}']"
            self.utils.page.wait_for_element_ready(month_button, visible=True, enabled=True)
            self.utils.page.click(month_button)
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_multiple_option(self, container_element, options_list):
        try:
            dropdown_button = f"{container_element} button.multiple-select-label"
            self.utils.page.click(dropdown_button)
            self.utils.page.wait_load_page()
            
            if len(options_list) > 0 and "All" not in options_list:
                all_checkbox = f"{container_element} .multiple-select-option-all input.option-checkbox"
                if self.utils.page.get_attribute(all_checkbox, "checked"):
                    self.utils.page.click(all_checkbox)
                    time.sleep(0.5)
            
            for option in options_list:
                if option == "All":
                    checkbox_element = f"{container_element} .multiple-select-option-all input.option-checkbox"
                else:
                    checkbox_element = f"//div[contains(@class, 'multiple-select-container')]//li[contains(@class, 'multiple-select-item')][.//span[contains(text(), '{option}')]]//input[@type='checkbox']"
                
                self.utils.page.click(checkbox_element)
                time.sleep(0.5)
            
            self.utils.page.press_key("Escape")
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_option(self, dropdown_element, option_value):
        try:
            try:
                self.utils.page.select_options(dropdown_element, option_value)
            except Exception:
                self.utils.page.click(dropdown_element)
                self.utils.page.wait_load_page()
                
                option_element = f"//select[@id='{dropdown_element.replace('#', '')}' or @name='{dropdown_element.replace('#', '')}']//option[text()='{option_value}' or @value='{option_value}']"
                self.utils.page.click(option_element)
            
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def go_to_next_page(self, pagination_container=".page-container"):
        try:
            next_button = f"{pagination_container} a.page-next:not(.disable)"
            if self.utils.page.does_element_exist(next_button):
                self.utils.page.click(next_button)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False

    def go_to_prev_page(self, pagination_container=".page-container"):
        try:
            prev_button = f"{pagination_container} a.page-prev:not(.disable)"
            if self.utils.page.does_element_exist(prev_button):
                self.utils.page.click(prev_button)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False

    def go_to_last_page(self, pagination_container=".page-container"):
        try:
            last_button = f"{pagination_container} a.page-last:not(.disable)"
            if self.utils.page.does_element_exist(last_button):
                self.utils.page.click(last_button)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False

    def go_to_first_page(self, pagination_container=".page-container"):
        try:
            first_button = f"{pagination_container} a.page-first:not(.disable)"
            if self.utils.page.does_element_exist(first_button):
                self.utils.page.click(first_button)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False
    
    def go_to_specific_page(self, pagination_container=".page-container", page_number=1):
        try:
            page_input = f"{pagination_container} input.page-form"
            if self.utils.page.does_element_exist(page_input):
                self.utils.page.input(page_input, str(page_number))
                self.utils.page.press_key("Enter", page_input)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False
    
    def set_page_size(self, pagination_container=".page-container", size="20"):
        try:
            page_size_select = f"{pagination_container} select.pagesize-select"
            if self.utils.page.does_element_exist(page_size_select):
                self.utils.page.select_options(page_size_select, size)
                self.utils.page.wait_load_page()
                return True
            return False
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            return False

    def logout_admin(self):
        try:
            self.utils.page.click(elm_header.lnk_logout)
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)