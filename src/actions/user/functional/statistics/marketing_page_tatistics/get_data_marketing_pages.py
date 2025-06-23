import time
from src.actions.common.action_common import Common
from src.interfaces.user.functional.statistics.marketing_page_tatistics.marketing_statistics_filter_elements import MarketingStatisticsFilterElements as elm_filter
from src.interfaces.user.functional.statistics.marketing_page_tatistics.marketing_statistics_table_elements import MarketingStatisticsTableElements as elm_table
from src.interfaces.user.ui.menu_list.menu_list import MenuList as elm_menu
from src.utils.services.utils import utilities

class GetDataMarketingPages(Common):
    
    def __init__(self, utils: utilities):
        super().__init__()
        self.utils = utils
    
    def get_data_marketing_pages_user_site(self, from_date=None, to_date=None, get_detail=False):
        try:
            self.navigate_to_marketing_pages_page()
            self.utils.page.new_pages.wait_for_element_ready(elm_filter.form_filter, visible=True, enabled=True, timeout=15)
            super().select_date_picker_user_site(elm_filter.input_from_date, from_date)
            super().select_date_picker_user_site(elm_filter.input_to_date, to_date)
            
            self.utils.page.new_pages.click(elm_filter.button_submit)
            self.utils.page.new_pages.wait_load_page()
            time.sleep(3)
            
            result = {
                "channels_data": [],
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
            
            number_of_rows = self.utils.page.new_pages.count_element("", f"{elm_table.tr_parent_rows}")
            
            if number_of_rows == 0:
                result["has_data"] = False
                return result
            
            for i in range(1, number_of_rows + 1):
                row_selector = f"({elm_table.tr_parent_rows})[{i}]"
                
                channel_name = self.utils.page.new_pages.get_text(f"{row_selector}/td[2]//span[@class='flex-0']")
                language = self.utils.page.new_pages.get_text(f"{row_selector}/td[3]")
                total_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[4]")
                unique_click = self.utils.page.new_pages.get_text(f"{row_selector}/td[5]")
                signups = self.utils.page.new_pages.get_text(f"{row_selector}/td[6]")
                fdm = self.utils.page.new_pages.get_text(f"{row_selector}/td[7]")
                
                channel_data = {
                    "channel_name": channel_name,
                    "language": language,
                    "total_click": total_click,
                    "unique_click": unique_click,
                    "signups": signups,
                    "fdm": fdm
                }
                result["channels_data"].append(channel_data)
            
            if get_detail:
                result["channel_details_data"] = self._extract_channel_details_data()
            
            return result
            
        except Exception as e:
            return {
                "channels_data": [],
                "has_data": False,
                "error": str(e)
            }
    
    def _extract_channel_details_data(self):
        channel_details_data = {}
        
        try:
            number_of_rows = self.utils.page.new_pages.count_element("", f"{elm_table.tr_parent_rows}")
            
            for i in range(1, number_of_rows + 1):
                row_selector = f"({elm_table.tr_parent_rows})[{i}]"
                
                channel_name = self.utils.page.new_pages.get_text(f"{row_selector}/td[2]//span[@class='flex-0']")
                
                toggle_button_selector = f"{row_selector}/td[2]//button[@class='btn btn-transparent']"
                if self.utils.page.new_pages.does_element_exist(toggle_button_selector):
                    self.utils.page.new_pages.click(toggle_button_selector)
                    time.sleep(2)
                    
                    detail_rows = self.utils.page.new_pages.count_element("", f"//table[@class='row-toogleable-table']/tbody/tr[not(@class='parent-item') and position() > {i}]")
                    
                    urls_data = []
                    detail_row_count = 0
                    
                    for j in range(i + 1, number_of_rows + detail_rows + 1):
                        detail_row_selector = f"(//table[@class='row-toogleable-table']/tbody/tr)[{j}]"
                        
                        if self.utils.page.new_pages.does_element_exist(f"{detail_row_selector}[@class='parent-item']"):
                            break
                        
                        url = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[2]")
                        language = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[3]")
                        total_clicks = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[4]")
                        unique_clicks = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[5]")
                        signups = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[6]")
                        fdm = self.utils.page.new_pages.get_text(f"{detail_row_selector}/td[7]")
                        
                        url_data = {
                            "url": url,
                            "language": language,
                            "total_clicks": total_clicks,
                            "unique_clicks": unique_clicks,
                            "signups": signups,
                            "fdm": fdm
                        }
                        urls_data.append(url_data)
                        detail_row_count += 1
                    
                    channel_key = f"{i} - {channel_name}"
                    channel_details_data[channel_key] = urls_data
                    
                    if self.utils.page.new_pages.does_element_exist(toggle_button_selector):
                        self.utils.page.new_pages.click(toggle_button_selector)
                        time.sleep(1)
            
        except Exception as e:
            pass
        
        return channel_details_data
    
    def navigate_to_marketing_pages_page(self):
        try:
            self.utils.page.new_pages.hover(elm_menu.lnk_statistics)
            self.utils.page.new_pages.click(elm_menu.lnk_marketing_pages)
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