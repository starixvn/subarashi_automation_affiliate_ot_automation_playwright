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
        
        mismatches = []
        
        if len(baseline_pages_data) != len(current_pages_data):
            mismatches.append(f"Number of pages mismatch. Baseline: {len(baseline_pages_data)}, Current: {len(current_pages_data)}")
        
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
                        mismatches.append(f"Total clicks mismatch for page {page_name} - {language}. Baseline: {baseline_total_click}, Current: {current_total_click}")
                    if current_unique_click != baseline_unique_click:
                        mismatches.append(f"Unique clicks mismatch for page {page_name} - {language}. Baseline: {baseline_unique_click}, Current: {current_unique_click}")
                    if current_signups != baseline_signups:
                        mismatches.append(f"Signups mismatch for page {page_name} - {language}. Baseline: {baseline_signups}, Current: {current_signups}")
                    if current_fdm != baseline_fdm:
                        mismatches.append(f"FDM mismatch for page {page_name} - {language}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                    break
            
            if not page_found and page_name.lower() != "none" and page_name.strip() != "":
                mismatches.append(f"Page '{page_name} - {language}' not found in current data")
        
        return mismatches
    
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
        
        consolidated_baseline, baseline_consolidation_stats = self._consolidate_website_urls_data(baseline_website_urls_data)
        consolidated_current, current_consolidation_stats = self._consolidate_website_urls_data(current_website_urls_data)
        
        mismatches = []
        
        transformed_current_data = {}
        lowercase_key_to_original = {}
        
        for current_key in consolidated_current:
            if " - " in current_key:
                page_name, language = current_key.split(" - ", 1)
                language_lower = language.lower()
                
                if language_lower in language_mapping:
                    language_code = language_mapping[language_lower]
                else:
                    language_code = language_lower
                    
                transformed_key = f"{page_name} - {language_code}"
                transformed_current_data[transformed_key] = consolidated_current[current_key]
                
                lowercase_key_to_original[transformed_key.lower()] = transformed_key
        
        for page_key in consolidated_baseline:
            if "none" in page_key.lower():
                continue
            
            lowercase_page_key = page_key.lower()
            
            if lowercase_page_key in lowercase_key_to_original:
                transformed_key = lowercase_key_to_original[lowercase_page_key]
                baseline_website_urls = consolidated_baseline[page_key]
                current_website_urls = transformed_current_data[transformed_key]
                
                if len(baseline_website_urls) != len(current_website_urls):
                    current_website_urls_list = [w.get("website_url", "unknown") for w in current_website_urls] if current_website_urls else []
                    baseline_website_urls_list = [w.get("website_url", "unknown") for w in baseline_website_urls] if baseline_website_urls else []
                    mismatches.append(f"Number of website URLs mismatch for page {page_key}. Baseline: {len(baseline_website_urls)} URLs {baseline_website_urls_list[:3]}{'...' if len(baseline_website_urls_list) > 3 else ''}, Current: {len(current_website_urls)} URLs {current_website_urls_list[:3]}{'...' if len(current_website_urls_list) > 3 else ''}")
                
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
                                mismatches.append(f"Total clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_total_clicks}, Current: {current_total_clicks}")
                            if current_unique_clicks != baseline_unique_clicks:
                                mismatches.append(f"Unique clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_unique_clicks}, Current: {current_unique_clicks}")
                            if current_signups != baseline_signups:
                                mismatches.append(f"Signups mismatch for website {baseline_website['website_url']}. Baseline: {baseline_signups}, Current: {current_signups}")
                            if current_fdm != baseline_fdm:
                                mismatches.append(f"FDM mismatch for website {baseline_website['website_url']}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                            break
                    
                    if not website_found:
                        mismatches.append(f"Website URL '{baseline_website['website_url']}' not found in current data for page {page_key}")
            else:
                available_keys = list(lowercase_key_to_original.keys())
                mismatches.append(f"Website URLs for page '{page_key}' not found in current data. Available keys: {available_keys[:5]}{'...' if len(available_keys) > 5 else ''}")
        
        return mismatches
    
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
    
    def _consolidate_website_urls_data(self, website_urls_data):
        consolidated_data = {}
        consolidation_stats = {
            "total_original_websites": 0,
            "total_consolidated_websites": 0,
            "pages_with_duplicates": 0,
            "duplicate_urls_found": []
        }
        
        for page_key, website_list in website_urls_data.items():
            if not isinstance(website_list, list):
                consolidated_data[page_key] = website_list
                continue
                
            original_count = len(website_list)
            consolidation_stats["total_original_websites"] += original_count
            
            url_groups = {}
            for website_data in website_list:
                url = website_data.get("website_url", "")
                if url not in url_groups:
                    url_groups[url] = []
                url_groups[url].append(website_data)
            
            page_has_duplicates = False
            for url, group in url_groups.items():
                if len(group) > 1:
                    page_has_duplicates = True
                    consolidation_stats["duplicate_urls_found"].append({
                        "page": page_key,
                        "url": url,
                        "duplicate_count": len(group)
                    })
            
            if page_has_duplicates:
                consolidation_stats["pages_with_duplicates"] += 1
            
            consolidated_websites = []
            for url, group in url_groups.items():
                if len(group) == 1:
                    consolidated_websites.append(group[0])
                else:
                    consolidated_website = {
                        "website_url": url,
                        "total_clicks": 0,
                        "unique_clicks": 0,
                        "signups": 0,
                        "fdm": 0
                    }
                    
                    for website_data in group:
                        consolidated_website["total_clicks"] += self.parse_int(website_data.get("total_clicks", 0))
                        consolidated_website["unique_clicks"] += self.parse_int(website_data.get("unique_clicks", 0))
                        
                        signups_value = 0
                        if "signups" in website_data:
                            signups_value = self.parse_int(website_data["signups"])
                        elif "sign_up" in website_data:
                            signups_value = self.parse_int(website_data["sign_up"])
                        consolidated_website["signups"] += signups_value
                        
                        consolidated_website["fdm"] += self.parse_int(website_data.get("fdm", 0))
                    
                    consolidated_websites.append(consolidated_website)
            
            consolidated_data[page_key] = consolidated_websites
            consolidation_stats["total_consolidated_websites"] += len(consolidated_websites)
        
        return consolidated_data, consolidation_stats
    
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
        
        return formatted_result
    
    def _get_username_for_period_device(self, period, device_type, fallback_username):
        period_mapping = {
            "last_month": {"All": "Landing_Pages_Last_Month", "PC / Laptop": "Landing_Pages_Last_Month_By_Desktop", "Mobile": "Landing_Pages_Last_Month_By_Mobile"},
            "last_week": {"All": "Landing_Pages_Last_Week", "PC / Laptop": "Landing_Pages_Last_Week_By_Desktop", "Mobile": "Landing_Pages_Last_Week_By_Mobile"},
            "yesterday": {"All": "Landing_Pages_Yesterday", "PC / Laptop": "Landing_Pages_Yesterday_By_Desktop", "Mobile": "Landing_Pages_Yesterday_By_Mobile"}
        }
        
        if period in period_mapping and device_type in period_mapping[period]:
            baseline_key = period_mapping[period][device_type]
            if baseline_key in Data and Data[baseline_key]:
                return Data[baseline_key]["metadata"]["filters"]["username"]
        
        return fallback_username

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
            to_date = (today - timedelta(days=today.weekday() + 1)).strftime("%m-%d-%Y")
            from_date = (today - timedelta(days=today.weekday() + 7)).strftime("%m-%d-%Y")
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
        
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if baseline_key not in Data or not Data[baseline_key]:
                cache["landing_pages"][cache_key] = {"has_data": False, "pages_data": [], "website_urls_data": {}}
                continue
                
            baseline_data = Data[baseline_key]
            baseline_has_data = baseline_data["metadata"].get("has_data", True)
            
            if not baseline_has_data:
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
            
            current_data = self.get_data_landing_pages_in_customer(
                username, "All", "All", baseline_from_date, baseline_to_date, device_type, get_detail=True
            )
            
            cache["landing_pages"][cache_key] = current_data
            
            cache_parts = cache_key.split("_")
            if len(cache_parts) >= 2:
                if cache_parts[0] in ["last", "yesterday"]:
                    if cache_parts[0] == "last":
                        period = cache_parts[0] + "_" + cache_parts[1]
                    else:
                        period = cache_parts[0]
                else:
                    period = cache_parts[0]
            
            if current_data.get("has_data", True):
                periods_with_data.add(period)
                
            if period not in cache:
                cache[period] = {
                    "date_range": {
                        "from_date": baseline_from_date,
                        "to_date": baseline_to_date
                    }
                }
        
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if cache_key not in cache["landing_pages"]:
                continue
                
            landing_pages_data = cache["landing_pages"][cache_key]
            if not landing_pages_data.get("has_data", True):
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
            
            referrers_data = self.get_data_referrers_in_customer(
                username, baseline_from_date, baseline_to_date, device_type, get_detail=False
            )
            cache["referrers"][cache_key] = referrers_data
        
        for period in periods_with_data:
            if period not in cache:
                continue
                
            period_info = cache[period]
            baseline_from_date = period_info["date_range"]["from_date"]
            baseline_to_date = period_info["date_range"]["to_date"]
            
            marketing_pages_data = self.get_data_marketing_pages_in_customer(
                username, "All", baseline_from_date, baseline_to_date, include_inactive_tracking=False, get_detail=False
            )
            cache["marketing_pages"][period] = marketing_pages_data

        if "last_month" in periods_with_data:
            baseline_period_data = Data["Landing_Pages_Last_Month"]
            baseline_from_date = baseline_period_data["metadata"]["period"]["from_date"]
            month_date = datetime.strptime(baseline_from_date, "%m-%d-%Y").strftime("%m-%Y")
            
            cache["statistics"]["last_month"] = self.get_data_statistics_in_customer(
                username, month_date
            )
        
        CompareDataLandingPage._cache_data = cache
        CompareDataLandingPage._cache_username = username
        return cache, username
    
    def check_data_landing_pages_filter_by_date_device_page_language(self, testcase):
        cache, username = self.preload_all_data()
        
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
            
            if len(baseline_data["pages_data"]) > 0:
                page_name = baseline_data["pages_data"][0]["page_name"]
                if page_name.lower() != "none" and page_name.strip() != "":
                    key = "last_month_All"
                    current_data = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
                    if current_data.get("has_data", True):
                        filtered_pages = [p for p in current_data["pages_data"] if p["page_name"].lower() == page_name.lower()]
                        if not filtered_pages:
                            raise Exception(f"Page filter test failed: Page '{page_name}' not found in cached data")
                        
                        subAutoTestCase += f"\n     + Successfully verified Page filter for '{page_name}' using cached data"
                    else:
                        subAutoTestCase += f"\n     + No data found when testing page filter for '{page_name}'"
                else:
                    subAutoTestCase += "\n     + No valid page name found in baseline data to test the filter"
            else:
                subAutoTestCase += "\n     + No pages data found in baseline data to test the filter"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the date picker'
            
            date_ranges = {
                "Last Month": ("last_month", Data["Landing_Pages_Last_Month"]),
                "Last Week": ("last_week", Data["Landing_Pages_Last_Week"]),
                "Yesterday": ("yesterday", Data["Landing_Pages_Yesterday"])
            }
            
            for period_name, (period, baseline_data) in date_ranges.items():
                subAutoTestCase += f"\n\n   → Testing {period_name} Date Range:"
                
                key = f"{period}_All"
                current_data = cache["landing_pages"].get(key, {"has_data": False, "pages_data": [], "website_urls_data": {}})
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                current_username = self._get_username_for_period_device(period, "All", username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                if period in cache and "date_range" in cache[period]:
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + Result: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{period_name}: No current data found, but baseline data exists")
                else:
                    baseline_pages_count = len(baseline_data["pages_data"])
                    current_pages_count = len(current_data["pages_data"])
                    baseline_websites_count = sum(len(websites) for websites in baseline_data["website_urls_data"].values())
                    current_websites_count = sum(len(websites) for websites in current_data["website_urls_data"].values())
                    
                    subAutoTestCase += f"\n     + Data Summary: Baseline={baseline_pages_count} pages, {baseline_websites_count} websites | Current={current_pages_count} pages, {current_websites_count} websites"
                    
                    page_mismatches = self._compare_pages_data(baseline_data["pages_data"], current_data["pages_data"])
                    website_mismatches = self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    
                    all_mismatches = page_mismatches + website_mismatches
                    
                    if all_mismatches:
                        total_clicks_errors = [m for m in all_mismatches if "total clicks" in m.lower()]
                        unique_clicks_errors = [m for m in all_mismatches if "unique clicks" in m.lower()]
                        signups_errors = [m for m in all_mismatches if "signups" in m.lower()]
                        fdm_errors = [m for m in all_mismatches if "fdm" in m.lower()]
                        other_errors = [m for m in all_mismatches if not any(keyword in m.lower() for keyword in ["total clicks", "unique clicks", "signups", "fdm"])]
                        
                        subAutoTestCase += f"\n     + Result: FAILED - {len(all_mismatches)} mismatches found"
                        subAutoTestCase += f"\n       • Total Clicks errors: {len(total_clicks_errors)}"
                        subAutoTestCase += f"\n       • Unique Clicks errors: {len(unique_clicks_errors)}"
                        subAutoTestCase += f"\n       • Signups errors: {len(signups_errors)}"
                        subAutoTestCase += f"\n       • FDM errors: {len(fdm_errors)}"
                        subAutoTestCase += f"\n       • Other errors: {len(other_errors)}"
                        
                        subAutoTestCase += f"\n     + Sample mismatches (first 4):"
                        for i, mismatch in enumerate(all_mismatches[:4]):
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(all_mismatches) > 4:
                            subAutoTestCase += f"\n       - ... and {len(all_mismatches) - 4} more mismatches"
                    else:
                        subAutoTestCase += f"\n     + Result: PASSED - All data matches between baseline and current"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Language filter'
            
            baseline_data = Data["Landing_Pages_Last_Month"]
            
            if len(baseline_data["pages_data"]) > 0:
                languages = set()
                for page_data in baseline_data["pages_data"]:
                    if page_data["language"] and page_data["language"].lower() != "none" and page_data["language"].strip() != "":
                        languages.add(page_data["language"])
                
                if languages:
                    language = next(iter(languages))
                    key = "last_month_All"
                    current_data = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
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
                        
                        language_found = False
                        for page_data in current_data["pages_data"]:
                            current_language_lower = page_data["language"].lower()
                            if current_language_lower in language_mapping:
                                current_language_code = language_mapping[current_language_lower]
                            else:
                                current_language_code = current_language_lower
                                
                            if current_language_code == language_code:
                                language_found = True
                                break
                        
                        if language_found:
                            subAutoTestCase += f"\n     + Successfully verified Language filter for '{language}'"
                        else:
                            subAutoTestCase += f"\n     + Language '{language}' not found in cached data"
                    else:
                        subAutoTestCase += f"\n     + No data found when testing language filter for '{language}'"
                else:
                    subAutoTestCase += "\n     + No valid language found in baseline data to test the filter"
            else:
                subAutoTestCase += "\n     + No pages data found in baseline data to test the filter"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Device filter'
            
            device_types = {
                "All": ("last_month_All", Data["Landing_Pages_Last_Month"]),
                "PC / Laptop": ("last_month_PC / Laptop", Data["Landing_Pages_Last_Month_By_Desktop"]),
                "Mobile": ("last_month_Mobile", Data["Landing_Pages_Last_Month_By_Mobile"])
            }
            
            for device_name, (key, baseline_data) in device_types.items():
                subAutoTestCase += f"\n\n   → Testing Device Filter: {device_name}"
                
                current_data = cache["landing_pages"].get(key, {"has_data": False, "pages_data": [], "website_urls_data": {}})
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                current_username = self._get_username_for_period_device("last_month", device_name, username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + Device Type: {device_name}"
                if "last_month" in cache and "date_range" in cache["last_month"]:
                    subAutoTestCase += f"\n     + From Date: {cache['last_month']['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache['last_month']['date_range']['to_date']}"
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + Result: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"Device '{device_name}': Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"Device '{device_name}': No current data found, but baseline data exists")
                else:
                    baseline_pages_count = len(baseline_data["pages_data"])
                    current_pages_count = len(current_data["pages_data"])
                    baseline_websites_count = sum(len(websites) for websites in baseline_data["website_urls_data"].values())
                    current_websites_count = sum(len(websites) for websites in current_data["website_urls_data"].values())
                    
                    subAutoTestCase += f"\n     + Data Summary: Baseline={baseline_pages_count} pages, {baseline_websites_count} websites | Current={current_pages_count} pages, {current_websites_count} websites"
                    
                    page_mismatches = self._compare_pages_data(baseline_data["pages_data"], current_data["pages_data"])
                    website_mismatches = self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    
                    all_mismatches = page_mismatches + website_mismatches
                    
                    if all_mismatches:
                        total_clicks_errors = [m for m in all_mismatches if "total clicks" in m.lower()]
                        unique_clicks_errors = [m for m in all_mismatches if "unique clicks" in m.lower()]
                        signups_errors = [m for m in all_mismatches if "signups" in m.lower()]
                        fdm_errors = [m for m in all_mismatches if "fdm" in m.lower()]
                        other_errors = [m for m in all_mismatches if not any(keyword in m.lower() for keyword in ["total clicks", "unique clicks", "signups", "fdm"])]
                        
                        subAutoTestCase += f"\n     + Result: FAILED - {len(all_mismatches)} mismatches found"
                        subAutoTestCase += f"\n       • Total Clicks errors: {len(total_clicks_errors)}"
                        subAutoTestCase += f"\n       • Unique Clicks errors: {len(unique_clicks_errors)}"
                        subAutoTestCase += f"\n       • Signups errors: {len(signups_errors)}"
                        subAutoTestCase += f"\n       • FDM errors: {len(fdm_errors)}"
                        subAutoTestCase += f"\n       • Other errors: {len(other_errors)}"
                        
                        subAutoTestCase += f"\n     + Sample mismatches (first 4):"
                        for i, mismatch in enumerate(all_mismatches[:4]):
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(all_mismatches) > 4:
                            subAutoTestCase += f"\n       - ... and {len(all_mismatches) - 4} more mismatches"
                    else:
                        subAutoTestCase += f"\n     + Result: PASSED - All data matches between baseline and current"
            
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
                    continue
                    
                for device in device_types:
                    if subAutoTestCase:
                        subAutoTestCase += '\n'
                    subAutoTestCase += f"- Verify that the Total Clicks of Landing Pages {device['display_name'].lower()} in {period.replace('_', ' ')} must match the Total Clicks of Statistics summary table"
                    
                    key = f"{period}_{device['name']}"
                    data_landing_pages = cache["landing_pages"][key]
                    data_statistics = cache["statistics"][period]
                    
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
                    
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                            landing_pages_unique_clicks += self.parse_int(page_data["unique_click"])
                    
                    mismatches = []
                    click_type = "Total Clicks"
                    if device["name"] == "Mobile":
                        click_type = "Mobile Total Clicks"
                    elif device["name"] == "PC / Laptop":
                        click_type = "Desktop Total Clicks"
                    
                    if landing_pages_total_clicks != statistics_total_clicks:
                        mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Landing Pages={landing_pages_total_clicks}")
                    
                    results = {
                        "username": username,
                        "device_type": device["name"],
                        "from_date": cache[period]["date_range"]["from_date"],
                        "to_date": cache[period]["date_range"]["to_date"],
                        "statistics_total_clicks": statistics_total_clicks,
                        "statistics_unique_clicks": statistics_unique_clicks,
                        "landing_pages_total_clicks": landing_pages_total_clicks,
                        "landing_pages_unique_clicks": landing_pages_unique_clicks,
                        "click_type": click_type
                    }
                    
                    subAutoTestCase += self._format_test_results(results, device["display_name"])
                    
                    if mismatches:
                        subAutoTestCase += "\n     + Mismatches found:"
                        for mismatch in mismatches[:4]:
                            subAutoTestCase += f"\n       - {mismatch}"
                    else:
                        subAutoTestCase += f"\n     + Total Clicks validation passed: All data matches between Landing Pages and Statistics"
            
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
                        current_username = self._get_username_for_period_device(period, device_type, username)
                        subAutoTestCase += f"\n     + Username: {current_username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        subAutoTestCase += f"\n     + Device Type: {device_type}"
                        
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
                    
                device_type = "All"
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                    
                subAutoTestCase += f"- Verify that Total Clicks for Landing Pages {period_display} (All devices) are equal to Total Clicks for Marketing Pages."
                
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
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    subAutoTestCase += f"\n     + Device Type: All (Marketing Pages don't have device breakdown)"
                    
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
                
                if compare_with == "marketing_pages":
                    device_types = ["All"]
                else:
                    device_types = ["All", "PC / Laptop", "Mobile"]
                
                for period in periods:
                    if period not in cache:
                        continue
                        
                    for device_type in device_types:
                        device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                        period_display = period.replace("_", " ")
                        
                        if subAutoTestCase:
                            subAutoTestCase += '\n\n'
                            
                        if compare_with == "marketing_pages":
                            subAutoTestCase += f"- Verify that {data_type_display} for Landing Pages {period_display} (All devices) are equal to {data_type_display} for {compare_with_display}."
                        else:
                            subAutoTestCase += f"- Verify that {data_type_display} for Landing Pages {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to {data_type_display} for {compare_with_display}."
                        
                        key = f"{period}_{device_type}"
                        data_landing_pages = cache["landing_pages"][key]
                        
                        if compare_with == "referrers":
                            data_compare = cache[compare_with].get(key, {"has_data": False, "site_urls_data": []})
                        else:
                            data_compare = cache[compare_with].get(period, {"has_data": False, "channels_data": []})
                        
                        landing_pages_value = 0
                        if data_landing_pages.get("has_data", True):
                            for page_data in data_landing_pages["pages_data"]:
                                landing_pages_value += self.parse_int(page_data[data_type])
                        
                        compare_value = 0
                        if data_compare.get("has_data", True):
                            if compare_with == "referrers":
                                for site_data in data_compare["site_urls_data"]:
                                    compare_value += self.parse_int(site_data[data_type])
                            else:
                                for channel in data_compare["channels_data"]:
                                    compare_value += self.parse_int(channel[data_type])
                        
                        has_data = data_landing_pages.get("has_data", True) and data_compare.get("has_data", True)
                        
                        if has_data:
                            current_username = self._get_username_for_period_device(period, device_type, username)
                            subAutoTestCase += f"\n     + Username: {current_username}"
                            if period in cache and "date_range" in cache[period]:
                                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                            
                            if compare_with == "marketing_pages":
                                subAutoTestCase += f"\n     + Device Type: All (Marketing Pages don't have device breakdown)"
                            else:
                                subAutoTestCase += f"\n     + Device Type: {device_type}"
                            
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
                    data_landing_pages = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
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
                    
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    if period in cache and "date_range" in cache[period]:
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
                    data_landing_pages = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    if period in cache and "date_range" in cache[period]:
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_landing_pages.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Landing Pages."
                        continue
                    
                    consolidated_website_urls_data, consolidation_stats = self._consolidate_website_urls_data(data_landing_pages["website_urls_data"])
                    
                    if consolidation_stats["pages_with_duplicates"] > 0:
                        subAutoTestCase += f"\n     + Consolidation Applied: {consolidation_stats['pages_with_duplicates']} pages had duplicate URLs"
                        subAutoTestCase += f"\n       - Original websites: {consolidation_stats['total_original_websites']}, After consolidation: {consolidation_stats['total_consolidated_websites']}"
                        subAutoTestCase += f"\n       - Sample duplicates: {consolidation_stats['duplicate_urls_found'][:2] if consolidation_stats['duplicate_urls_found'] else 'None'}"
                    
                    mismatches = []
                    validation_details = []
                    
                    for page_data in data_landing_pages["pages_data"]:
                        page_name = page_data["page_name"]
                        language = page_data["language"]
                        page_key = f"{page_name} - {language}"
                        
                        if page_name.lower() == "none" or page_name.strip() == "":
                            continue
                        
                        if page_key not in consolidated_website_urls_data:
                            mismatches.append(f"No website URLs data found for page '{page_key}'")
                            continue
                        
                        website_urls = consolidated_website_urls_data[page_key]
                        
                        website_total_clicks = 0
                        website_signups = 0
                        website_fdm = 0
                        
                        for website_data in website_urls:
                            website_total_clicks += self.parse_int(website_data["total_clicks"])
                            
                            if "signups" in website_data:
                                website_signups += self.parse_int(website_data["signups"])
                            elif "sign_up" in website_data:
                                website_signups += self.parse_int(website_data["sign_up"])
                            
                            website_fdm += self.parse_int(website_data["fdm"])
                        
                        page_total_click = self.parse_int(page_data["total_click"])
                        page_signups = self.parse_int(page_data["signups"])
                        page_fdm = self.parse_int(page_data["fdm"])
                        
                        validation_details.append(f"Page '{page_key}': Total Clicks (Page={page_total_click}, Sum={website_total_clicks}), Signups (Page={page_signups}, Sum={website_signups}), FDM (Page={page_fdm}, Sum={website_fdm})")
                        
                        if website_total_clicks != page_total_click:
                            mismatches.append(f"Total clicks mismatch for page '{page_key}': Page value={page_total_click}, Sum of consolidated website values={website_total_clicks}")
                        
                        if website_signups != page_signups:
                            mismatches.append(f"Signups mismatch for page '{page_key}': Page value={page_signups}, Sum of consolidated website values={website_signups}")
                        
                        if website_fdm != page_fdm:
                            mismatches.append(f"FDM mismatch for page '{page_key}': Page value={page_fdm}, Sum of consolidated website values={website_fdm}")
                    
                    subAutoTestCase += f"\n     + Comparison Details ({len(validation_details)} pages checked, excluding unique clicks):"
                    for detail in validation_details[:4]:
                        subAutoTestCase += f"\n       • {detail}"
                    if len(validation_details) > 4:
                        subAutoTestCase += f"\n       • ... and {len(validation_details) - 4} more pages"
                    
                    if mismatches:
                        subAutoTestCase += f"\n     + Result: FAILED - {len(mismatches)} mismatches found:"
                        for mismatch in mismatches[:4]:
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(mismatches) > 4:
                            subAutoTestCase += f"\n       - ... and {len(mismatches) - 4} more mismatches"
                    else:
                        subAutoTestCase += f"\n     + Result: PASSED - All {len(data_landing_pages['pages_data'])} pages data validation completed (excluding unique clicks check)."
            
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
                    data_landing_pages = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
                    landing_pages_signups = 0
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_signups += self.parse_int(page_data["signups"])
                    
                    device_signups[device_type] = landing_pages_signups
                    
                    if device_type == "All":
                        all_landing_pages_signups = landing_pages_signups
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                current_username = self._get_username_for_period_device(period, "All", username)
                subAutoTestCase += f"\n     + Username: {current_username}"
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
            indexChl += 1
            
            subAutoTestCase = ''
            
            for period in time_periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total FDM for Landing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_landing_pages_fdm = 0
                device_fdm = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_landing_pages = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
                    landing_pages_fdm = 0
                    if data_landing_pages.get("has_data", True):
                        for page_data in data_landing_pages["pages_data"]:
                            landing_pages_fdm += self.parse_int(page_data["fdm"])
                    
                    device_fdm[device_type] = landing_pages_fdm
                    
                    if device_type == "All":
                        all_landing_pages_fdm = landing_pages_fdm
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                
                current_username = self._get_username_for_period_device(period, "All", username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if all_landing_pages_fdm == statistics_fdm:
                    subAutoTestCase += f"\n     + FDM match: Statistics={statistics_fdm}, Landing Pages (All)={all_landing_pages_fdm}"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch: Statistics={statistics_fdm}, Landing Pages (All)={all_landing_pages_fdm}"
                    subAutoTestCase += f"\n     + Landing Pages by device: PC / Laptop={device_fdm['PC / Laptop']}, Mobile={device_fdm['Mobile']}"
            
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
                    data_landing_pages = cache["landing_pages"].get(key, {"has_data": False, "pages_data": []})
                    
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    if period in cache and "date_range" in cache[period]:
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
                    
                    consolidated_website_urls_data, consolidation_stats = self._consolidate_website_urls_data(data_landing_pages["website_urls_data"])
                    
                    for page_key, website_urls in consolidated_website_urls_data.items():
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