import time
from src.actions.common.action_common import Common
from src.interfaces.user.functional.statistics.referrers_statistics.referrers_filter_elements import ReferrersFilterElements as elm_filter
from src.interfaces.user.functional.statistics.referrers_statistics.referrers_statistics_table_elements import ReferrersStatisticsTableElements as elm_table
from src.interfaces.user.functional.statistics.referrers_statistics.referrers_detail_table_elements import ReferrersDetailTableElements as elm_detail
from src.interfaces.user.ui.menu_list.menu_list import MenuList as elm_menu
from src.utils.services.utils import utilities

class GetDataReferrers(Common):
    
    def __init__(self, utils: utilities):
        super().__init__()
        self.utils = utils
    
    def get_data_referrers_user_site(self, from_date=None, to_date=None, device_type="All", get_detail=True):
        try:
            self.navigate_to_referrers_page()
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
                "site_urls_data": [],
                "website_urls_data": {},
                "has_data": True
            }
            
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
                
                site_url = self.utils.page.new_pages.get_text(f"{row_selector}/td[1]")
                total_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[2]")
                unique_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[3]")
                signups = self.utils.page.new_pages.get_text(f"{row_selector}/td[4]")
                fdm = self.utils.page.new_pages.get_text(f"{row_selector}/td[5]")
                
                site_data = {
                    "site_url": site_url,
                    "total_click": total_click,
                    "unique_click": unique_click,
                    "signups": signups,
                    "fdm": fdm
                }
                result["site_urls_data"].append(site_data)
                
                if get_detail and site_url and site_url.lower() != "none":
                    detail_link = f"{row_selector}/td[1]/a[@class='statisticsItem']"
                    if self.utils.page.new_pages.does_element_exist(detail_link):
                        try:
                            self.utils.page.new_pages.click(detail_link)
                            time.sleep(2)
                            
                            if self.utils.page.new_pages.does_element_exist(elm_detail.div_statistics_detail_table):
                                self.utils.page.new_pages.wait_for_element_ready(elm_detail.div_statistics_detail_table, visible=True, enabled=True, timeout=10)
                                
                                website_urls = []
                                detail_rows = self.utils.page.new_pages.count_element("", f"{elm_detail.tr_detail_rows}")
                                
                                for j in range(1, detail_rows + 1):
                                    detail_row_selector = f"{elm_detail.tbody_detail}/tr[{j}]"
                                    
                                    website_url = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[1]")
                                    total_clicks = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[2]")
                                    unique_clicks = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[3]")
                                    sign_up = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[4]")
                                    url_fdm = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[5]")
                                    
                                    url_data = {
                                        "website_url": website_url,
                                        "total_clicks": total_clicks,
                                        "unique_clicks": unique_clicks,
                                        "sign_up": sign_up,
                                        "fdm": url_fdm
                                    }
                                    website_urls.append(url_data)
                                
                                result["website_urls_data"][site_url] = website_urls
                            
                            self.utils.page.new_pages.go_back()
                            time.sleep(2)
                            
                        except Exception as detail_error:
                            print(f"Warning: Cannot get detail for site {site_url}: {str(detail_error)}")
                            if "back" in str(detail_error).lower() or "navigate" in str(detail_error).lower():
                                try:
                                    self.utils.page.new_pages.go_back()
                                    time.sleep(2)
                                except:
                                    pass
            
            return result
            
        except Exception as e:
            return {
                "site_urls_data": [],
                "website_urls_data": {},
                "has_data": False,
                "error": str(e)
            }
    
    def navigate_to_referrers_page(self):
        try:
            self.utils.page.new_pages.hover(elm_menu.lnk_statistics)
            self.utils.page.new_pages.click(elm_menu.lnk_referrers)          
            self.utils.page.new_pages.wait_for_element_ready(elm_filter.form_filter, visible=True, enabled=True, timeout=15)
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