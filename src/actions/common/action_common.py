import time
import re
from datetime import datetime, timedelta
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
    
    # Common parsing methods
    @staticmethod
    def parse_int(text):
        """Parse text to integer, handling various edge cases"""
        try:
            if text is None:
                return 0
            text_str = str(text).replace(',', '').strip().lower()
            if text_str in ['', 'none', '-', 'null', 'n/a', 'na']:
                return 0
            return int(text_str)
        except (ValueError, TypeError):
            return 0
    
    @staticmethod
    def parse_fraction(text):
        """Parse fraction text like '10/20' into dict with unique and total"""
        try:
            if '/' in str(text):
                parts = str(text).split('/')
                return {
                    "unique": Common.parse_int(parts[0]),
                    "total": Common.parse_int(parts[1]) if len(parts) > 1 else 0
                }
            return {"unique": 0, "total": 0}
        except Exception:
            return {"unique": 0, "total": 0}
    
    # Date utility methods
    @staticmethod
    def get_date_range(period):
        """Get date range for given period (last_month, last_week, yesterday)"""
        today = datetime.now()
        
        if period == "last_month":
            first_day_current_month = today.replace(day=1)
            last_day_previous_month = first_day_current_month - timedelta(days=1)
            first_day_previous_month = last_day_previous_month.replace(day=1)
            from_date = first_day_previous_month.strftime("%m-%d-%Y")
            to_date = last_day_previous_month.strftime("%m-%d-%Y")
            month_date = last_day_previous_month.strftime("%m-%Y")
        elif period == "last_week":
            to_date = (today - timedelta(days=today.weekday() + 1)).strftime("%m-%d-%Y")
            from_date = (today - timedelta(days=today.weekday() + 7)).strftime("%m-%d-%Y")
            month_date = today.strftime("%m-%Y")
        elif period == "yesterday":
            yesterday = today - timedelta(days=1)
            from_date = yesterday.strftime("%m-%d-%Y")
            to_date = yesterday.strftime("%m-%d-%Y")
            month_date = yesterday.strftime("%m-%Y")
        else:
            raise ValueError(f"Unknown period: {period}")

        return {
            "from_date": from_date,
            "to_date": to_date,
            "month_date": month_date
        }
    
    # Username utility methods
    @staticmethod
    def get_username():
        """Get username based on environment"""
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer
            data_player = GetDataPlayer()
            # Note: utils needs to be passed in actual implementation
            player_data_api = data_player.get_data_player_via_api()
            return player_data_api["players_data"][0]["affiliate_name"]
    
    @staticmethod
    def get_username_for_period_device(period, device_type, data_dict, fallback_username):
        """Get username for specific period and device type from data dictionary"""
        period_mappings = {
            "marketing_pages": {
                "last_month": {"All": "Marketing_Pages_Last_Month"},
                "last_week": {"All": "Marketing_Pages_Last_Week"},
                "yesterday": {"All": "Marketing_Pages_Yesterday"}
            },
            "landing_pages": {
                "last_month": {"All": "Landing_Pages_Last_Month", "PC / Laptop": "Landing_Pages_Last_Month_By_Desktop", "Mobile": "Landing_Pages_Last_Month_By_Mobile"},
                "last_week": {"All": "Landing_Pages_Last_Week", "PC / Laptop": "Landing_Pages_Last_Week_By_Desktop", "Mobile": "Landing_Pages_Last_Week_By_Mobile"},
                "yesterday": {"All": "Landing_Pages_Yesterday", "PC / Laptop": "Landing_Pages_Yesterday_By_Desktop", "Mobile": "Landing_Pages_Yesterday_By_Mobile"}
            },
            "referrers": {
                "last_month": {"All": "Referres_Last_Month", "PC / Laptop": "Referres_Last_Month_By_Desktop", "Mobile": "Referres_Last_Month_By_Mobile"},
                "last_week": {"All": "Referres_Last_Week", "PC / Laptop": "Referres_Last_Week_By_Desktop", "Mobile": "Referres_Last_Week_By_Mobile"},
                "yesterday": {"All": "Referres_Yesterday", "PC / Laptop": "Referres_Yesterday_By_Desktop", "Mobile": "Referres_Yesterday_By_Mobile"}
            }
        }
        
        # Auto-detect data type based on available keys in data_dict
        data_type = None
        for dt, mapping in period_mappings.items():
            if period in mapping and device_type in mapping[period]:
                key = mapping[period][device_type]
                if key in data_dict and data_dict[key]:
                    data_type = dt
                    break
        
        if data_type and period in period_mappings[data_type] and device_type in period_mappings[data_type][period]:
            baseline_key = period_mappings[data_type][period][device_type]
            if baseline_key in data_dict and data_dict[baseline_key]:
                return data_dict[baseline_key]["metadata"]["filters"]["username"]
        
        return fallback_username
    
    # Website URLs consolidation (common in landing_pages and referrers)
    @staticmethod
    def consolidate_website_urls_data(website_urls_data):
        """
        Consolidate duplicate website URLs by summing their metrics.
        Input: {key: [website_data_list]}
        Output: ({key: [consolidated_website_data_list]}, consolidation_stats)
        """
        consolidated_data = {}
        consolidation_stats = {
            "total_original_websites": 0,
            "total_consolidated_websites": 0,
            "pages_with_duplicates": 0,
            "duplicate_urls_found": []
        }
        
        for key, website_list in website_urls_data.items():
            if not isinstance(website_list, list):
                consolidated_data[key] = website_list
                continue
                
            original_count = len(website_list)
            consolidation_stats["total_original_websites"] += original_count
            
            url_groups = {}
            for website_data in website_list:
                url = website_data.get("website_url", "")
                if url not in url_groups:
                    url_groups[url] = []
                url_groups[url].append(website_data)
            
            page_has_duplicates = False
            for url, group in url_groups.items():
                if len(group) > 1:
                    page_has_duplicates = True
                    consolidation_stats["duplicate_urls_found"].append({
                        "page": key,
                        "url": url,
                        "duplicate_count": len(group)
                    })
            
            if page_has_duplicates:
                consolidation_stats["pages_with_duplicates"] += 1
            
            consolidated_websites = []
            for url, group in url_groups.items():
                if len(group) == 1:
                    consolidated_websites.append(group[0])
                else:
                    consolidated_website = {
                        "website_url": url,
                        "total_clicks": 0,
                        "unique_clicks": 0,
                        "signups": 0,
                        "fdm": 0
                    }
                    
                    for website_data in group:
                        consolidated_website["total_clicks"] += Common.parse_int(website_data.get("total_clicks", 0))
                        consolidated_website["unique_clicks"] += Common.parse_int(website_data.get("unique_clicks", 0))
                        
                        signups_value = 0
                        if "signups" in website_data:
                            signups_value = Common.parse_int(website_data["signups"])
                        elif "sign_up" in website_data:
                            signups_value = Common.parse_int(website_data["sign_up"])
                        consolidated_website["signups"] += signups_value
                        
                        consolidated_website["fdm"] += Common.parse_int(website_data.get("fdm", 0))
                    
                    consolidated_websites.append(consolidated_website)
            
            consolidated_data[key] = consolidated_websites
            consolidation_stats["total_consolidated_websites"] += len(consolidated_websites)
        
        return consolidated_data, consolidation_stats
    
    # Test result formatting
    @staticmethod
    def format_test_results(results, device_display_name, data_type="referrers"):
        """Format test results for display in test reports"""
        formatted_result = ""
        formatted_result += f"\n     + Username: {results['username']}"
        formatted_result += f"\n     + Device Type: {results['device_type']}"
        formatted_result += f"\n     + From Date: {results['from_date']}"
        formatted_result += f"\n     + To Date: {results['to_date']}"
        
        if device_display_name == "All":
            formatted_result += f"\n     + Total Clicks: Statistics={results['statistics_total_clicks']}, {data_type.title()}={results.get(f'{data_type}_total_clicks', 'N/A')}"
            if f'statistics_unique_clicks' in results:
                formatted_result += f"\n     + Unique Clicks: Statistics={results['statistics_unique_clicks']}, {data_type.title()}={results.get(f'{data_type}_unique_clicks', 'N/A')}"
        else:
            formatted_result += f"\n     + {device_display_name} Total Clicks: Statistics={results['statistics_total_clicks']}, {data_type.title()}={results.get(f'{data_type}_total_clicks', 'N/A')}"
        
        if 'statistics_signups' in results:
            formatted_result += f"\n     + Signups: Statistics={results['statistics_signups']}, {data_type.title()}={results.get(f'{data_type}_signups', 'N/A')}"
        if 'statistics_fdm' in results:
            formatted_result += f"\n     + FDM: Statistics={results['statistics_fdm']}, {data_type.title()}={results.get(f'{data_type}_fdm', 'N/A')}"
        
        return formatted_result
    
    # Error handling for test cases
    @staticmethod
    def handle_test_case_error(utils, test_case_data, main_checklist, current_index, sub_auto_test_case, sheet_name):
        """Handle test case errors and update remaining checklist items"""
        utils.update_result_to_ggsheet(
            test_case_data["TestCase_spread_sheet_id"], 
            main_checklist[current_index], 
            test_case_data["testcase"], 
            sub_auto_test_case, 
            test_case_data["TestCase_Auto_Status"][1],
            sheet_name=sheet_name
        )
        current_index += 1
        if current_index < len(main_checklist):
            for i in range(current_index, len(main_checklist)):
                if i >= len(main_checklist):
                    break
                utils.update_result_to_ggsheet(
                    test_case_data["TestCase_spread_sheet_id"], 
                    main_checklist[i], 
                    test_case_data["testcase"], 
                    "", 
                    test_case_data["TestCase_Auto_Status"][2],
                    sheet_name=sheet_name
                )
    
    # Language mapping utility
    @staticmethod
    def get_language_mapping():
        """Get standard language mapping dictionary"""
        return {
            "chinese simplified": "zh-cn",
            "english": "en-us",
            "bengali": "bn-in",
            "english (india)": "en-in",
            "indonesian": "id-id",
            "japanese": "ja-jp",
            "korean": "ko-kr",
            "thai": "th-th",
            "vietnamese": "vi-vn",
            "telugu": "te-in"
        }
    
    # Cache management
    @staticmethod
    def clear_cache_for_class(class_ref):
        """Clear cache for any class that has _cache_data and _cache_username"""
        class_ref._cache_data = None
        class_ref._cache_username = None

    def setup(self):
        self.utils = utilities()
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
            self.utils.page.navigate(ADMIN_12BET_URL)
            self.utils.page.input(elm_login_admin.inp_username, ADMIN_12BET_USERNAME)
            self.utils.page.input(elm_login_admin.inp_password, PASSWORD)
            self.utils.page.click(elm_login_admin.btn_login)
            self.utils.page.verify_element_exist(elm_menu.nav_menu_list)
            time.sleep(3)
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def sso_login(self, affiliatename):
        try:
            self.selectMenu("Customer")
            self.utils.page.input(elm_left_panel.inp_aff_name, affiliatename)
            self.utils.page.click(elm_left_panel.btn_search)
            self.utils.page.wait_for_element_ready(elm_left_panel.div_affiliate_label, visible=True, enabled=True)
            self.utils.page.wait_for_element_ready(elm_left_panel.lnk_affiliate, visible=True, enabled=True)
            self.utils.page.open_new_page_by_click(elm_left_panel.lnk_affiliate)
            self.utils.page.new_pages.wait_load_page()
            self.utils.page.new_pages.wait_for_element_ready(elm_header.a_my_account, visible=True, enabled=True)
            text_username = self.utils.page.new_pages.get_text(elm_header.a_my_account)
            match = re.search(r'\b([A-Z0-9]{10,})\b', text_username)
            if match:
                username_text = match.group(1)
            else:
                username_text = None
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

    def select_date_picker_user_site(self, element, date_value='05-16-2025'):
        try:
            month = date_value.split("-")[0]
            day = date_value.split("-")[1]
            year = date_value.split("-")[2]
            
            self.utils.page.new_pages.click(element)
            self.utils.page.new_pages.wait_for_element_ready(element, visible=True, enabled=True)
            time.sleep(1)
            
            year_selector = f"//div[contains(@class, 'pika-single') and not(contains(@class, 'is-hidden'))]//*[@class='pika-select pika-select-year']"
            self.utils.page.new_pages.select_options(year_selector, year)
            time.sleep(1)
            month_selector = f"//div[contains(@class, 'pika-single') and not(contains(@class, 'is-hidden'))]//*[@class='pika-select pika-select-month']"
            month_index = int(month) - 1
            self.utils.page.new_pages.select_options(month_selector, str(month_index))
            time.sleep(1)
            day_selector = f"//div[contains(@class, 'pika-single') and not(contains(@class, 'is-hidden'))]//button[@class='pika-button pika-day'][@data-pika-year='{year}'][@data-pika-month='{month_index}'][@data-pika-day='{int(day)}']"
            self.utils.page.new_pages.click(day_selector)
            self.utils.page.new_pages.wait_load_page()
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
            self.utils.page.select_options(dropdown_element, option_value)
            self.utils.page.wait_load_page()
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def select_option_user_site(self, dropdown_element, option_value):
        try:
            self.utils.page.new_pages.select_options(dropdown_element, option_value)
            self.utils.page.new_pages.wait_load_page()
        except Exception as e:
            self.utils.page.new_pages.extract_TestCaseFailed(e)

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