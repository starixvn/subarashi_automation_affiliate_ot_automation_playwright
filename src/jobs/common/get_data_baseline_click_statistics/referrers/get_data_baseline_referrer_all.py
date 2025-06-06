import os
import pytz
import json
import random
from datetime import datetime, timedelta
from config.constants.settings import *
from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer


class GetDataBaselineReferrerAll(GetDataCustomer):
    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_referrers")
        self.timezone = pytz.timezone('Asia/Singapore')
        self.data_player = None
    
    def _initialize_data_player(self):
        if self.data_player is None:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
    
    def _get_username(self):
        self._initialize_data_player()
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            top_100_data_player = self.data_player.get_top_100_data_player()
            return top_100_data_player["players_data"][random.randint(0, len(top_100_data_player["players_data"]) - 1)]["affiliate_name"]
    
    def _parse_int(self, text):
        try:
            return int(str(text).replace(',', '').strip() or 0)
        except (ValueError, AttributeError):
            return 0
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def _map_device_type(self, device_type):
        device_map = {
            "desktop": "PC / Laptop",
            "mobile": "Mobile",
            "all": "All"
        }
        return device_map.get(device_type.lower(), device_type)
    
    def _save_data(self, data, period, device_type):
        try:
            os.makedirs(self.data_directory, exist_ok=True)
            
            filename_parts = ["data_referrers"]
            if period == "yesterday":
                filename_parts.append("yesterday")
            elif period == "last_week":
                filename_parts.append("last_week")
            elif period == "last_month":
                filename_parts.append("last_month")
            
            if device_type.lower() != "all":
                filename_parts.append(f"by_{device_type.lower()}")
            
            filename = "_".join(filename_parts) + ".py"
            py_file = os.path.join(self.data_directory, filename)
            
            class_name_parts = ["DataReferrers"]
            if period == "yesterday":
                class_name_parts.append("Yesterday")
            elif period == "last_week":
                class_name_parts.append("LastWeek")
            elif period == "last_month":
                class_name_parts.append("LastMonth")
            
            if device_type.lower() == "desktop":
                class_name_parts.append("ByDesktop")
            elif device_type.lower() == "mobile":
                class_name_parts.append("ByMobile")
            
            class_name = "".join(class_name_parts)
            
            var_name_parts = ["data_referrers"]
            if period == "yesterday":
                var_name_parts.append("yesterday")
            elif period == "last_week":
                var_name_parts.append("last_week")
            elif period == "last_month":
                var_name_parts.append("last_month")
            
            if device_type.lower() == "desktop":
                var_name_parts.append("by_desktop")
            elif device_type.lower() == "mobile":
                var_name_parts.append("by_mobile")
            
            var_name = "_".join(var_name_parts)
            
            description = f"get data baseline referrer {period}"
            if device_type.lower() != "all":
                description += f" by {device_type.lower()}"
            
            json_str = json.dumps(data, indent=4, ensure_ascii=False)
            python_str = json_str.replace('"has_data": true', '"has_data": True').replace('"has_data": false', '"has_data": False')
            
            current_time_gmt8 = datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z")
            with open(py_file, "w", encoding="utf-8") as f:
                f.write(f"# {description} at {current_time_gmt8} (GMT+8)\n\n")
                f.write(f"class {class_name}:\n")
                f.write(f"    {var_name} = ")
                f.write(python_str)
                f.write("\n")
            
            return py_file
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def _get_referrer_data(self, period, device_type="all"):
        try:
            username = self._get_username()
            device_type_api = self._map_device_type(device_type)
            
            today = datetime.now(self.timezone)
            
            if period == "yesterday":
                yesterday = today - timedelta(days=1)
                from_date = yesterday.strftime("%m-%d-%Y")
                to_date = from_date
            elif period == "last_week":
                current_weekday = today.weekday()
                days_since_monday = current_weekday
                monday_this_week = today - timedelta(days=days_since_monday)
                monday_this_week = monday_this_week.replace(hour=0, minute=0, second=0, microsecond=0)
                
                monday_last_week = monday_this_week - timedelta(days=7)
                sunday_last_week = monday_this_week - timedelta(days=1)
                
                from_date = monday_last_week.strftime("%m-%d-%Y")
                to_date = sunday_last_week.strftime("%m-%d-%Y")
            elif period == "last_month":
                first_day_current_month = today.replace(day=1)
                last_day_previous_month = first_day_current_month - timedelta(days=1)
                first_day_previous_month = last_day_previous_month.replace(day=1)
                from_date = first_day_previous_month.strftime("%m-%d-%Y")
                to_date = last_day_previous_month.strftime("%m-%d-%Y")
            else:
                raise ValueError(f"Invalid period: {period}")
            
            raw_data = super().get_data_referrers_via_api(username, from_date, to_date, device_type_api)
            
            collected_data = {
                "metadata": {
                    "collected_at": datetime.now(self.timezone).strftime("%Y-%m-%d %H:%M:%S %z"),
                    "period": {
                        "from_date": from_date,
                        "to_date": to_date
                    },
                    "filters": {
                        "username": username,
                        "device_type": device_type_api
                    },
                    "has_data": True
                },
                "site_urls_data": [],
                "website_urls_data": {}
            }
            
            if not raw_data.get("has_data", True):
                collected_data["metadata"]["has_data"] = False
                self._save_data(collected_data, period, device_type)
                return collected_data
            
            for site_data in raw_data["site_urls_data"]:
                site_url = site_data["site_url"]
                
                collected_data["site_urls_data"].append({
                    "site_url": site_url,
                    "total_click": self._parse_int(site_data["total_click"]),
                    "unique_click": self._parse_int(site_data["unique_click"]),
                    "signups": self._parse_int(site_data["signups"]),
                    "fdm": self._parse_int(site_data["fdm"])
                })
            
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
            
            self._save_data(collected_data, period, device_type)
            return collected_data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_data_referrer_yesterday(self):
        return self._get_referrer_data("yesterday", "all")
    
    def get_data_referrer_yesterday_by_desktop(self):
        return self._get_referrer_data("yesterday", "desktop")
    
    def get_data_referrer_yesterday_by_mobile(self):
        return self._get_referrer_data("yesterday", "mobile")
    
    def get_data_referrer_last_week(self):
        return self._get_referrer_data("last_week", "all")
    
    def get_data_referrer_last_week_by_desktop(self):
        return self._get_referrer_data("last_week", "desktop")
    
    def get_data_referrer_last_week_by_mobile(self):
        return self._get_referrer_data("last_week", "mobile")
    
    def get_data_referrer_last_month(self):
        return self._get_referrer_data("last_month", "all")
    
    def get_data_referrer_last_month_by_desktop(self):
        return self._get_referrer_data("last_month", "desktop")
    
    def get_data_referrer_last_month_by_mobile(self):
        return self._get_referrer_data("last_month", "mobile")
    
    def get_all_referrer_data(self):
        results = {}
        
        results["yesterday"] = self.get_data_referrer_yesterday()
        results["yesterday_desktop"] = self.get_data_referrer_yesterday_by_desktop()
        results["yesterday_mobile"] = self.get_data_referrer_yesterday_by_mobile()
        
        results["last_week"] = self.get_data_referrer_last_week()
        results["last_week_desktop"] = self.get_data_referrer_last_week_by_desktop()
        results["last_week_mobile"] = self.get_data_referrer_last_week_by_mobile()
        
        results["last_month"] = self.get_data_referrer_last_month()
        results["last_month_desktop"] = self.get_data_referrer_last_month_by_desktop()
        results["last_month_mobile"] = self.get_data_referrer_last_month_by_mobile()
        
        return results 