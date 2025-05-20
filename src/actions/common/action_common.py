from src.utils.services.utils import utilities
from config.constants.settings import *
import time
from playwright.sync_api import Page

from src.interfaces.admin.authentication.login import LoginElements as elm_login_admin
from src.interfaces.admin.common.menu_elements import MenuElements as elm_menu
from src.interfaces.admin.common.common_elements import CommonElements as elm_common
from src.interfaces.admin.common.header_elements import HeaderElements as elm_header

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
                ciphertext=ADMIN_12BET_ENCRYPTED_PASSWORD,
                password=ADMIN_12BET_PASSWORD,
                salt=ADMIN_12BET_SALT_PASSWORD
            )
            self.utils.page.navigate(ADMIN_12BET_URL[self.env])
            self.utils.page.input(elm_login_admin.inp_username, ADMIN_12BET_USERNAME)
            self.utils.page.input(elm_login_admin.inp_password, PASSWORD)
            self.utils.page.click(elm_login_admin.btn_login)
            self.utils.page.verify_element_exist(elm_menu.nav_menu_list)
            time.sleep(3)
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def selectMenu(self, mainMenu):
        try:
            self.utils.page.click("//a[@id='"+ mainMenu +"']")
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_date_picker(self, element, date_value='05-16-2025'):
        """
        Select a date using the date picker component
        Format: month-day-year (e.g., '05-16-2025')
        
        Example element: div.daterange-container input.datepicker
        """
        try:
            month = date_value.split("-")[0]
            day = date_value.split("-")[1]
            year = date_value.split("-")[2]
            
            # Click the input field to open the date picker
            self.utils.page.click(element)
            self.utils.page.wait_load_page()
            
            # Select year from the dropdown
            year_selector = f"{element}//div[contains(@class, 'rdr-DateRange')]//span[contains(@class, 'rdr-MonthAndYear-year')]//select"
            self.utils.page.select_options(year_selector, year)
            
            # Select month from the dropdown
            month_selector = f"{element}//div[contains(@class, 'rdr-DateRange')]//span[contains(@class, 'rdr-MonthAndYear-month')]//select"
            month_index = int(month) - 1
            self.utils.page.select_options(month_selector, str(month_index))
            
            # Select the day
            day_selector = f"{element}//div[contains(@class, 'rdr-Days')]//span[contains(@class, 'rdr-Day') and not(contains(@class, 'is-passive')) and text()='{int(day)}']"
            self.utils.page.click(day_selector)
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_month_picker(self, element, month_year='05-2025'):
        """
        Select a month using the month picker component
        Format: month-year (e.g., '05-2025')
        
        Examples: 
        - <div class="mp-form-container">
        - <div class="position-relative d-inline-block">
        """
        try:
            month = month_year.split("-")[0]
            year = month_year.split("-")[1]
            
            # Click the element to open the month picker
            self.utils.page.click(element)
            self.utils.page.wait_load_page()
            
            # Select year from dropdown
            year_selector = "//select[contains(@class, 'mp-select-year')]"
            self.utils.page.select_options(year_selector, year)
            
            # Map month index (1-12) to name and select the month button
            month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
            month_name = month_names[int(month) - 1]
            
            # Click the month button
            month_button = f"//button[contains(@class, 'mp-btn-month') and text()='{month_name}']"
            self.utils.page.click(month_button)
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_multiple_option(self, container_element, options_list):
        """
        Select multiple options from a multi-select dropdown
        
        Example element: div.multiple-select-container
        """
        try:
            # Click on the container to open the dropdown
            dropdown_button = f"{container_element} button.multiple-select-label"
            self.utils.page.click(dropdown_button)
            self.utils.page.wait_load_page()
            
            # First, uncheck "All" if we're selecting specific options
            if len(options_list) > 0 and "All" not in options_list:
                all_checkbox = f"{container_element} .multiple-select-option-all input.option-checkbox"
                if self.utils.page.get_attribute(all_checkbox, "checked"):
                    self.utils.page.click(all_checkbox)
                    time.sleep(0.5)
            
            # Select or deselect options
            for option in options_list:
                if option == "All":
                    checkbox_element = f"{container_element} .multiple-select-option-all input.option-checkbox"
                else:
                    # Use XPath to find the correct option
                    checkbox_element = f"//div[contains(@class, 'multiple-select-container')]//li[contains(@class, 'multiple-select-item')][.//span[contains(text(), '{option}')]]//input[@type='checkbox']"
                
                self.utils.page.click(checkbox_element)
                time.sleep(0.5)
            
            # Click outside to close the dropdown
            self.utils.page.press_key("Escape")
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def select_option(self, dropdown_element, option_value):
        """
        Select an option from a dropdown select element
        
        Example: select#BaseCurrency
        """
        try:
            # Use select_options method directly if possible
            try:
                self.utils.page.select_options(dropdown_element, option_value)
            except Exception:
                # Fallback to click method
                self.utils.page.click(dropdown_element)
                self.utils.page.wait_load_page()
                
                # Try to find the option by text or value
                option_element = f"//select[@id='{dropdown_element.replace('#', '')}' or @name='{dropdown_element.replace('#', '')}']//option[text()='{option_value}' or @value='{option_value}']"
                self.utils.page.click(option_element)
            
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def go_to_next_page(self, pagination_container=".page-container"):
        """
        Navigate to the next page using pagination controls
        
        Example element: div.page-container
        """
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
        """
        Navigate to the previous page using pagination controls
        
        Example element: div.page-container
        """
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
        """
        Navigate to the last page using pagination controls
        
        Example element: div.page-container
        """
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
        """
        Navigate to the first page using pagination controls
        
        Example element: div.page-container
        """
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
        """
        Navigate to a specific page by entering the page number
        
        Example element: div.page-container
        """
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
        """
        Set the number of items to display per page
        
        Example element: div.page-container
        """
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