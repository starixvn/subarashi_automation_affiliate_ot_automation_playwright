import os
import pytz
import json
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer


class GetDataBaselineLandingPageYesterday(GetDataCustomer):

    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_landing_pages")
        self.timezone = pytz.timezone('Asia/Singapore')

    def get_data_landing_page_yesterday(self):
        username = "12betaff001"
        page_name = "All"
        language = "All"
        device_type = "All"
        
        today = datetime.now(self.timezone)
        yesterday = today - timedelta(days=1)
        date_str = yesterday.strftime("%m-%d-%Y")
        
        from_date = date_str
        to_date = date_str

        raw_data = super().get_data_landing_pages_in_customer(username, page_name, language, from_date, to_date, device_type)
        
        collected_data = {
            "metadata": {
                "collected_at": datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z"),
                "period": {
                    "from_date": from_date,
                    "to_date": to_date
                },
                "filters": {
                    "username": username,
                    "page_name": page_name,
                    "language": language,
                    "device_type": device_type
                },
                "has_data": True
            },
            "pages_data": {},
            "website_urls_data": {}
        }
        
        if not raw_data.get("has_data", True):
            collected_data["metadata"]["has_data"] = False
            self._save_data(collected_data)
            return collected_data
        
        for page_data in raw_data["pages_data"]:
            page_name = page_data["page_name"]
            language = page_data["language"]
            key = f"{page_name} - {language}"
            
            collected_data["pages_data"][key] = {
                "page_name": page_name,
                "language": language,
                "total_clicks": self._parse_int(page_data["total_click"]),
                "unique_clicks": self._parse_int(page_data["unique_click"]),
                "signups": self._parse_int(page_data["signups"]),
                "fdm": self._parse_int(page_data["fdm"])
            }
        
        collected_data["website_urls_data"] = {}
        for page_key, urls_data in raw_data["website_urls_data"].items():
            collected_data["website_urls_data"][page_key] = []
            for url_data in urls_data:
                collected_data["website_urls_data"][page_key].append({
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
        

        py_file = os.path.join(self.data_directory, "data_landing_pages_yesterday.py")
        current_time_gmt8 = datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(f"# get data baseline landing page yesterday at {current_time_gmt8} (GMT+8)\n\n")
            f.write(f"class DataLandingPagesYesterday:\n")
            f.write(f"    data_landing_pages_yesterday = ")
            f.write(python_str)
            f.write("\n")
