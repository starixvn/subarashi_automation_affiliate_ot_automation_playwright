import time
from src.actions.common.action_common import Common
from src.interfaces.user.functional.statistics.landing_pages_statistics.landing_pages_filter_elements import LandingPagesFilterElements as elm_filter
from src.interfaces.user.functional.statistics.landing_pages_statistics.landing_pages_statistics_table_elements import LandingPagesStatisticsTableElements as elm_table
from src.interfaces.user.ui.menu_list.menu_list import MenuList as elm_menu
from src.utils.services.utils import utilities

class GetDataLandingPages(Common):
    
    def __init__(self, utils: utilities):
        super().__init__()
        self.utils = utils
    
    def get_data_landing_pages_user_site(self, from_date=None, to_date=None, device_type="All", get_detail=False):
        try:
            self.navigate_to_landing_pages_page()
            self.utils.page.new_pages.wait_for_element_ready(elm_filter.button_submit, visible=True, enabled=True, timeout=15)
            super().select_date_picker_user_site(elm_filter.input_from_date, from_date)
            super().select_date_picker_user_site(elm_filter.input_to_date, to_date)
            
            device_value_mapping = {
                "All": "-1",
                "PC / Laptop": "0", 
                "Mobile": "1"
            }
            device_value = device_value_mapping.get(device_type, "-1")
            super().select_option_user_site(elm_filter.select_device, device_value)
            
            self.utils.page.new_pages.click(elm_filter.button_submit)
            self.utils.page.new_pages.wait_load_page()
            time.sleep(3)
            
            result = {
                "pages_data": [],
                "has_data": True
            }
            
            if get_detail:
                result["website_urls_data"] = {}
            
            no_data_elements = self.utils.page.new_pages.count_element("", "//*[contains(text(), 'No data') or contains(text(), 'There is no information') or contains(text(), 'No records found')]")
            if no_data_elements > 0:
                result["has_data"] = False
                return result
            
            if not self.utils.page.new_pages.does_element_exist(elm_table.tbody):
                result["has_data"] = False
                return result
            
            self.utils.page.new_pages.wait_for_element_ready(elm_table.tbody, visible=True, enabled=True)
            
            number_of_rows = self.utils.page.new_pages.count_element("", f"{elm_table.tr_rows}")
            
            if number_of_rows == 0:
                result["has_data"] = False
                return result
            
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_table.tbody}/tr[{i}]"
                
                page_name = self.utils.page.new_pages.get_text(f"{row_selector}/td[1]")
                language = self.utils.page.new_pages.get_text(f"{row_selector}/td[2]")
                total_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[3]")
                unique_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[4]")
                signups = self.utils.page.new_pages.get_text(f"{row_selector}/td[5]")
                fdm = self.utils.page.new_pages.get_text(f"{row_selector}/td[6]")
                
                page_data = {
                    "page_name": page_name,
                    "language": language,
                    "total_click": total_click,
                    "unique_click": unique_click,
                    "signups": signups,
                    "fdm": fdm
                }
                result["pages_data"].append(page_data)
                
                if get_detail and page_name.lower() != "none" and page_name.strip():
                    try:
                        page_key = f"{page_name} - {language}"
                        page_link_selector = f"{row_selector}/td[1]/a"
                        
                        if self.utils.page.new_pages.does_element_exist(page_link_selector):
                            self.utils.page.new_pages.click(page_link_selector)
                            time.sleep(2)
                            
                            website_urls_data = self._extract_website_urls_data()
                            result["website_urls_data"][page_key] = website_urls_data
                            
                            self.utils.page.new_pages.go_back()
                            time.sleep(2)
                        else:
                            result["website_urls_data"][page_key] = []
                    except Exception as e:
                        result["website_urls_data"][page_key] = []
            
            return result
            
        except Exception as e:
            return {
                "pages_data": [],
                "has_data": False,
                "error": str(e)
            }
    
    def _extract_website_urls_data(self):
        website_urls_data = []
        try:
            if not self.utils.page.new_pages.does_element_exist(elm_table.tbody):
                return website_urls_data
            
            number_of_rows = self.utils.page.new_pages.count_element("", f"{elm_table.tr_rows}")
            
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_table.tbody}/tr[{i}]"
                
                website_url = self.utils.page.new_pages.get_text(f"{row_selector}/td[1]")
                total_clicks = self.utils.page.new_pages.get_text(f"{row_selector}/td[2]")
                unique_clicks = self.utils.page.new_pages.get_text(f"{row_selector}/td[3]")
                signups = self.utils.page.new_pages.get_text(f"{row_selector}/td[4]")
                fdm = self.utils.page.new_pages.get_text(f"{row_selector}/td[5]")
                
                website_data = {
                    "website_url": website_url,
                    "total_clicks": self.parse_int(total_clicks),
                    "unique_clicks": self.parse_int(unique_clicks),
                    "signups": self.parse_int(signups),
                    "fdm": self.parse_int(fdm)
                }
                website_urls_data.append(website_data)
                
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
            
        return website_urls_data
    
    def navigate_to_landing_pages_page(self):
        try:
            self.utils.page.new_pages.hover(elm_menu.lnk_statistics)
            self.utils.page.new_pages.click(elm_menu.lnk_landing_pages)
            self.utils.page.new_pages.wait_for_element_ready(elm_filter.input_from_date, visible=True, enabled=True, timeout=15)
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def parse_int(self, value):
        try:
            if isinstance(value, str):
                cleaned = value.replace(',', '').replace(' ', '').strip()
                if cleaned == '' or cleaned == '-' or cleaned.lower() == 'n/a':
                    return 0
                return int(cleaned)
            return int(value) if value else 0
        except (ValueError, TypeError):
            return 0 