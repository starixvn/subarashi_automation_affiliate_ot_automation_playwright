import time

from src.utils.services.utils import utilities
from config.constants.settings import *
from src.actions.common.action_common import Common
from src.interfaces.admin.player.player_elements import PlayerElements as elm_player

class GetDataPlayer(Common):

    def get_top_100_data_player(self, affiliate_name="", username="", system_name="", include_removed_players=False):
        try:
            super().selectMenu("Player")
            time.sleep(3)
            
            if affiliate_name:
                self.utils.page.input(elm_player.inp_affiliate, affiliate_name)
                
            if username:
                self.utils.page.input(elm_player.inp_username, username)
            
            if system_name:
                self.utils.page.input(elm_player.inp_system_name, system_name)
            
            if include_removed_players:
                self.utils.page.click(elm_player.chk_include_removed_players)
                
            self.utils.page.click(elm_player.btn_search)
            self.utils.page.wait_load_page()
            
            time.sleep(3)
            
            self.utils.page.select_options(elm_player.sel_page_size, "100")
            self.utils.page.wait_load_page()
            
            time.sleep(3)

            result = {
                "players_data": [],
                "has_data": True
            }
            
            no_data_message = self.utils.page.count_element("", f"//*[contains(text(), 'There is no information available')]")
            if no_data_message > 0:
                result["has_data"] = False
                return result
            
            number_of_rows = self.utils.page.count_element("", f"{elm_player.div_table_container}//tbody/tr[not(contains(@class, 'first-row'))]")
            for i in range(1, number_of_rows + 1):
                row_selector = f"{elm_player.div_table_container}//tbody/tr[not(contains(@class, 'first-row'))][{i}]"
                username = self.utils.page.get_text(f"{row_selector}//td[2]")
                system_name = self.utils.page.get_text(f"{row_selector}//td[3]")
                first_name = self.utils.page.get_text(f"{row_selector}//td[4]")
                last_name = self.utils.page.get_text(f"{row_selector}//td[5]")
                registration_date = self.utils.page.get_text(f"{row_selector}//td[6]")
                affiliate_name = self.utils.page.get_text(f"{row_selector}//td[7]")
                status = self.utils.page.get_text(f"{row_selector}//td[8]")
                last_action_date = self.utils.page.get_text(f"{row_selector}//td[9]")
                
                player_data = {
                    "username": username,
                    "system_name": system_name,
                    "first_name": first_name,
                    "last_name": last_name,
                    "registration_date": registration_date,
                    "affiliate_name": affiliate_name,
                    "status": status,
                    "last_action_date": last_action_date
                }
                result["players_data"].append(player_data)
                    
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)


