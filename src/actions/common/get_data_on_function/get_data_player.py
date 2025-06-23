import time
import re

from src.utils.services.utils import utilities
from config.constants.settings import *
from src.actions.common.action_common import Common
from src.interfaces.admin.player.player_elements import PlayerElements as elm_player
from src.test_data.admin.customer.player import PLAYER_API, PLAYER_HEADERS, PLAYER_REQUEST_TEMPLATE

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

    def get_data_player_via_api(self, affiliate_name="", username="", system_name="", include_removed_players=False):
        try:
            if not hasattr(self, 'utils') or not hasattr(self.utils, 'api'):
                self.utils.page.extract_TestCaseFailed("API client not initialized. Please ensure login_admin() was called first.")
            
            current_url = self.utils.page.get_current_url()
            base_url = re.match(r'(https?://[^/]+)', current_url).group(1)
            api_url = f"{base_url}{PLAYER_API}"
            
            csrf_token = self._get_csrf_token()
            headers = PLAYER_HEADERS.copy()
            headers["X-Requested-With"] = "XMLHttpRequest"
            if csrf_token:
                headers["__RequestVerificationToken"] = csrf_token
            
            request_body = PLAYER_REQUEST_TEMPLATE.copy()
            request_body.update({
                "AffName": affiliate_name,
                "UserName": username,
                "IbcUserName": system_name,
                "IsIncludeRemovedPlayer": include_removed_players,
                "PageIndex": 1,
                "PageSize": 100
            })
            
            response = self.utils.api.post(
                url=api_url,
                data=request_body,
                header=headers
            )
            
            if response.status != 200:
                self.utils.page.extract_TestCaseFailed(f"API request failed with status code: {response.status}")
            
            response_data = self.utils.api.extract_response_json(response)
            
            result = {
                "players_data": [],
                "has_data": True
            }
            
            if not response_data or "MainData" not in response_data or not response_data["MainData"]:
                result["has_data"] = False
                return result
            
            for player_item in response_data["MainData"]:
                player_data = {
                    "username": player_item.get("UserName", ""),
                    "system_name": player_item.get("IbcUserName", ""),
                    "first_name": player_item.get("FirstName", ""),
                    "last_name": player_item.get("LastName", ""),
                    "registration_date": player_item.get("RegisteredDate", ""),
                    "affiliate_name": player_item.get("AffUserName", ""),
                    "status": "Active" if not player_item.get("IsRemoved", False) else "Removed",
                    "last_action_date": player_item.get("LastAction", "")
                }
                result["players_data"].append(player_data)
            
            return result
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def _get_csrf_token(self):
        try:
            form_token = self.utils.page.page.evaluate("""
                () => {
                    const tokenInput = document.querySelector('input[name="__RequestVerificationToken"]');
                    if (tokenInput && tokenInput.value) return tokenInput.value;
                    return null;
                }
            """)
            
            return form_token
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(f"Failed to get CSRF token: {str(e)}")
            return None


