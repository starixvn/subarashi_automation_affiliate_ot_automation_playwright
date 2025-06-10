from config.constants.settings import *
env = ENVIRONMENT
import random
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer

from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month import DataLandingPagesLastMonth
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week import DataLandingPagesLastWeek
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday import DataLandingPagesYesterday
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month_by_desktop import DataLandingPagesLastMonthByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week_by_desktop import DataLandingPagesLastWeekByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday_by_desktop import DataLandingPagesYesterdayByDesktop
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_month_by_mobile import DataLandingPagesLastMonthByMobile
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_last_week_by_mobile import DataLandingPagesLastWeekByMobile
from src.test_data.common.data_click_statistics.data_landing_pages.data_landing_pages_yesterday_by_mobile import DataLandingPagesYesterdayByMobile

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
    "Landing_Pages_Last_Month": DataLandingPagesLastMonth.data_landing_pages_last_month,
    "Landing_Pages_Last_Week": DataLandingPagesLastWeek.data_landing_pages_last_week,
    "Landing_Pages_Yesterday": DataLandingPagesYesterday.data_landing_pages_yesterday,
    "Landing_Pages_Last_Month_By_Desktop": DataLandingPagesLastMonthByDesktop.data_landing_pages_last_month_by_desktop,
    "Landing_Pages_Last_Week_By_Desktop": DataLandingPagesLastWeekByDesktop.data_landing_pages_last_week_by_desktop,
    "Landing_Pages_Yesterday_By_Desktop": DataLandingPagesYesterdayByDesktop.data_landing_pages_yesterday_by_desktop,
    "Landing_Pages_Last_Month_By_Mobile": DataLandingPagesLastMonthByMobile.data_landing_pages_last_month_by_mobile,
    "Landing_Pages_Last_Week_By_Mobile": DataLandingPagesLastWeekByMobile.data_landing_pages_last_week_by_mobile,
    "Landing_Pages_Yesterday_By_Mobile": DataLandingPagesYesterdayByMobile.data_landing_pages_yesterday_by_mobile,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"

