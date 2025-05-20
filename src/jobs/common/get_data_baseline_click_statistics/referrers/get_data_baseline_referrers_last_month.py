import os
import pytz
import json
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer


class GetDataBaselineReferrersLastMonth(GetDataCustomer):

    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_referrers")
        self.timezone = pytz.timezone('Asia/Singapore')

    def get_data_referrers_last_month(self):
        username = "12betaff001"
        device_type = "All"
        
        today = datetime.now(self.timezone)
        first_day_current_month = today.replace(day=1)
        last_day_previous_month = first_day_current_month - timedelta(days=1)
        first_day_previous_month = last_day_previous_month.replace(day=1)
        from_date = first_day_previous_month.strftime("%m-%d-%Y")
        to_date = last_day_previous_month.strftime("%m-%d-%Y")

        raw_data = super().get_data_referrers_in_customer(username, from_date, to_date, device_type)
        
        collected_data = {
            "metadata": {
                "collected_at": datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z"),
                "period": {
                    "from_date": from_date,
                    "to_date": to_date
                },
                "filters": {
                    "username": username,
                    "device_type": device_type
                },
                "has_data": True
            },
            "site_urls_data": {},
            "website_urls_data": {}
        }
        
        if not raw_data.get("has_data", True):
            collected_data["metadata"]["has_data"] = False
            self._save_data(collected_data)
            return collected_data
        
        for site_data in raw_data["site_urls_data"]:
            site_url = site_data["site_url"]
            
            collected_data["site_urls_data"][site_url] = {
                "site_url": site_url,
                "total_clicks": self._parse_int(site_data["total_click"]),
                "unique_clicks": self._parse_int(site_data["unique_click"]),
                "signups": self._parse_int(site_data["signups"]),
                "fdm": self._parse_int(site_data["fdm"])
            }
        
        collected_data["website_urls_data"] = {}
        for site_url, urls_data in raw_data["website_urls_data"].items():
            collected_data["website_urls_data"][site_url] = []
            for url_data in urls_data:
                collected_data["website_urls_data"][site_url].append({
                    "website_url": url_data["website_url"],
                    "total_clicks": self._parse_int(url_data["total_clicks"]),
                    "unique_clicks": self._parse_int(url_data["unique_clicks"]),
                    "signups": self._parse_int(url_data["sign_up"]),
                    "fdm": self._parse_int(url_data["fdm"])
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
        
        py_file = os.path.join(self.data_directory, "data_referrers_last_month.py")
        current_time_gmt8 = datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(f"# get data baseline referrers last month at {current_time_gmt8} (GMT+8)\n\n")
            f.write(f"class DataReferrersLastMonth:\n")
            f.write(f"    data_referrers_last_month = ")
            f.write(python_str)
            f.write("\n")
