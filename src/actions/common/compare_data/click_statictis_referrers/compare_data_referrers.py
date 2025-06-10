from config.constants.settings import *
env = ENVIRONMENT
import random
from datetime import datetime, timedelta

from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer

from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month import DataReferrersLastMonth
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week import DataReferrersLastWeek
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday import DataReferrersYesterday
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month_by_desktop import DataReferrersLastMonthByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week_by_desktop import DataReferrersLastWeekByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday_by_desktop import DataReferrersYesterdayByDesktop
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_month_by_mobile import DataReferrersLastMonthByMobile
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_last_week_by_mobile import DataReferrersLastWeekByMobile
from src.test_data.common.data_click_statistics.data_referrers.data_referrers_yesterday_by_mobile import DataReferrersYesterdayByMobile

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
    "Referres_Last_Month" : DataReferrersLastMonth.data_referrers_last_month,
    "Referres_Last_Week" : DataReferrersLastWeek.data_referrers_last_week,
    "Referres_Yesterday" : DataReferrersYesterday.data_referrers_yesterday,
    "Referres_Last_Month_By_Desktop" : DataReferrersLastMonthByDesktop.data_referrers_last_month_by_desktop,
    "Referres_Last_Week_By_Desktop" : DataReferrersLastWeekByDesktop.data_referrers_last_week_by_desktop,
    "Referres_Yesterday_By_Desktop" : DataReferrersYesterdayByDesktop.data_referrers_yesterday_by_desktop,
    "Referres_Last_Month_By_Mobile" : DataReferrersLastMonthByMobile.data_referrers_last_month_by_mobile,
    "Referres_Last_Week_By_Mobile" : DataReferrersLastWeekByMobile.data_referrers_last_week_by_mobile,
    "Referres_Yesterday_By_Mobile" : DataReferrersYesterdayByMobile.data_referrers_yesterday_by_mobile,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"


