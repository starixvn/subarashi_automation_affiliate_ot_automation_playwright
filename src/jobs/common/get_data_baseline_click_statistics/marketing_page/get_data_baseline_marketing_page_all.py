import os
import pytz
import json
import random
from datetime import datetime, timedelta
from config.constants.settings import *
from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer


class GetDataBaselineMarketingPageAll(GetDataCustomer):
    """
    A consolidated class that combines all marketing page data collection methods.
    This replaces multiple separate files with a single file while maintaining the same functionality.
    """
    
    def __init__(self):
        super().__init__()
        self.data_directory = os.path.join("src", "test_data", "common", "data_click_statistics", "data_marketing_pages")
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
    
    def _save_data(self, data, period, include_inactive=False):
        """Save data to appropriate file based on period and include_inactive flag"""
        try:
            os.makedirs(self.data_directory, exist_ok=True)
            
            filename_parts = ["data_marketing_pages"]
            if period == "yesterday":
                filename_parts.append("yesterday")
            elif period == "last_week":
                filename_parts.append("last_week")
            elif period == "last_month":
                filename_parts.append("last_month")
            
            if include_inactive:
                filename_parts.append("with_inactive")
            
            filename = "_".join(filename_parts) + ".py"
            py_file = os.path.join(self.data_directory, filename)
            
            class_name_parts = ["DataMarketingPages"]
            if period == "yesterday":
                class_name_parts.append("Yesterday")
            elif period == "last_week":
                class_name_parts.append("LastWeek")
            elif period == "last_month":
                class_name_parts.append("LastMonth")
            
            if include_inactive:
                class_name_parts.append("WithInactive")
            
            class_name = "".join(class_name_parts)
            
            var_name_parts = ["data_marketing_pages"]
            if period == "yesterday":
                var_name_parts.append("yesterday")
            elif period == "last_week":
                var_name_parts.append("last_week")
            elif period == "last_month":
                var_name_parts.append("last_month")
            
            if include_inactive:
                var_name_parts.append("with_inactive")
            
            var_name = "_".join(var_name_parts)
            
            description = f"get data baseline marketing page {period}"
            if include_inactive:
                description += " with inactive tracking"
            
            json_str = json.dumps(data, indent=4, ensure_ascii=False)
            python_str = json_str.replace('"has_data": true', '"has_data": True')\
                    .replace('"has_data": false', '"has_data": False')\
                    .replace('"include_inactive_tracking": true', '"include_inactive_tracking": True')\
                    .replace('"include_inactive_tracking": false', '"include_inactive_tracking": False')\
                    .replace(': true', ': True')\
                    .replace(': false', ': False')\
                    .replace(': null', ': None')
            
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
    
    def _get_marketing_page_data(self, period, language="All", include_inactive=False):
        """
        Generic method to get marketing page data for different periods
        
        Args:
            period (str): 'yesterday', 'last_week', or 'last_month'
            language (str): Language filter
            include_inactive (bool): Whether to include inactive tracking links
        
        Returns:
            dict: Collected data
        """
        try:
            username = self._get_username()
            
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
            
            raw_data = super().get_data_marketing_pages_via_api(
                username, 
                language=language,
                from_date=from_date, 
                to_date=to_date, 
                include_inactive_tracking=include_inactive
            )
            
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
                        "include_inactive_tracking": include_inactive
                    },
                    "has_data": True
                },
                "channels_data": [],
                "channel_details_data": {}
            }
            
            if not raw_data.get("has_data", True):
                collected_data["metadata"]["has_data"] = False
                self._save_data(collected_data, period, include_inactive)
                return collected_data
            
            for channel_data in raw_data["channels_data"]:
                collected_data["channels_data"].append({
                    "channel_name": channel_data["channel_name"],
                    "language": channel_data["language"],
                    "total_click": self._parse_int(channel_data["total_click"]),
                    "unique_click": self._parse_int(channel_data["unique_click"]),
                    "signups": self._parse_int(channel_data["signups"]),
                    "fdm": self._parse_int(channel_data["fdm"])
                })
            
            for channel_key, urls_data in raw_data["channel_details_data"].items():
                collected_data["channel_details_data"][channel_key] = []
                for url_data in urls_data:
                    collected_data["channel_details_data"][channel_key].append({
                        "url": url_data["url"],
                        "language": url_data["language"],
                        "total_clicks": self._parse_int(url_data["total_clicks"]),
                        "unique_clicks": self._parse_int(url_data["unique_clicks"]),
                        "signups": self._parse_int(url_data["signups"]),
                        "fdm": self._parse_int(url_data["fdm"])
                    })
            
            self._save_data(collected_data, period, include_inactive)
            return collected_data
        except Exception as e:
            self.utils.page.extract_TestCaseFailed(e)
    
    def get_data_marketing_page_yesterday(self, include_inactive=False):
        """Get marketing page data for yesterday"""
        return self._get_marketing_page_data("yesterday", include_inactive=include_inactive)
    
    def get_data_marketing_page_last_week(self, include_inactive=False):
        """Get marketing page data for last week"""
        return self._get_marketing_page_data("last_week", include_inactive=include_inactive)
    
    def get_data_marketing_page_last_month(self, include_inactive=False):
        """Get marketing page data for last month"""
        return self._get_marketing_page_data("last_month", include_inactive=include_inactive)
    
    def get_all_marketing_page_data(self, include_inactive=False):
        """Run all marketing page data collection methods"""
        results = {}
        
        # Yesterday data
        results["yesterday"] = self.get_data_marketing_page_yesterday(include_inactive)
        
        # Last week data
        results["last_week"] = self.get_data_marketing_page_last_week(include_inactive)
        
        # Last month data
        results["last_month"] = self.get_data_marketing_page_last_month(include_inactive)
        
        return results 