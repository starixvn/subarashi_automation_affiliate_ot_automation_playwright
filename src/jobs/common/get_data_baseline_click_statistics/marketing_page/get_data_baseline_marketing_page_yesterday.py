import os
import pytz
import json
import random
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer
from config.constants.settings import *
class GetDataBaselineMarketingPageYesterday(GetDataCustomer):

    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_marketing_pages")
        self.timezone = pytz.timezone('Asia/Singapore')

    def get_data_marketing_page_yesterday(self):
        try:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
            if ENVIRONMENT == "local":
                username = "12BETAFF001"
            else:
                top_100_data_player = self.data_player.get_top_100_data_player()
                username = top_100_data_player["players_data"][random.randint(0, len(top_100_data_player["players_data"]) - 1)]["affiliate_name"]
            language = "All"
            include_inactive_tracking = False
            
            today = datetime.now(self.timezone)
            yesterday = today - timedelta(days=1)
            date_str = yesterday.strftime("%m-%d-%Y")
            
            from_date = date_str
            to_date = date_str

            raw_data = super().get_data_marketing_pages_in_customer(username, language, from_date, to_date, include_inactive_tracking)
            
            collected_data = {
                "metadata": {
                    "collected_at": datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z"),
                    "period": {
                        "from_date": from_date,
                        "to_date": to_date
                    },
                    "filters": {
                        "username": username,
                        "language": language,
                        "include_inactive_tracking": include_inactive_tracking
                    },
                    "has_data": True
                },
                "channels_data": {},
                "channel_details_data": {}
            }
            
            if not raw_data.get("has_data", True):
                collected_data["metadata"]["has_data"] = False
                self._save_data(collected_data)
                return collected_data
            
            for channel_data in raw_data["channels_data"]:
                channel_name = channel_data["channel_name"]
                language = channel_data["language"]
                key = f"{channel_name}"
                
                collected_data["channels_data"][key] = {
                    "channel_name": channel_name,
                    "language": language,
                    "total_clicks": self._parse_int(channel_data["total_click"]),
                    "unique_clicks": self._parse_int(channel_data["unique_click"]),
                    "signups": self._parse_int(channel_data["signups"]),
                    "fdm": self._parse_int(channel_data["fdm"])
                }
            
            collected_data["channel_details_data"] = {}
            for channel_key, details_data in raw_data["channel_details_data"].items():
                channel_name = channel_key.split(" - ")[0] if " - " in channel_key else channel_key
                collected_data["channel_details_data"][channel_key] = []
                for detail_data in details_data:
                    collected_data["channel_details_data"][channel_key].append({
                        "url": detail_data["url"],
                        "language": detail_data["language"],
                        "total_clicks": self._parse_int(detail_data["total_clicks"]),
                        "unique_clicks": self._parse_int(detail_data["unique_clicks"]),
                        "signups": self._parse_int(detail_data["signups"]),
                        "fdm": self._parse_int(detail_data["fdm"])
                    })
            
            self._save_data(collected_data)
            return collected_data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)

    def _parse_int(self, text):
        """convert string to int"""
        try:
            return int(str(text).replace(',', '').strip() or 0)
        except (ValueError, AttributeError):
            return 0
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
        

    def _save_data(self, data):
        """save data to file"""
        try:
            os.makedirs(self.data_directory, exist_ok=True)
            
            json_str = json.dumps(data, indent=4, ensure_ascii=False)
            python_str = json_str.replace('"has_data": true', '"has_data": True').replace('"has_data": false', '"has_data": False').replace('"include_inactive_tracking": false', '"include_inactive_tracking": False').replace('"include_inactive_tracking": true', '"include_inactive_tracking": True')
            
            py_file = os.path.join(self.data_directory, "data_marketing_pages_yesterday.py")
            current_time_gmt8 = datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z")
            with open(py_file, "w", encoding="utf-8") as f:
                f.write(f"# get data baseline marketing page yesterday at {current_time_gmt8} (GMT+8)\n\n")
                f.write(f"class DataMarketingPagesYesterday:\n")
                f.write(f"    data_marketing_pages_yesterday = ")
                f.write(python_str)
                f.write("\n")
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)