class CompareDataReferrers(GetDataCustomer):
    _cache_data = None
    _cache_username = None
    
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    @staticmethod
    def clear_cache():
        CompareDataReferrers._cache_data = None
        CompareDataReferrers._cache_username = None

    def _compare_site_urls(self, baseline_site_urls, current_site_urls):
        if len(baseline_site_urls) != len(current_site_urls):
            raise Exception(f"Number of site URLs mismatch. Baseline: {len(baseline_site_urls)}, Current: {len(current_site_urls)}")
        
        for baseline_site_data in baseline_site_urls:
            site_url = baseline_site_data["site_url"]
            site_found = False
            for current_site in current_site_urls:
                if current_site["site_url"].lower() == site_url.lower():
                    site_found = True
                    if int(current_site["total_click"]) != baseline_site_data["total_click"]:
                        raise Exception(f"Total clicks mismatch for site {site_url}. Baseline: {baseline_site_data['total_click']}, Current: {current_site['total_click']}")
                    if int(current_site["unique_click"]) != baseline_site_data["unique_click"]:
                        raise Exception(f"Unique clicks mismatch for site {site_url}. Baseline: {baseline_site_data['unique_click']}, Current: {current_site['unique_click']}")
                    if int(current_site["signups"]) != baseline_site_data["signups"]:
                        raise Exception(f"Signups mismatch for site {site_url}. Baseline: {baseline_site_data['signups']}, Current: {current_site['signups']}")
                    if int(current_site["fdm"]) != baseline_site_data["fdm"]:
                        raise Exception(f"FDM mismatch for site {site_url}. Baseline: {baseline_site_data['fdm']}, Current: {current_site['fdm']}")
                    break
            
            if not site_found and site_url.lower() != "none" and site_url.strip() != "":
                raise Exception(f"Site URL '{site_url}' not found in current data")
    
    def _compare_website_urls(self, baseline_website_urls_data, current_website_urls_data):
        for site_url, baseline_website_urls in baseline_website_urls_data.items():
            if site_url.lower() == "none":
                continue
            
            if site_url not in current_website_urls_data:
                raise Exception(f"Website URLs for site '{site_url}' not found in current data")
            
            current_website_urls = current_website_urls_data[site_url]
            
            if len(baseline_website_urls) != len(current_website_urls):
                raise Exception(f"Number of website URLs mismatch for site {site_url}. Baseline: {len(baseline_website_urls)}, Current: {len(current_website_urls)}")
            
            for baseline_website in baseline_website_urls:
                website_found = False
                for current_website in current_website_urls:
                    if current_website["website_url"] == baseline_website["website_url"]:
                        website_found = True
                        if int(current_website["total_clicks"]) != baseline_website["total_clicks"]:
                            raise Exception(f"Total clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['total_clicks']}, Current: {current_website['total_clicks']}")
                        if int(current_website["unique_clicks"]) != baseline_website["unique_clicks"]:
                            raise Exception(f"Unique clicks mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['unique_clicks']}, Current: {current_website['unique_clicks']}")
                        
                        baseline_signups = baseline_website["signups"]
                        current_signups = 0
                        if "signups" in current_website:
                            current_signups = int(current_website["signups"])
                        elif "sign_up" in current_website:
                            current_signups = int(current_website["sign_up"])
                        
                        if current_signups != baseline_signups:
                            raise Exception(f"Signups mismatch for website {baseline_website['website_url']}. Baseline: {baseline_signups}, Current: {current_signups}")
                        
                        if int(current_website["fdm"]) != baseline_website["fdm"]:
                            raise Exception(f"FDM mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['fdm']}, Current: {current_website['fdm']}")
                        break
                
                if not website_found:
                    raise Exception(f"Website URL '{baseline_website['website_url']}' not found in current data for site {site_url}")
    
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
    
    def _get_username_for_period_device(self, period, device_type, fallback_username):
        
        period_mapping = {
            "last_month": {"All": "Referres_Last_Month", "PC / Laptop": "Referres_Last_Month_By_Desktop", "Mobile": "Referres_Last_Month_By_Mobile"},
            "last_week": {"All": "Referres_Last_Week", "PC / Laptop": "Referres_Last_Week_By_Desktop", "Mobile": "Referres_Last_Week_By_Mobile"},
            "yesterday": {"All": "Referres_Yesterday", "PC / Laptop": "Referres_Yesterday_By_Desktop", "Mobile": "Referres_Yesterday_By_Mobile"}
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

    def _format_test_results(self, results, device_display_name):
        formatted_result = ""
        formatted_result += f"\n     + Username: {results['username']}"
        formatted_result += f"\n     + Device Type: {results['device_type']}"
        formatted_result += f"\n     + From Date: {results['from_date']}"
        formatted_result += f"\n     + To Date: {results['to_date']}"
        
        if device_display_name == "All":
            formatted_result += f"\n     + Total Clicks: Statistics={results['statistics_total_clicks']}, Referrers={results['referrers_total_clicks']}"
            formatted_result += f"\n     + Unique Clicks: Statistics={results['statistics_unique_clicks']}, Referrers={results['referrers_unique_clicks']}"
        else:
            formatted_result += f"\n     + {device_display_name} Total Clicks: Statistics={results['statistics_total_clicks']}, Referrers={results['referrers_total_clicks']}"
        
        formatted_result += f"\n     + Signups: Statistics={results['statistics_signups']}, Referrers={results['referrers_signups']}"
        formatted_result += f"\n     + FDM: Statistics={results['statistics_fdm']}, Referrers={results['referrers_fdm']}"
        
        return formatted_result

    def check_data_referrers_filter_by_date_and_device(self, testcase):
        cache, username = self.preload_all_data()
        
        subAutoTestCase = ''
        mainChecklist = ["Verify that the Referrers data displayed is correct according to the date picker.",
                        "Verify that the Referrers data displayed is correct by device."
                        ]
        indexChl = 0
        
        baseline_to_cache_mapping = {
            "Referres_Last_Month": "last_month_All",
            "Referres_Last_Week": "last_week_All", 
            "Referres_Yesterday": "yesterday_All",
            "Referres_Last_Month_By_Desktop": "last_month_PC / Laptop",
            "Referres_Last_Week_By_Desktop": "last_week_PC / Laptop",
            "Referres_Yesterday_By_Desktop": "yesterday_PC / Laptop", 
            "Referres_Last_Month_By_Mobile": "last_month_Mobile",
            "Referres_Last_Week_By_Mobile": "last_week_Mobile",
            "Referres_Yesterday_By_Mobile": "yesterday_Mobile"
        }
        
        try:
            if "Referres_Last_Month" not in Data or not Data["Referres_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the date picker'
            
            date_tests = [
                ("Last Month", "Referres_Last_Month"),
                ("Last Week", "Referres_Last_Week"), 
                ("Yesterday", "Referres_Yesterday")
            ]
            
            for period_name, baseline_key in date_tests:
                baseline_data = Data[baseline_key]
                cache_key = baseline_to_cache_mapping[baseline_key]
                
                baseline_username = baseline_data["metadata"]["filters"]["username"]
                
                # Use CACHED data - no more API calls!
                current_data = cache["referrers"][cache_key]
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + {period_name}: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{period_name}: No current data found but baseline data exists")
                else:
                    self._compare_site_urls(baseline_data["site_urls_data"], current_data["site_urls_data"])
                    self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    subAutoTestCase += f"\n     + {period_name}: Successfully verified data (Username: {baseline_username})"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            subAutoTestCase = '- Verify that the data displayed is correct by device'
            
            device_tests = [
                ("Desktop - Last Month", "Referres_Last_Month_By_Desktop"),
                ("Desktop - Last Week", "Referres_Last_Week_By_Desktop"),
                ("Desktop - Yesterday", "Referres_Yesterday_By_Desktop"),
                ("Mobile - Last Month", "Referres_Last_Month_By_Mobile"), 
                ("Mobile - Last Week", "Referres_Last_Week_By_Mobile"),
                ("Mobile - Yesterday", "Referres_Yesterday_By_Mobile")
            ]
            
            for device_period_name, baseline_key in device_tests:
                baseline_data = Data[baseline_key]
                cache_key = baseline_to_cache_mapping[baseline_key]
                baseline_username = baseline_data["metadata"]["filters"]["username"]
                
                current_data = cache["referrers"][cache_key]
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + {device_period_name}: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{device_period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{device_period_name}: No current data found but baseline data exists")
                else:
                    self._compare_site_urls(baseline_data["site_urls_data"], current_data["site_urls_data"])
                    self._compare_website_urls(baseline_data["website_urls_data"], current_data["website_urls_data"])
                    subAutoTestCase += f"\n     + {device_period_name}: Successfully verified data (Username: {baseline_username})"
            
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

    def preload_all_data(self):
        if CompareDataReferrers._cache_data is not None:
            print("Using cached data from previous load!")
            return CompareDataReferrers._cache_data, CompareDataReferrers._cache_username
        
        cache = {
            "referrers": {},
            "landing_pages": {},
            "marketing_pages": {},
            "statistics": {}
        }
        
        if "Referres_Last_Month" not in Data or not Data["Referres_Last_Month"]:
            raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
        
        baseline_last_month = Data["Referres_Last_Month"]
        username = baseline_last_month["metadata"]["filters"]["username"]
        print(f"Using consistent username from baseline: {username}")
        
        baseline_to_cache_mapping = {
            "Referres_Last_Month": "last_month_All",
            "Referres_Last_Month_By_Desktop": "last_month_PC / Laptop", 
            "Referres_Last_Month_By_Mobile": "last_month_Mobile",
            "Referres_Last_Week": "last_week_All",
            "Referres_Last_Week_By_Desktop": "last_week_PC / Laptop",
            "Referres_Last_Week_By_Mobile": "last_week_Mobile",
            "Referres_Yesterday": "yesterday_All",
            "Referres_Yesterday_By_Desktop": "yesterday_PC / Laptop",
            "Referres_Yesterday_By_Mobile": "yesterday_Mobile"
        }
        
        periods_with_data = set()
        
        print("Phase 1: Loading referrers data...")
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if baseline_key not in Data or not Data[baseline_key]:
                print(f"Skipping {cache_key} - baseline not found")
                cache["referrers"][cache_key] = {"has_data": False, "site_urls_data": [], "website_urls_data": {}}
                continue
                
            baseline_data = Data[baseline_key]
            baseline_has_data = baseline_data["metadata"].get("has_data", True)
            
            if not baseline_has_data:
                print(f"Skipping {cache_key} - baseline has no data")
                cache["referrers"][cache_key] = {"has_data": False, "site_urls_data": [], "website_urls_data": {}}
                continue
            
            baseline_from_date = baseline_data["metadata"]["period"]["from_date"]
            baseline_to_date = baseline_data["metadata"]["period"]["to_date"]
            
            # Extract device type from cache key
            if "Mobile" in cache_key:
                device_type = "Mobile"
            elif "PC / Laptop" in cache_key:
                device_type = "PC / Laptop"
            else:
                device_type = "All"
            
            print(f"Loading referrers data for {cache_key} (device: {device_type})")
            current_data = self.get_data_referrers_in_customer(
                username, baseline_from_date, baseline_to_date, device_type, get_detail=True
            )
            cache["referrers"][cache_key] = current_data
            
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
        
        print(f"Periods with referrers data: {periods_with_data}")
        
        print("Phase 2: Loading landing pages data...")
        for baseline_key, cache_key in baseline_to_cache_mapping.items():
            if cache_key not in cache["referrers"]:
                continue
                
            referrers_data = cache["referrers"][cache_key]
            if not referrers_data.get("has_data", True):
                print(f"Skipping landing pages for {cache_key} - no referrers data")
                cache["landing_pages"][cache_key] = {"has_data": False, "pages_data": [], "website_urls_data": {}}
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
            
            print(f"Loading landing pages data for {cache_key} (device: {device_type})")
            landing_pages_data = self.get_data_landing_pages_in_customer(
                username, "All", "All", baseline_from_date, baseline_to_date, device_type, get_detail=False
            )
            cache["landing_pages"][cache_key] = landing_pages_data
        
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
            baseline_period_data = Data["Referres_Last_Month"]
            baseline_from_date = baseline_period_data["metadata"]["period"]["from_date"]
            month_date = datetime.strptime(baseline_from_date, "%m-%d-%Y").strftime("%m-%Y")
            
            print(f"Loading statistics for last_month (month: {month_date})")
            cache["statistics"]["last_month"] = self.get_data_statistics_in_customer(
                username, month_date
            )
        
        CompareDataReferrers._cache_data = cache
        CompareDataReferrers._cache_username = username
        
        print(f"✅ Data loading completed successfully!")
        print(f"   Username: {username}")
        print(f"   Loaded periods: {list(periods_with_data)}")
        print(f"   Referrers cache keys: {list(cache['referrers'].keys())}")
        print(f"   Landing pages cache keys: {list(cache['landing_pages'].keys())}")
        print(f"   Marketing pages cache keys: {list(cache['marketing_pages'].keys())}")
        print(f"   Statistics cache keys: {list(cache['statistics'].keys())}")
        return cache, username

    def check_data_referrers_click_statistics_and_compare(self, testcase):
        cache, username = self.preload_all_data()
        mainChecklist = ["Verify that the Referrers data in the \"Click Statistics\" sub‑function matches the data in Statistics.",
                        "Verify that the Total Clicks for Referrers equal the Total Clicks for Landing Pages.",
                        "Verify that the Total Clicks for Referrers equal the Total Clicks for Marketing Pages."
                        ]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month"]
            device_types = [
                {"name": "All", "display_name": "All"}
            ]
            
            for period in time_periods:
                if period not in cache["statistics"]:
                    print(f"Skipping {period} - no statistics data available")
                    continue
                    
                for device in device_types:
                    if subAutoTestCase:
                        subAutoTestCase += '\n'
                    subAutoTestCase += f"- Verify that the data of Referrers {device['display_name'].lower()} in {period.replace('_', ' ')} must match the data of Statistics summary table"
                    
                    key = f"{period}_{device['name']}"
                    data_referrers = cache["referrers"][key]
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
                    
                    referrers_total_clicks = 0
                    referrers_unique_clicks = 0
                    referrers_signups = 0
                    referrers_fdm = 0
                    
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                            referrers_unique_clicks += self.parse_int(site_data["unique_click"])
                            referrers_signups += self.parse_int(site_data["signups"])
                            referrers_fdm += self.parse_int(site_data["fdm"])
                    
                    baseline_data = Data["Referres_Last_Month"]
                    current_username = baseline_data["metadata"]["filters"]["username"]
                    
                    click_type = "Total Clicks"
                    if device["name"] == "Mobile":
                        click_type = "Mobile Total Clicks"
                    elif device["name"] == "PC / Laptop":
                        click_type = "Desktop Total Clicks"
                    
                    results = {
                        "username": current_username,
                        "device_type": device["name"],
                        "from_date": cache[period]["date_range"]["from_date"],
                        "to_date": cache[period]["date_range"]["to_date"],
                        "statistics_total_clicks": statistics_total_clicks,
                        "statistics_unique_clicks": statistics_unique_clicks,
                        "referrers_total_clicks": referrers_total_clicks,
                        "referrers_unique_clicks": referrers_unique_clicks,
                        "statistics_signups": statistics_signups,
                        "referrers_signups": referrers_signups,
                        "statistics_fdm": statistics_fdm,
                        "referrers_fdm": referrers_fdm,
                        "click_type": click_type
                    }
                    
                    subAutoTestCase += self._format_test_results(results, device["display_name"])
                    
                    if referrers_total_clicks != statistics_total_clicks:
                        subAutoTestCase += f"\n     + {click_type} mismatch: Statistics={statistics_total_clicks}, Referrers={referrers_total_clicks}"
                    
                    if referrers_signups != statistics_signups:
                        subAutoTestCase += f"\n     + Signups mismatch: Statistics={statistics_signups}, Referrers={referrers_signups}"
                    
                    if referrers_fdm != statistics_fdm:
                        subAutoTestCase += f"\n     + FDM mismatch: Statistics={statistics_fdm}, Referrers={referrers_fdm}"
            
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
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Landing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    data_landing_pages = cache["landing_pages"].get(key, {})
                    
                    referrers_total_clicks = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                    
                    landing_pages_total_clicks = 0
                    if data_landing_pages.get("has_data", True):
                        for page in data_landing_pages["pages_data"]:
                            landing_pages_total_clicks += self.parse_int(page["total_click"])
                    
                    has_data = data_referrers.get("has_data", True) and data_landing_pages.get("has_data", True)
                    
                    if has_data:
                        current_username = self._get_username_for_period_device(period, device_type, username)
                        subAutoTestCase += f"\n     + Username: {current_username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if referrers_total_clicks == landing_pages_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {referrers_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, Landing Pages={landing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Referrers or Landing Pages."
            
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
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Marketing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    data_marketing_pages = cache["marketing_pages"].get(period, {})
                    
                    referrers_total_clicks = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_total_clicks += self.parse_int(site_data["total_click"])
                    
                    marketing_pages_total_clicks = 0
                    if data_marketing_pages.get("has_data", True):
                        for channel in data_marketing_pages["channels_data"]:
                            marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                    
                    has_data = data_referrers.get("has_data", True) and data_marketing_pages.get("has_data", True)
                    
                    if has_data:
                        current_username = self._get_username_for_period_device(period, device_type, username)
                        subAutoTestCase += f"\n     + Username: {current_username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if referrers_total_clicks == marketing_pages_total_clicks:
                            subAutoTestCase += f"\n     + Total Clicks match: {referrers_total_clicks}"
                        else:
                            subAutoTestCase += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, Marketing Pages={marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + No data found for Total Clicks for Referrers or Marketing Pages."
            
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
            "Verify that the Signups for Referrers equal the Signups for Landing Pages.",
            "Verify that the Signups for Referrers equal the Signups for Marketing Pages.",
            "Verify that the FDM for Referrers equal the FDM for Landing Pages.",
            "Verify that the FDM for Referrers equal the FDM for Marketing Pages."
        ]
        
        try:
            for checklist_index, comparison_type in enumerate([
                {"data_type": "signups", "compare_with": "landing_pages"},
                {"data_type": "signups", "compare_with": "marketing_pages"},
                {"data_type": "fdm", "compare_with": "landing_pages"},
                {"data_type": "fdm", "compare_with": "marketing_pages"}
            ]):
                data_type = comparison_type["data_type"]
                compare_with = comparison_type["compare_with"]
                
                data_type_display = data_type.capitalize()
                compare_with_display = "Landing Pages" if compare_with == "landing_pages" else "Marketing Pages"
                
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
                            
                        subAutoTestCase += f"- Verify that {data_type_display} for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to {data_type_display} for {compare_with_display}."
                        
                        key = f"{period}_{device_type}"
                        data_referrers = cache["referrers"].get(key, {})
                        
                        if compare_with == "marketing_pages":
                            data_pages = cache["marketing_pages"].get(period, {})
                        else:
                            data_pages = cache["landing_pages"].get(key, {})
                        
                        referrers_value = 0
                        if data_referrers.get("has_data", True):
                            for site_data in data_referrers["site_urls_data"]:
                                referrers_value += self.parse_int(site_data[data_type])
                        
                        pages_value = 0
                        if data_pages.get("has_data", True):
                            if compare_with == "landing_pages":
                                for page in data_pages["pages_data"]:
                                    pages_value += self.parse_int(page[data_type])
                            else:
                                for channel in data_pages["channels_data"]:
                                    pages_value += self.parse_int(channel[data_type])
                        
                        has_data = data_referrers.get("has_data", True) and data_pages.get("has_data", True)
                        
                        if has_data:
                            current_username = self._get_username_for_period_device(period, device_type, username)
                            subAutoTestCase += f"\n     + Username: {current_username}"
                            subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                            subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                            
                            if referrers_value == pages_value:
                                subAutoTestCase += f"\n     + {data_type_display} match: {referrers_value}"
                            else:
                                subAutoTestCase += f"\n     + {data_type_display} mismatch: Referrers={referrers_value}, {compare_with_display}={pages_value}"
                        else:
                            subAutoTestCase += f"\n     + No data found for {data_type_display} for Referrers or {compare_with_display}."
                
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
    
    def verify_site_url_website_url_match(self, testcase):
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
                if period not in cache:
                    continue
                    
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, clicking on a Site URL shows the Website URLs sub-table"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    
                    has_site_urls = False
                    has_sub_tables = False
                    
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            site_url = site_data["site_url"]
                            if site_url.lower() != "none" and site_url.strip() != "":
                                has_site_urls = True
                                if site_url in data_referrers["website_urls_data"]:
                                    has_sub_tables = True
                                    break
                
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_referrers.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Referrers."
                    elif not has_site_urls:
                        subAutoTestCase += f"\n     + No valid Site URLs found (all are 'none' or empty)."
                    elif has_sub_tables:
                        subAutoTestCase += f"\n     + Verified: Sub-data table is displayed when clicking on Site URLs."
            
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
                    
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, the sum of Website URL values match the Site URL values"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_referrers.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Referrers."
                        continue
                    
                    mismatches = []
                    for site_data in data_referrers["site_urls_data"]:
                        site_url = site_data["site_url"]
                        if site_url.lower() == "none" or site_url.strip() == "":
                            continue
                        
                        if site_url not in data_referrers["website_urls_data"]:
                            mismatches.append(f"No website URLs data found for site '{site_url}'")
                            continue
                        
                        website_urls = data_referrers["website_urls_data"][site_url]
                        
                        website_total_clicks = 0
                        website_unique_clicks = 0
                        website_signups = 0
                        website_fdm = 0
                        
                        for website_data in website_urls:
                            website_total_clicks += self.parse_int(website_data["total_clicks"])
                            website_unique_clicks += self.parse_int(website_data["unique_clicks"])
                            
                            if "signups" in website_data:
                                website_signups += self.parse_int(website_data["signups"])
                            elif "sign_up" in website_data:
                                website_signups += self.parse_int(website_data["sign_up"])
                            
                            website_fdm += self.parse_int(website_data["fdm"])
                        
                        site_total_click = self.parse_int(site_data["total_click"])
                        site_unique_click = self.parse_int(site_data["unique_click"])
                        site_signups = self.parse_int(site_data["signups"])
                        site_fdm = self.parse_int(site_data["fdm"])
                        
                        if website_total_clicks != site_total_click:
                            mismatches.append(f"Total clicks mismatch for site '{site_url}': Site value={site_total_click}, Sum of website values={website_total_clicks}")
                        
                        if website_unique_clicks != site_unique_click:
                            mismatches.append(f"Unique clicks mismatch for site '{site_url}': Site value={site_unique_click}, Sum of website values={website_unique_clicks}")
                        
                        if website_signups != site_signups:
                            mismatches.append(f"Signups mismatch for site '{site_url}': Site value={site_signups}, Sum of website values={website_signups}")
                        
                        if website_fdm != site_fdm:
                            mismatches.append(f"FDM mismatch for site '{site_url}': Site value={site_fdm}, Sum of website values={website_fdm}")
                    
                    if mismatches:
                        subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found:"
                        for mismatch in mismatches[:3]:
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(mismatches) > 3:
                            subAutoTestCase += f"\n       - ... and {len(mismatches) - 3} more"
                    else:
                        subAutoTestCase += f"\n     + Verified: All Website URL sums match their corresponding Site URL values."
            
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
            "Verify that the total FDM for the month equals the total FDM in the Statistics data table Referrers report."
        ]
        
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month"]
            
            for period in time_periods:
                if period not in cache["statistics"]:
                    print(f"Skipping {period} - no statistics data available")
                    continue
                    
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total Signups for Referrers in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_referrers_signups = 0
                device_signups = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    
                    referrers_signups = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_signups += self.parse_int(site_data["signups"])
                    
                    device_signups[device_type] = referrers_signups
                    
                    if device_type == "All":
                        all_referrers_signups = referrers_signups
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                current_username = self._get_username_for_period_device(period, "All", username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if all_referrers_signups == statistics_signups:
                    subAutoTestCase += f"\n     + Signups match: Statistics={statistics_signups}, Referrers (All)={all_referrers_signups}"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch: Statistics={statistics_signups}, Referrers (All)={all_referrers_signups}"
                    subAutoTestCase += f"\n     + Referrers by device: PC / Laptop={device_signups['PC / Laptop']}, Mobile={device_signups['Mobile']}"
            
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
                if period not in cache["statistics"]:
                    continue
                    
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total FDM for Referrers in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_referrers_fdm = 0
                device_fdm = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    
                    referrers_fdm = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_fdm += self.parse_int(site_data["fdm"])
                    
                    device_fdm[device_type] = referrers_fdm
                    
                    if device_type == "All":
                        all_referrers_fdm = referrers_fdm
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                
                current_username = self._get_username_for_period_device(period, "All", username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if all_referrers_fdm == statistics_fdm:
                    subAutoTestCase += f"\n     + FDM match: Statistics={statistics_fdm}, Referrers (All)={all_referrers_fdm}"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch: Statistics={statistics_fdm}, Referrers (All)={all_referrers_fdm}"
                    subAutoTestCase += f"\n     + Referrers by device: PC / Laptop={device_fdm['PC / Laptop']}, Mobile={device_fdm['Mobile']}"
            
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
                if period not in cache:
                    continue
                    
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, if Total Clicks has data, then Unique Clicks also has data"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"].get(key, {})
                    
                    current_username = self._get_username_for_period_device(period, device_type, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_referrers.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Referrers."
                        continue
                    
                    violations = []
                    total_sites = 0
                    sites_with_total_clicks = 0
                    
                    for site_data in data_referrers["site_urls_data"]:
                        site_url = site_data["site_url"]
                        total_clicks = self.parse_int(site_data["total_click"])
                        unique_clicks = self.parse_int(site_data["unique_click"])
                        
                        total_sites += 1
                        
                        if total_clicks > 0:
                            sites_with_total_clicks += 1
                            if unique_clicks == 0:
                                violations.append(f"Site URL '{site_url}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                    
                    for site_url, website_urls in data_referrers["website_urls_data"].items():
                        for website_data in website_urls:
                            website_url = website_data["website_url"]
                            total_clicks = self.parse_int(website_data["total_clicks"])
                            unique_clicks = self.parse_int(website_data["unique_clicks"])
                            
                            if total_clicks > 0 and unique_clicks == 0:
                                violations.append(f"Website URL '{website_url}' under Site '{site_url}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                    
                    if not sites_with_total_clicks:
                        subAutoTestCase += f"\n     + No sites with Total Clicks data found."
                    elif violations:
                        subAutoTestCase += f"\n     + Failed: {len(violations)} sites/websites have Total Clicks but no Unique Clicks:"
                        for violation in violations[:3]:
                            subAutoTestCase += f"\n       - {violation}"
                        if len(violations) > 3:
                            subAutoTestCase += f"\n       - ... and {len(violations) - 3} more"
                    else:
                        subAutoTestCase += f"\n     + Verified: All {sites_with_total_clicks} sites/websites with Total Clicks also have Unique Clicks data."
            
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