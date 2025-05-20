import os
import pytz
import json
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer


class GetDataBaselineMarketingPageLastWeek(GetDataCustomer):

    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_marketing_pages")
        self.timezone = pytz.timezone('Asia/Singapore')

    def get_data_marketing_page_last_week(self):
        username = "12betaff001"
        language = "All"
        include_inactive_tracking = False
        
        today = datetime.now(self.timezone)
        current_weekday = today.weekday()
        days_since_monday = current_weekday
        monday_this_week = today - timedelta(days=days_since_monday)
        monday_this_week = monday_this_week.replace(hour=0, minute=0, second=0, microsecond=0)
        
        monday_last_week = monday_this_week - timedelta(days=7)
        sunday_last_week = monday_this_week - timedelta(days=1)
        
        from_date = monday_last_week.strftime("%m-%d-%Y")
        to_date = sunday_last_week.strftime("%m-%d-%Y")

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
            key = f"{channel_name} - {language}"
            
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

    def _parse_int(self, text):
        """convert string to int"""
        try:
            return int(str(text).replace(',', '').strip() or 0)
        except (ValueError, AttributeError):
            return 0
        
    def _save_data(self, data):
        """save data to file"""
        os.makedirs(self.data_directory, exist_ok=True)
        
        json_str = json.dumps(data, indent=4, ensure_ascii=False)
        python_str = json_str.replace('"has_data": true', '"has_data": True').replace('"has_data": false', '"has_data": False')
        
        py_file = os.path.join(self.data_directory, "data_marketing_pages_last_week.py")
        current_time_gmt8 = datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(f"# get data baseline marketing page last week at {current_time_gmt8} (GMT+8)\n\n")
            f.write(f"class DataMarketingPagesLastWeek:\n")
            f.write(f"    data_marketing_pages_last_week = ")
            f.write(python_str)
            f.write("\n")