class CompareDataLandingPage(GetDataCustomer):
    _cache_data = None
    _cache_username = None
    
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    @staticmethod
    def clear_cache():
        CompareDataLandingPage._cache_data = None
        CompareDataLandingPage._cache_username = None

    def _compare_pages_data(self, baseline_pages_data, current_pages_data):
        language_mapping = {
            "chinese simplified": "zh-cn",
            "english": "en-us",
            "bengali": "bn-in",
            "english (india)": "en-in",
            "indonesian": "id-id",
            "japanese": "ja-jp",
            "korean": "ko-kr",
            "thai": "th-th",
            "vietnamese": "vi-vn",
            "telugu": "te-in"
        }
        
        if len(baseline_pages_data) != len(current_pages_data):
            raise Exception(f"Number of pages mismatch. Baseline: {len(baseline_pages_data)}, Current: {len(current_pages_data)}")
        
        for baseline_page_data in baseline_pages_data:
            page_name = baseline_page_data["page_name"]
            language = baseline_page_data["language"]
            language_lower = language.lower()
            
            if language_lower in language_mapping:
                language_code = language_mapping[language_lower]
            else:
                language_code = language_lower
            
            page_found = False
            
            for current_page in current_pages_data:
                current_language_lower = current_page["language"].lower()
                
                if current_language_lower in language_mapping:
                    current_language_code = language_mapping[current_language_lower]
                else:
                    current_language_code = current_language_lower
                
                if current_page["page_name"].lower() == page_name.lower() and current_language_code == language_code:
                    page_found = True
                    baseline_total_click = self.parse_int(baseline_page_data["total_click"])
                    current_total_click = self.parse_int(current_page["total_click"])
                    baseline_unique_click = self.parse_int(baseline_page_data["unique_click"])
                    current_unique_click = self.parse_int(current_page["unique_click"])
                    baseline_signups = self.parse_int(baseline_page_data["signups"])
                    current_signups = self.parse_int(current_page["signups"])
                    baseline_fdm = self.parse_int(baseline_page_data["fdm"])
                    current_fdm = self.parse_int(current_page["fdm"])
                    
                    if current_total_click != baseline_total_click:
                        raise Exception(f"Total clicks mismatch for page {page_name} - {language}. Baseline: {baseline_total_click}, Current: {current_total_click}")
                    if current_unique_click != baseline_unique_click:
                        raise Exception(f"Unique clicks mismatch for page {page_name} - {language}. Baseline: {baseline_unique_click}, Current: {current_unique_click}")
                    if current_signups != baseline_signups:
                        raise Exception(f"Signups mismatch for page {page_name} - {language}. Baseline: {baseline_signups}, Current: {current_signups}")
                    if current_fdm != baseline_fdm:
                        raise Exception(f"FDM mismatch for page {page_name} - {language}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                    break
            
            if not page_found and page_name.lower() != "none" and page_name.strip() != "":
                raise Exception(f"Page '{page_name} - {language}' not found in current data")
    
    def _compare_website_urls(self, baseline_website_urls_data, current_website_urls_data):
        language_mapping = {
            "chinese simplified": "zh-cn",
            "english": "en-us",
            "bengali": "bn-in",
            "english (india)": "en-in",
            "indonesian": "id-id",
            "japanese": "ja-jp",
            "korean": "ko-kr",
            "thai": "th-th",
            "vietnamese": "vi-vn",
            "telugu": "te-in"
        }
        
        transformed_current_data = {}
        lowercase_key_to_original = {}
        
        for current_key in current_website_urls_data:
            if " - " in current_key:
                page_name, language = current_key.split(" - ", 1)
                language_lower = language.lower()
                
                if language_lower in language_mapping:
                    language_code = language_mapping[language_lower]
                else:
                    language_code = language_lower
                    
                transformed_key = f"{page_name} - {language_code}"
                transformed_current_data[transformed_key] = current_website_urls_data[current_key]
                
                lowercase_key_to_original[transformed_key.lower()] = transformed_key
        
        
        for page_key in baseline_website_urls_data:
            if "none" in page_key.lower():
                continue
            
            lowercase_page_key = page_key.lower()
            
            if lowercase_page_key in lowercase_key_to_original:
                transformed_key = lowercase_key_to_original[lowercase_page_key]
                baseline_website_urls = baseline_website_urls_data[page_key]
                current_website_urls = transformed_current_data[transformed_key]
                
                if len(baseline_website_urls) != len(current_website_urls):
                    raise Exception(f"Number of website URLs mismatch for page {page_key}. Baseline: {len(baseline_website_urls)}, Current: {len(current_website_urls)}")
                
                for baseline_website in baseline_website_urls:
                    website_found = False
                    for current_website in current_website_urls:
                        if current_website["website_url"] == baseline_website["website_url"]:
                            website_found = True
                            baseline_total_clicks = self.parse_int(baseline_website["total_clicks"])
                            current_total_clicks = self.parse_int(current_website["total_clicks"])
                            baseline_unique_clicks = self.parse_int(baseline_website["unique_clicks"])
                            current_unique_clicks = self.parse_int(current_website["unique_clicks"])
                            
                            baseline_signups = 0
                            if "signups" in baseline_website:
                                baseline_signups = self.parse_int(baseline_website["signups"])
                            
                            current_signups = 0
                            if "signups" in current_website:
                                current_signups = self.parse_int(current_website["signups"])
                            elif "sign_up" in current_website:
                                current_signups = self.parse_int(current_website["sign_up"])
                            
                            baseline_fdm = self.parse_int(baseline_website["fdm"])
                            current_fdm = self.parse_int(current_website["fdm"])
                            
                            if current_total_clicks != baseline_total_clicks:
                                raise Exception(f"Total clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_total_clicks}, Current: {current_total_clicks}")
                            if current_unique_clicks != baseline_unique_clicks:
                                raise Exception(f"Unique clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_unique_clicks}, Current: {current_unique_clicks}")
                            if current_signups != baseline_signups:
                                raise Exception(f"Signups mismatch for website {baseline_website['website_url']}. Baseline: {baseline_signups}, Current: {current_signups}")
                            if current_fdm != baseline_fdm:
                                raise Exception(f"FDM mismatch for website {baseline_website['website_url']}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                            break
                    
                    if not website_found:
                        raise Exception(f"Website URL '{baseline_website['website_url']}' not found in current data for page {page_key}")
            else:
                raise Exception(f"Website URLs for page '{page_key}' not found in current data")
    
    def parse_int(self, text):
        try:
            return int(str(text).replace(',', '').strip() or 0)
        except (ValueError, TypeError):
            return 0
    
    def parse_fraction(self, text):
        try:
            if '/' in str(text):
                parts = str(text).split('/')
                return {
                    "unique": self.parse_int(parts[0]),
                    "total": self.parse_int(parts[1]) if len(parts) > 1 else 0
                }
            return {"unique": 0, "total": 0}
        except Exception:
            return {"unique": 0, "total": 0}
    
    def _format_test_results(self, results, device_display_name):
        formatted_result = ""
        formatted_result += f"\n     + Username: {results['username']}"
        formatted_result += f"\n     + Device Type: {results['device_type']}"
        formatted_result += f"\n     + From Date: {results['from_date']}"
        formatted_result += f"\n     + To Date: {results['to_date']}"
        
        if device_display_name == "All":
            formatted_result += f"\n     + Total Clicks: Statistics={results['statistics_total_clicks']}, Landing Pages={results['landing_pages_total_clicks']}"
            formatted_result += f"\n     + Unique Clicks: Statistics={results['statistics_unique_clicks']}, Landing Pages={results['landing_pages_unique_clicks']}"
        else:
            formatted_result += f"\n     + {device_display_name} Total Clicks: Statistics={results['statistics_total_clicks']}, Landing Pages={results['landing_pages_total_clicks']}"
        
        formatted_result += f"\n     + Signups: Statistics={results['statistics_signups']}, Landing Pages={results['landing_pages_signups']}"
        formatted_result += f"\n     + FDM: Statistics={results['statistics_fdm']}, Landing Pages={results['landing_pages_fdm']}"
        
        return formatted_result
    

    def _get_username(self):
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
            player_data_api = self.data_player.get_data_player_via_api()
            return player_data_api["players_data"][0]["affiliate_name"]
        
    def _get_date_range(self, period):
        today = datetime.now()
        
        if period == "last_month":
            first_day_current_month = today.replace(day=1)
            last_day_previous_month = first_day_current_month - timedelta(days=1)
            first_day_previous_month = last_day_previous_month.replace(day=1)
            from_date = first_day_previous_month.strftime("%m-%d-%Y")
            to_date = last_day_previous_month.strftime("%m-%d-%Y")
            month_date = last_day_previous_month.strftime("%m-%Y")
        elif period == "last_week":
            to_date = (today - timedelta(days=today.weekday() + 1)).strftime("%m-%d-%Y")  # Last Sunday
            from_date = (today - timedelta(days=today.weekday() + 7)).strftime("%m-%d-%Y")  # Previous Monday
            month_date = today.strftime("%m-%Y")
        elif period == "yesterday":
            yesterday = today - timedelta(days=1)
            from_date = yesterday.strftime("%m-%d-%Y")
            to_date = yesterday.strftime("%m-%d-%Y")
            month_date = yesterday.strftime("%m-%Y")

        
        return {
            "from_date": from_date,
            "to_date": to_date,
            "month_date": month_date
        }

    def preload_all_data(self):
        if CompareDataLandingPage._cache_data is not None:
            print("Using cached data from previous load!")
            return CompareDataLandingPage._cache_data, CompareDataLandingPage._cache_username
        
        cache = {
            "landing_pages": {},
            "referrers": {},
            "marketing_pages": {},
            "statistics": {}
        }
        
        if "Landing_Pages_Last_Month" not in Data or not Data["Landing_Pages_Last_Month"]:
            raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
        
        baseline_last_month = Data["Landing_Pages_Last_Month"]
        username = baseline_last_month["metadata"]["filters"]["username"]
        print(f"Using consistent username from baseline: {username}")
        
        baseline_to_cache_mapping = {
            "Landing_Pages_Last_Month": "last_month_All",
            "Landing_Pages_Last_Month_By_Desktop": "last_month_PC / Laptop",
            "Landing_Pages_Last_Month_By_Mobile": "last_month_Mobile",
            "Landing_Pages_Last_Week": "last_week_All",
            "Landing_Pages_Last_Week_By_Desktop": "last_week_PC / Laptop",
            "Landing_Pages_Last_Week_By_Mobile": "last_week_Mobile",
            "Landing_Pages_Yesterday": "yesterday_All",
            "Landing_Pages_Yesterday_By_Desktop": "yesterday_PC / Laptop",
            "Landing_Pages_Yesterday_By_Mobile": "yesterday_Mobile"
        }
        
        periods_with_data = set()
        
        print("Phase 1: Loading landing pages data...")
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if baseline_key not in Data or not Data[baseline_key]:
                print(f"Skipping {cache_key} - baseline not found")
                cache["landing_pages"][cache_key] = {"has_data": False, "pages_data": [], "website_urls_data": {}}
                continue
                
            baseline_data = Data[baseline_key]
            baseline_has_data = baseline_data["metadata"].get("has_data", True)
            
            if not baseline_has_data:
                print(f"Skipping {cache_key} - baseline has no data")
                cache["landing_pages"][cache_key] = {"has_data": False, "pages_data": [], "website_urls_data": {}}
                continue
            
            baseline_from_date = baseline_data["metadata"]["period"]["from_date"]
            baseline_to_date = baseline_data["metadata"]["period"]["to_date"]
            
            if "Mobile" in cache_key:
                device_type = "Mobile"
            elif "PC / Laptop" in cache_key:
                device_type = "PC / Laptop"
            else:
                device_type = "All"
            
            print(f"Loading landing pages data for {cache_key} (device: {device_type})")
            current_data = self.get_data_landing_pages_in_customer(
                username, "All", "All", baseline_from_date, baseline_to_date, device_type, get_detail=True
            )
            cache["landing_pages"][cache_key] = current_data
            
            period = cache_key.split("_")[0] + "_" + cache_key.split("_")[1]
            if current_data.get("has_data", True):
                periods_with_data.add(period)
                
            if period not in cache:
                cache[period] = {
                    "date_range": {
                        "from_date": baseline_from_date,
                        "to_date": baseline_to_date
                    }
                }
        
        print(f"Periods with landing pages data: {periods_with_data}")
        
        print("Phase 2: Loading referrers data...")
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if cache_key not in cache["landing_pages"]:
                continue
                
            landing_pages_data = cache["landing_pages"][cache_key]
            if not landing_pages_data.get("has_data", True):
                print(f"Skipping referrers for {cache_key} - no landing pages data")
                cache["referrers"][cache_key] = {"has_data": False, "site_urls_data": [], "website_urls_data": {}}
                continue
            
            baseline_data = Data[baseline_key]
            baseline_from_date = baseline_data["metadata"]["period"]["from_date"]
            baseline_to_date = baseline_data["metadata"]["period"]["to_date"]
            
            if "Mobile" in cache_key:
                device_type = "Mobile"
            elif "PC / Laptop" in cache_key:
                device_type = "PC / Laptop"
            else:
                device_type = "All"
            
            print(f"Loading referrers data for {cache_key} (device: {device_type})")
            referrers_data = self.get_data_referrers_in_customer(
                username, baseline_from_date, baseline_to_date, device_type, get_detail=False
            )
            cache["referrers"][cache_key] = referrers_data
        
        print("Phase 3: Loading marketing pages data...")
        for period in periods_with_data:
            period_info = cache[period]
            baseline_from_date = period_info["date_range"]["from_date"]
            baseline_to_date = period_info["date_range"]["to_date"]
            
            print(f"Loading marketing pages data for {period} (no device filter)")
            marketing_pages_data = self.get_data_marketing_pages_in_customer(
                username, "All", baseline_from_date, baseline_to_date, include_inactive_tracking=False, get_detail=False
            )
            cache["marketing_pages"][period] = marketing_pages_data

        print("Phase 4: Loading statistics data...")
        if "last_month" in periods_with_data:
            baseline_period_data = Data["Landing_Pages_Last_Month"]
            baseline_from_date = baseline_period_data["metadata"]["period"]["from_date"]
            month_date = datetime.strptime(baseline_from_date, "%m-%d-%Y").strftime("%m-%Y")
            
            print(f"Loading statistics for last_month (month: {month_date})")
            cache["statistics"]["last_month"] = self.get_data_statistics_in_customer(
                username, month_date
            )
        
        CompareDataLandingPage._cache_data = cache
        CompareDataLandingPage._cache_username = username
        
        print(f"✅ Data loading completed successfully!")
        print(f"   Username: {username}")
        print(f"   Loaded periods: {list(periods_with_data)}")
        print(f"   Landing pages cache keys: {list(cache['landing_pages'].keys())}")
        print(f"   Referrers cache keys: {list(cache['referrers'].keys())}")
        print(f"   Marketing pages cache keys: {list(cache['marketing_pages'].keys())}")
        print(f"   Statistics cache keys: {list(cache['statistics'].keys())}")
        return cache, username
    
    def check_data_landing_pages_filter_by_date_device_page_language(self, testcase):
        subAutoTestCase = ''
        mainChecklist = [
            "Verify that the Landing Pages data displays correctly according to the Page filter.",
            "Verify that the Landing Pages data displays correctly according to the date picker.",
            "Verify that the Landing Pages data displays correctly according to the Language filter.",
            "Verify that the Landing Pages data displays correctly according to the Device filter."
        ]
        indexChl = 0
        try:
            if "Landing_Pages_Last_Month" not in Data or not Data["Landing_Pages_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
                
            subAutoTestCase = '- Verify that the data displayed is correct according to the Page filter'
            
            baseline_data = Data["Landing_Pages_Last_Month"]
            username = baseline_data["metadata"]["filters"]["username"]
            from_date = baseline_data["metadata"]["period"]["from_date"]
            to_date = baseline_data["metadata"]["period"]["to_date"]
            device_type = baseline_data["metadata"]["filters"]["device_type"]
            
            if len(baseline_data["pages_data"]) > 0:
                page_name = baseline_data["pages_data"][0]["page_name"]
                if page_name.lower() != "none" and page_name.strip() != "":
                    current_data = self.get_data_landing_pages_in_customer(username, page_name, "All", from_date, to_date, device_type)
                    
                    if current_data.get("has_data", True):
                        for page_data in current_data["pages_data"]:
                            if page_data["page_name"].lower() != page_name.lower():
                                raise Exception(f"Page filter did not work correctly. Found page {page_data['page_name']} when filtering for {page_name}")
                        
                        subAutoTestCase += f"\n     + Successfully verified Page filter for '{page_name}'"
                    else:
                        subAutoTestCase += f"\n     + No data found when filtering for page '{page_name}'"
                else:
                    subAutoTestCase += "\n     + No valid page name found in baseline data to test the filter"
            else:
                subAutoTestCase += "\n     + No pages data found in baseline data to test the filter"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the date picker'
            
            date_ranges = {
                "Last Month": Data["Landing_Pages_Last_Month"],
                "Last Week": Data["Landing_Pages_Last_Week"],
                "Yesterday": Data["Landing_Pages_Yesterday"]
            }
            
            for period_name, baseline_data in date_ranges.items():
                username = baseline_data["metadata"]["filters"]["username"]
                device_type = baseline_data["metadata"]["filters"]["device_type"]
                from_date = baseline_data["metadata"]["period"]["from_date"]
                to_date = baseline_data["metadata"]["period"]["to_date"]
                
                current_data = self.get_data_landing_pages_in_customer(username, "All", "All", from_date, to_date, device_type)
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + {period_name}: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{period_name}: No current data found for user {username} from {from_date} to {to_date} with device type {device_type}, but baseline data exists")
                else:
                    self._compare_pages_data(baseline_data["pages_data"], current_data["pages_data"])
                    self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    subAutoTestCase += f"\n     + {period_name}: Successfully verified data with date range {from_date} to {to_date}"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Language filter'
            
            baseline_data = Data["Landing_Pages_Last_Month"]
            username = baseline_data["metadata"]["filters"]["username"]
            from_date = baseline_data["metadata"]["period"]["from_date"]
            to_date = baseline_data["metadata"]["period"]["to_date"]
            device_type = baseline_data["metadata"]["filters"]["device_type"]
            
            if len(baseline_data["pages_data"]) > 0:
                languages = set()
                for page_data in baseline_data["pages_data"]:
                    if page_data["language"] and page_data["language"].lower() != "none" and page_data["language"].strip() != "":
                        languages.add(page_data["language"])
                
                if languages:
                    language = next(iter(languages))
                    current_data = self.get_data_landing_pages_in_customer(username, "All", language, from_date, to_date, device_type)
                    
                    if current_data.get("has_data", True):
                        language_mapping = {
                            "chinese simplified": "zh-cn",
                            "english": "en-us",
                            "bengali": "bn-in",
                            "english (india)": "en-in",
                            "indonesian": "id-id",
                            "japanese": "ja-jp",
                            "korean": "ko-kr",
                            "thai": "th-th",
                            "vietnamese": "vi-vn",
                            "telugu": "te-in"
                        }
                        
                        language_lower = language.lower()
                        if language_lower in language_mapping:
                            language_code = language_mapping[language_lower]
                        else:
                            language_code = language_lower
                            
                        for page_data in current_data["pages_data"]:
                            current_language_lower = page_data["language"].lower()
                            if current_language_lower in language_mapping:
                                current_language_code = language_mapping[current_language_lower]
                            else:
                                current_language_code = current_language_lower
                                
                            if current_language_code != language_code:
                                raise Exception(f"Language filter did not work correctly. Found language {page_data['language']} (code: {current_language_code}) when filtering for {language} (code: {language_code})")
                        
                        subAutoTestCase += f"\n     + Successfully verified Language filter for '{language}'"
                    else:
                        subAutoTestCase += f"\n     + No data found when filtering for language '{language}'"
                else:
                    subAutoTestCase += "\n     + No valid language found in baseline data to test the filter"
            else:
                subAutoTestCase += "\n     + No pages data found in baseline data to test the filter"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Device filter'
            
            device_types = {
                "All": Data["Landing_Pages_Last_Month"],
                "PC / Laptop": Data["Landing_Pages_Last_Month_By_Desktop"],
                "Mobile": Data["Landing_Pages_Last_Month_By_Mobile"]
            }
            
            for device_name, baseline_data in device_types.items():
                username = baseline_data["metadata"]["filters"]["username"]
                from_date = baseline_data["metadata"]["period"]["from_date"]
                to_date = baseline_data["metadata"]["period"]["to_date"]
                
                current_data = self.get_data_landing_pages_in_customer(username, "All", "All", from_date, to_date, device_name)
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + Device '{device_name}': No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"Device '{device_name}': Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"Device '{device_name}': No current data found for user {username} from {from_date} to {to_date}, but baseline data exists")
                else:
                    self._compare_pages_data(baseline_data["pages_data"], current_data["pages_data"])
                    self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    subAutoTestCase += f"\n     + Device '{device_name}': Successfully verified data"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][1], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[i], testcase, "", Data["TestCase_Auto_Status"][2], sheet_name=Checklist_Sheet_Name)
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_landing_pages_statistics_match(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = ["Verify that the Landing Page data matches the data in the Statistics table."]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month"]
            device_types = [
                {"name": "All", "display_name": "All"},
                {"name": "Mobile", "display_name": "Mobile"},
                {"name": "PC / Laptop", "display_name": "Desktop"}
            ]
            
            for period in time_periods:
                if period not in cache["statistics"]:
                    print(f"Skipping {period} - no statistics data available")
                    continue
                    
                for device in device_types:
                    if subAutoTestCase:
                        subAutoTestCase += '\n'
                    subAutoTestCase += f"- Verify that the data of Landing Pages {device['display_name'].lower()} in {period.replace('_', ' ')} must match the data of Statistics summary table"
                    
                    key = f"{period}_{device['name']}"
                    data_landing_pages = cache["landing_pages"][key]
                    data_statistics = cache["statistics"][period]
                    
                    new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                    statistics_signups = self.parse_int(new_signups_fdm[0])
                    statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                    
                    pc_tracking = self.parse_fraction(data_statistics["tracking_pc_month"])
                    mobile_tracking = self.parse_fraction(data_statistics["tracking_mobile_month"])
                    
                    if device["name"] == "All":
                        statistics_total_clicks = pc_tracking["total"] + mobile_tracking["total"]
                        statistics_unique_clicks = pc_tracking["unique"] + mobile_tracking["unique"]
                    elif device["name"] == "Mobile":
                        statistics_total_clicks = mobile_tracking["total"]
                        statistics_unique_clicks = mobile_tracking["unique"]
                    else:
                        statistics_total_clicks = pc_tracking["total"]
                        statistics_unique_clicks = pc_tracking["unique"]
                    
                    landing_pages_total_clicks = 0
                    landing_pages_unique_clicks = 0
                    landing_pages_signups = 0
                    landing_pages_fdm = 0
                    
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                            landing_pages_unique_clicks += self.parse_int(page_data["unique_click"])
                            landing_pages_signups += self.parse_int(page_data["signups"])
                            landing_pages_fdm += self.parse_int(page_data["fdm"])
                    
                    mismatches = []
                    click_type = "Total Clicks"
                    if device["name"] == "Mobile":
                        click_type = "Mobile Total Clicks"
                    elif device["name"] == "PC / Laptop":
                        click_type = "Desktop Total Clicks"
                    
                    if landing_pages_total_clicks != statistics_total_clicks:
                        mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Landing Pages={landing_pages_total_clicks}")
                    
                    if landing_pages_signups != statistics_signups:
                        mismatches.append(f"Signups mismatch: Statistics={statistics_signups}, Landing Pages={landing_pages_signups}")
                    
                    if landing_pages_fdm != statistics_fdm:
                        mismatches.append(f"FDM mismatch: Statistics={statistics_fdm}, Landing Pages={landing_pages_fdm}")
                    
                    results = {
                        "username": username,
                        "device_type": device["name"],
                        "from_date": cache[period]["date_range"]["from_date"],
                        "to_date": cache[period]["date_range"]["to_date"],
                        "statistics_total_clicks": statistics_total_clicks,
                        "statistics_unique_clicks": statistics_unique_clicks,
                        "landing_pages_total_clicks": landing_pages_total_clicks,
                        "landing_pages_unique_clicks": landing_pages_unique_clicks,
                        "statistics_signups": statistics_signups,
                        "landing_pages_signups": landing_pages_signups,
                        "statistics_fdm": statistics_fdm,
                        "landing_pages_fdm": landing_pages_fdm,
                        "click_type": click_type
                    }
                    
                    subAutoTestCase += self._format_test_results(results, device["display_name"])
                    
                    if mismatches:
                        subAutoTestCase += "\n     + Mismatches found:"
                        for mismatch in mismatches[:3]:
                            subAutoTestCase += f"\n       - {mismatch}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_landing_pages_click_statistics_and_compare(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the Total Clicks for Landing Pages equal the Total Clicks for Referrers.",
            "Verify that the Total Clicks for Landing Pages equal the Total Clicks for Marketing Pages."
        ]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            device_types = ["All", "PC / Laptop", "Mobile"]
            
            for period in periods:
                if period not in cache:
                    continue
                    
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Referrers."
                    
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    data_referrers = cache["referrers"][key]
                    
                    landing_pages_total_clicks = 0
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                    
                    referrers_total_clicks = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                    
                    has_data = data_landing_pages.get("has_data", True) and data_referrers.get("has_data", True)
                    
                    if has_data:
                        subAutoTestCase += f"\n     + Username: {username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if landing_pages_total_clicks == referrers_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {landing_pages_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Landing Pages={landing_pages_total_clicks}, Referrers={referrers_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Landing Pages or Referrers."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            
            subAutoTestCase = ''
            
            for period in periods:
                if period not in cache:
                    continue
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Marketing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    data_marketing_pages = cache["marketing_pages"][period]
                    
                    landing_pages_total_clicks = 0
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                    
                    marketing_pages_total_clicks = 0
                    if data_marketing_pages.get("has_data", True):
                        for channel in data_marketing_pages["channels_data"]:
                            marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                    
                    has_data = data_landing_pages.get("has_data", True) and data_marketing_pages.get("has_data", True)
                    
                    if has_data:
                        subAutoTestCase += f"\n     + Username: {username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if landing_pages_total_clicks == marketing_pages_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {landing_pages_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Landing Pages={landing_pages_total_clicks}, Marketing Pages={marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Landing Pages or Marketing Pages."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)

    def check_data_signups_and_fdm(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the Signups for Landing Pages equal the Signups for Referrers.",
            "Verify that the Signups for Landing Pages equal the Signups for Marketing Pages.",
            "Verify that the FDM for Landing Pages equals the FDM for Referrers.",
            "Verify that the FDM for Landing Pages equals the FDM for Marketing Pages."
        ]
        
        try:
            for checklist_index, comparison_type in enumerate([
                {"data_type": "signups", "compare_with": "referrers"},
                {"data_type": "signups", "compare_with": "marketing_pages"},
                {"data_type": "fdm", "compare_with": "referrers"},
                {"data_type": "fdm", "compare_with": "marketing_pages"}
            ]):
                data_type = comparison_type["data_type"]
                compare_with = comparison_type["compare_with"]
                
                data_type_display = data_type.capitalize()
                compare_with_display = "Referrers" if compare_with == "referrers" else "Marketing Pages"
                
                subAutoTestCase = ''
                periods = ["last_month", "last_week", "yesterday"]
                device_types = ["All", "PC / Laptop", "Mobile"]
                
                for period in periods:
                    if period not in cache:
                        continue
                        
                    for device_type in device_types:
                        device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                        period_display = period.replace("_", " ")
                        
                        if subAutoTestCase:
                            subAutoTestCase += '\n\n'
                            
                        subAutoTestCase += f"- Verify that {data_type_display} for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to {data_type_display} for {compare_with_display}."
                        
                        key = f"{period}_{device_type}"
                        data_landing_pages = cache["landing_pages"][key]
                        data_compare = cache[compare_with][key]
                        
                        landing_pages_value = 0
                        if data_landing_pages.get("has_data", True):
                            for page_data in data_landing_pages["pages_data"]:
                                landing_pages_value += self.parse_int(page_data[data_type])
                        
                        compare_value = 0
                        if data_compare.get("has_data", True):
                            if compare_with == "referrers":
                                for site_data in data_compare["site_urls_data"]:
                                    compare_value += self.parse_int(site_data[data_type])
                            else:  # marketing_pages
                                for channel in data_compare["channels_data"]:
                                    compare_value += self.parse_int(channel[data_type])
                        
                        has_data = data_landing_pages.get("has_data", True) and data_compare.get("has_data", True)
                        
                        if has_data:
                            subAutoTestCase += f"\n     + Username: {username}"
                            subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                            subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                            
                            if landing_pages_value == compare_value:
                                subAutoTestCase += f"\n     + {data_type_display} match: {landing_pages_value}"
                            else:
                                subAutoTestCase += f"\n     + {data_type_display} mismatch: Landing Pages={landing_pages_value}, {compare_with_display}={compare_value}"
                        else:
                            subAutoTestCase += f"\n     + No data found for {data_type_display} for Landing Pages or {compare_with_display}."
                
                self.utils.update_result_to_ggsheet(
                    Data["TestCase_spread_sheet_id"], 
                    mainChecklist[checklist_index], 
                    testcase, 
                    subAutoTestCase, 
                    Data["TestCase_Auto_Status"][0],
                    sheet_name=Checklist_Sheet_Name
                )
                
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[checklist_index], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            checklist_index += 1
            if checklist_index < len(mainChecklist):
                for i in range(checklist_index, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)

    def verify_page_website_url_match(self, testcase):
        cache, username = self.preload_all_data()
        periods = ["last_month", "last_week", "yesterday"]
        device_types = ["All", "PC / Laptop", "Mobile"]
        
        mainChecklist = [
            "Verify that when clicking on a Page (if not None), the sub‑data table is displayed.",
            "Verify that the values in the sub‑data table match the corresponding row in the main table."
        ]
        
        subAutoTestCase = ''
        indexChl = 0
        
        try:
            for period in periods:
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display}, clicking on a Page shows the Website URLs sub-table"
                    
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    
                    has_pages = False
                    has_sub_tables = False
                    
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            page_name = page_data["page_name"]
                            language = page_data["language"]
                            page_key = f"{page_name} - {language}"
                            
                            if page_name.lower() != "none" and page_name.strip() != "":
                                has_pages = True
                                if page_key in data_landing_pages["website_urls_data"]:
                                    has_sub_tables = True
                                    break
                    
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_landing_pages.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Landing Pages."
                    elif not has_pages:
                        subAutoTestCase += f"\n     + No valid Pages found (all are 'none' or empty)."
                    elif has_sub_tables:
                        subAutoTestCase += f"\n     + Verified: Sub-data table is displayed when clicking on Pages."
                    else:
                        subAutoTestCase += f"\n     + Failed: No sub-data tables found for any Page."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            
            subAutoTestCase = ''
            
            for period in periods:
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display}, the sum of Website URL values match the Page values"
                    
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_landing_pages.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Landing Pages."
                        continue
                    
                    mismatches = []
                    for page_data in data_landing_pages["pages_data"]:
                        page_name = page_data["page_name"]
                        language = page_data["language"]
                        page_key = f"{page_name} - {language}"
                        
                        if page_name.lower() == "none" or page_name.strip() == "":
                            continue
                        
                        if page_key not in data_landing_pages["website_urls_data"]:
                            mismatches.append(f"No website URLs data found for page '{page_key}'")
                            continue
                        
                        website_urls = data_landing_pages["website_urls_data"][page_key]
                        
                        website_total_clicks = 0
                        website_unique_clicks = 0
                        website_signups = 0
                        website_fdm = 0
                        
                        for website_data in website_urls:
                            website_total_clicks += self.parse_int(website_data["total_clicks"])
                            website_unique_clicks += self.parse_int(website_data["unique_clicks"])
                            website_signups += self.parse_int(website_data["sign_up"])
                            website_fdm += self.parse_int(website_data["fdm"])
                        
                        page_total_click = self.parse_int(page_data["total_click"])
                        page_unique_click = self.parse_int(page_data["unique_click"])
                        page_signups = self.parse_int(page_data["signups"])
                        page_fdm = self.parse_int(page_data["fdm"])
                        
                        if website_total_clicks != page_total_click:
                            mismatches.append(f"Total clicks mismatch for page '{page_key}': Page value={page_total_click}, Sum of website values={website_total_clicks}")
                        
                        if website_unique_clicks != page_unique_click:
                            mismatches.append(f"Unique clicks mismatch for page '{page_key}': Page value={page_unique_click}, Sum of website values={website_unique_clicks}")
                        
                        if website_signups != page_signups:
                            mismatches.append(f"Signups mismatch for page '{page_key}': Page value={page_signups}, Sum of website values={website_signups}")
                        
                        if website_fdm != page_fdm:
                            mismatches.append(f"FDM mismatch for page '{page_key}': Page value={page_fdm}, Sum of website values={website_fdm}")
                    
                    if mismatches:
                        subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found:"
                        for mismatch in mismatches[:3]:
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(mismatches) > 3:
                            subAutoTestCase += f"\n       - ... and {len(mismatches) - 3} more"
                    else:
                        subAutoTestCase += f"\n     + Verified: All Website URL sums match their corresponding Page values."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
        
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)

    def verify_signups_fdm_statistics_match(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the total Signups for the month equal the total Signups in the Statistics data table.",
            "Verify that the total FDM for the month equals the total FDM in the Statistics data table Landing Pages."
        ]
        
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month"]
            
            for period in time_periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total Signups for Landing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_landing_pages_signups = 0
                device_signups = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    
                    landing_pages_signups = 0
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_signups += self.parse_int(page_data["signups"])
                    
                    device_signups[device_type] = landing_pages_signups
                    
                    if device_type == "All":
                        all_landing_pages_signups = landing_pages_signups
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if all_landing_pages_signups == statistics_signups:
                    subAutoTestCase += f"\n     + Signups match: Statistics={statistics_signups}, Landing Pages (All)={all_landing_pages_signups}"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch: Statistics={statistics_signups}, Landing Pages (All)={all_landing_pages_signups}"
                    subAutoTestCase += f"\n     + Landing Pages by device: PC / Laptop={device_signups['PC / Laptop']}, Mobile={device_signups['Mobile']}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
        
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    if i >= len(mainChecklist):
                        break
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],
                        sheet_name=Checklist_Sheet_Name
                    )
            self.utils.page.extract_TestCaseFailed(e)

    def verify_total_clicks_has_unique_clicks(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that if there is data in the Total Clicks column, then the Unique Click column also contains data."
        ]
        
        indexChl = 0
        subAutoTestCase = ''
        
        try:
            periods = ["last_month", "last_week", "yesterday"]
            device_types = ["All", "PC / Laptop", "Mobile"]
            
            for period in periods:
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display}, if Total Clicks has data, then Unique Clicks also has data"
                    
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"][key]
                    
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_landing_pages.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Landing Pages."
                        continue
                    
                    violations = []
                    total_pages = 0
                    pages_with_total_clicks = 0
                    
                    for page_data in data_landing_pages["pages_data"]:
                        page_name = page_data["page_name"]
                        language = page_data["language"]
                        page_key = f"{page_name} - {language}"
                        total_clicks = self.parse_int(page_data["total_click"])
                        unique_clicks = self.parse_int(page_data["unique_click"])
                        
                        total_pages += 1
                        
                        if total_clicks > 0:
                            pages_with_total_clicks += 1
                            if unique_clicks == 0:
                                violations.append(f"Page '{page_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                    
                    for page_key, website_urls in data_landing_pages["website_urls_data"].items():
                        for website_data in website_urls:
                            website_url = website_data["website_url"]
                            total_clicks = self.parse_int(website_data["total_clicks"])
                            unique_clicks = self.parse_int(website_data["unique_clicks"])
                            
                            if total_clicks > 0 and unique_clicks == 0:
                                violations.append(f"Website URL '{website_url}' under Page '{page_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                    
                    if not pages_with_total_clicks:
                        subAutoTestCase += f"\n     + No pages with Total Clicks data found."
                    elif violations:
                        subAutoTestCase += f"\n     + Failed: {len(violations)} pages/websites have Total Clicks but no Unique Clicks:"
                        for violation in violations[:3]:
                            subAutoTestCase += f"\n       - {violation}"
                        if len(violations) > 3:
                            subAutoTestCase += f"\n       - ... and {len(violations) - 3} more"
                    else:
                        subAutoTestCase += f"\n     + Verified: All {pages_with_total_clicks} pages/websites with Total Clicks also have Unique Clicks data."
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
        
        except Exception as e:
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],
                sheet_name=Checklist_Sheet_Name
            )
            self.utils.page.extract_TestCaseFailed(e)