import os
import pytz
import json
import random
from datetime import datetime, timedelta
from config.constants.settings import *
from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer


class GetDataBaselineLandingPageAll(GetDataCustomer):
    """
    A consolidated class that combines all landing page data collection methods.
    This replaces 9 separate files with a single file while maintaining the same functionality.
    """
    
    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_landing_pages")
        self.timezone = pytz.timezone('Asia/Singapore')
        self.data_player = None
    
    def _initialize_data_player(self):
        """Initialize the data player if not already done"""
        if self.data_player is None:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
    
    def _get_username(self):
        """Get username based on environment"""
        self._initialize_data_player()
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            top_100_data_player = self.data_player.get_top_100_data_player()
            return top_100_data_player["players_data"][random.randint(0, len(top_100_data_player["players_data"]) - 1)]["affiliate_name"]
    
    def _parse_int(self, text):
        """Convert string to int"""
        try:
            return int(str(text).replace(',', '').strip() or 0)
        except (ValueError, AttributeError):
            return 0
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def _map_device_type(self, device_type):
        """Map device type to API expected value"""
        device_map = {
            "desktop": "PC / Laptop",
            "mobile": "Mobile",
            "all": "All"
        }
        return device_map.get(device_type.lower(), device_type)
    
    def _save_data(self, data, period, device_type):
        """Save data to appropriate file based on period and device type"""
        try:
            os.makedirs(self.data_directory, exist_ok=True)
            
            # Format the filename based on period and device type
            filename_parts = ["data_landing_pages"]
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
            
            # Format the class name based on period and device type
            class_name_parts = ["DataLandingPages"]
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
            
            # Format the variable name based on period and device type
            var_name_parts = ["data_landing_pages"]
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
            
            # Generate description based on period and device type
            description = f"get data baseline landing page {period}"
            if device_type.lower() != "all":
                description += f" by {device_type.lower()}"
            
            # Convert data to Python-compatible string
            json_str = json.dumps(data, indent=4, ensure_ascii=False)
            python_str = json_str.replace('"has_data": true', '"has_data": True').replace('"has_data": false', '"has_data": False')
            
            # Write to file
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
    
    def _get_landing_page_data(self, period, device_type="all"):
        """
        Generic method to get landing page data for different periods and device types
        
        Args:
            period (str): 'yesterday', 'last_week', or 'last_month'
            device_type (str): 'all', 'desktop', or 'mobile'
        
        Returns:
            dict: Collected data
        """
        try:
            username = self._get_username()
            page_name = "All"
            language = "All"
            device_type_api = self._map_device_type(device_type)
            
            today = datetime.now(self.timezone)
            
            if period == "yesterday":
                yesterday = today - timedelta(days=1)
                from_date = yesterday.strftime("%m/%d/%Y")
                to_date = from_date
            elif period == "last_week":
                current_weekday = today.weekday()
                days_since_monday = current_weekday
                monday_this_week = today - timedelta(days=days_since_monday)
                monday_this_week = monday_this_week.replace(hour=0, minute=0, second=0, microsecond=0)
                
                monday_last_week = monday_this_week - timedelta(days=7)
                sunday_last_week = monday_this_week - timedelta(days=1)
                
                from_date = monday_last_week.strftime("%m/%d/%Y")
                to_date = sunday_last_week.strftime("%m/%d/%Y")
            elif period == "last_month":
                first_day_current_month = today.replace(day=1)
                last_day_previous_month = first_day_current_month - timedelta(days=1)
                first_day_previous_month = last_day_previous_month.replace(day=1)
                from_date = first_day_previous_month.strftime("%m/%d/%Y")
                to_date = last_day_previous_month.strftime("%m/%d/%Y")
            else:
                raise ValueError(f"Invalid period: {period}")
            
            raw_data = super().get_data_landing_pages_via_api(username, page_name, language, from_date, to_date, device_type_api)
            
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
                        "device_type": device_type_api
                    },
                    "has_data": True
                },
                "pages_data": {},
                "website_urls_data": {}
            }
            
            if not raw_data.get("has_data", True):
                collected_data["metadata"]["has_data"] = False
                self._save_data(collected_data, period, device_type)
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
            
            self._save_data(collected_data, period, device_type)
            return collected_data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_data_landing_page_yesterday(self):
        """Get landing page data for yesterday with all device types"""
        return self._get_landing_page_data("yesterday", "all")
    
    def get_data_landing_page_yesterday_by_desktop(self):
        """Get landing page data for yesterday with desktop device type"""
        return self._get_landing_page_data("yesterday", "desktop")
    
    def get_data_landing_page_yesterday_by_mobile(self):
        """Get landing page data for yesterday with mobile device type"""
        return self._get_landing_page_data("yesterday", "mobile")
    
    def get_data_landing_page_last_week(self):
        """Get landing page data for last week with all device types"""
        return self._get_landing_page_data("last_week", "all")
    
    def get_data_landing_page_last_week_by_desktop(self):
        """Get landing page data for last week with desktop device type"""
        return self._get_landing_page_data("last_week", "desktop")
    
    def get_data_landing_page_last_week_by_mobile(self):
        """Get landing page data for last week with mobile device type"""
        return self._get_landing_page_data("last_week", "mobile")
    
    def get_data_landing_page_last_month(self):
        """Get landing page data for last month with all device types"""
        return self._get_landing_page_data("last_month", "all")
    
    def get_data_landing_page_last_month_by_desktop(self):
        """Get landing page data for last month with desktop device type"""
        return self._get_landing_page_data("last_month", "desktop")
    
    def get_data_landing_page_last_month_by_mobile(self):
        """Get landing page data for last month with mobile device type"""
        return self._get_landing_page_data("last_month", "mobile")
    
    def get_all_landing_page_data(self):
        """Run all landing page data collection methods"""
        results = {}
        
        # Yesterday data
        results["yesterday"] = self.get_data_landing_page_yesterday()
        results["yesterday_desktop"] = self.get_data_landing_page_yesterday_by_desktop()
        results["yesterday_mobile"] = self.get_data_landing_page_yesterday_by_mobile()
        
        # Last week data
        results["last_week"] = self.get_data_landing_page_last_week()
        results["last_week_desktop"] = self.get_data_landing_page_last_week_by_desktop()
        results["last_week_mobile"] = self.get_data_landing_page_last_week_by_mobile()
        
        # Last month data
        results["last_month"] = self.get_data_landing_page_last_month()
        results["last_month_desktop"] = self.get_data_landing_page_last_month_by_desktop()
        results["last_month_mobile"] = self.get_data_landing_page_last_month_by_mobile()
        
        return results 