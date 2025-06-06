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
                        if int(current_website["sign_up"]) != baseline_website["signups"]:
                            raise Exception(f"Signups mismatch for website {baseline_website['website_url']}. Baseline: {baseline_website['signups']}, Current: {current_website['sign_up']}")
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
    
    def _compare_referrers_with_page(self, cache, username, period, device_type, page_type="landing"):
        key = f"{period}_{device_type}"
        
        data_referrers = cache["referrers"][key]
        
        referrers_total_clicks = 0
        if data_referrers.get("has_data", True):
            for site_data in data_referrers["site_urls_data"]:
                referrers_total_clicks += self.parse_int(site_data["total_click"])
        
        if page_type == "landing":
            data_pages = cache["landing_pages"][key]
            pages_name = "Landing Pages"
            
            pages_total_clicks = 0
            if data_pages.get("has_data", True):
                for page in data_pages["pages_data"]:
                    pages_total_clicks += self.parse_int(page["total_click"])
        else:
            data_pages = cache["marketing_pages"][key]
            pages_name = "Marketing Pages"
            
            pages_total_clicks = 0
            if data_pages.get("has_data", True):
                for channel in data_pages["channels_data"]:
                    pages_total_clicks += self.parse_int(channel["total_click"])
        
        has_data = data_referrers.get("has_data", True) and data_pages.get("has_data", True)
        
        result = ""
        if has_data:
            result += f"\n     + Username: {username}"
            result += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
            result += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
            
            if referrers_total_clicks == pages_total_clicks:
                result += f"\n     + Total Clicks match: {referrers_total_clicks}"
            else:
                result += f"\n     + Total Clicks mismatch: Referrers={referrers_total_clicks}, {pages_name}={pages_total_clicks}"
        else:
            result += f"\n     + No data found for Total Clicks for Referrers or {pages_name}."
        
        return result

    def _get_username(self):
        if ENVIRONMENT == "local":
            return "12BETAFF001"
        else:
            self.data_player = GetDataPlayer()
            self.data_player.referUtils(self.utils)
            top_100_data_player = self.data_player.get_top_100_data_player()
            return top_100_data_player["players_data"][random.randint(0, len(top_100_data_player["players_data"]) - 1)]["affiliate_name"]
        
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
        else:  # current_month
            first_day_current_month = today.replace(day=1)
            from_date = first_day_current_month.strftime("%m-%d-%Y")
            to_date = today.strftime("%m-%d-%Y")
            month_date = today.strftime("%m-%Y")
        
        return {
            "from_date": from_date,
            "to_date": to_date,
            "month_date": month_date
        }

    def _check_data_for_period_and_device(self, period, device_type):
        username = self._get_username()
        date_range = self._get_date_range(period)
        
        data_referrers = self.get_data_referrers_in_customer(username, date_range["from_date"], date_range["to_date"], device_type)
        data_statistics = self.get_data_statistics_in_customer(username, date_range["month_date"])
        
        new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
        statistics_signups = self.parse_int(new_signups_fdm[0])
        statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
        
        pc_tracking = self.parse_fraction(data_statistics["tracking_pc_month"])
        mobile_tracking = self.parse_fraction(data_statistics["tracking_mobile_month"])
        
        if device_type == "All":
            statistics_total_clicks = pc_tracking["total"] + mobile_tracking["total"]
            statistics_unique_clicks = pc_tracking["unique"] + mobile_tracking["unique"]
        elif device_type == "Mobile":
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
        
        mismatches = []
        
        click_type = "Total Clicks"
        if device_type == "Mobile":
            click_type = "Mobile Total Clicks"
        elif device_type == "PC / Laptop":
            click_type = "Desktop Total Clicks"
        
        if referrers_total_clicks != statistics_total_clicks:
            mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Referrers={referrers_total_clicks}")
        
        if referrers_signups != statistics_signups:
            mismatches.append(f"Signups mismatch: Statistics={statistics_signups}, Referrers={referrers_signups}")
        
        if referrers_fdm != statistics_fdm:
            mismatches.append(f"FDM mismatch: Statistics={statistics_fdm}, Referrers={referrers_fdm}")
        
        if mismatches:
            raise Exception("\n".join(mismatches))
        
        return {
            "username": username,
            "device_type": device_type,
            "from_date": date_range["from_date"],
            "to_date": date_range["to_date"],
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
                    subAutoTestCase += f"\n     + {period_name}: Successfully verified data"
            
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
                    subAutoTestCase += f"\n     + {device_period_name}: Successfully verified data"
            
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
            
        periods = ["last_month", "last_week", "yesterday", "current_month"]
        device_types = ["All", "PC / Laptop", "Mobile"]
        stats_periods = ["last_month", "current_month"]
        
        cache = {
            "referrers": {},
            "landing_pages": {},
            "marketing_pages": {},
            "statistics": {}
        }
        
        username = self._get_username()
        
        for period in periods:
            date_range = self._get_date_range(period)
            cache[period] = {
                "date_range": date_range
            }
            
            if period in stats_periods:
                cache["statistics"][period] = self.get_data_statistics_in_customer(
                    username, date_range["month_date"]
                )
            
            for device_type in device_types:
                key = f"{period}_{device_type}"
                
                data_referrers = self.get_data_referrers_in_customer(
                    username, date_range["from_date"], date_range["to_date"], device_type, get_detail=False
                )
                cache["referrers"][key] = data_referrers
                
                data_landing_pages = self.get_data_landing_pages_in_customer(
                    username, "All", "All", date_range["from_date"], date_range["to_date"], device_type, get_detail=False
                )
                cache["landing_pages"][key] = data_landing_pages

                data_marketing_pages = self.get_data_marketing_pages_in_customer(
                    username, "All", date_range["from_date"], date_range["to_date"], get_detail=False
                )
                cache["marketing_pages"][key] = data_marketing_pages
        
        CompareDataReferrers._cache_data = cache
        CompareDataReferrers._cache_username = username
        
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
            time_periods = ["last_month", "current_month"]
            device_types = [
                {"name": "All", "display_name": "All"},
                {"name": "Mobile", "display_name": "Mobile"},
                {"name": "PC / Laptop", "display_name": "Desktop"}
            ]
            
            for period in time_periods:
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
                    
                    mismatches = []
                    click_type = "Total Clicks"
                    if device["name"] == "Mobile":
                        click_type = "Mobile Total Clicks"
                    elif device["name"] == "PC / Laptop":
                        click_type = "Desktop Total Clicks"
                    
                    if referrers_total_clicks != statistics_total_clicks:
                        mismatches.append(f"{click_type} mismatch: Statistics={statistics_total_clicks}, Referrers={referrers_total_clicks}")
                    
                    if referrers_signups != statistics_signups:
                        mismatches.append(f"Signups mismatch: Statistics={statistics_signups}, Referrers={referrers_signups}")
                    
                    if referrers_fdm != statistics_fdm:
                        mismatches.append(f"FDM mismatch: Statistics={statistics_fdm}, Referrers={referrers_fdm}")
                    
                    if mismatches:
                        raise Exception("\n".join(mismatches))
                    
                    results = {
                        "username": username,
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
            periods = ["last_month", "last_week", "current_month"]
            device_types = ["All", "PC / Laptop", "Mobile"]
            
            for period in periods:
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Landing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    data_landing_pages = cache["landing_pages"][key]
                    
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
                        subAutoTestCase += f"\n     + Username: {username}"
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
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that Total Clicks for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to Total Clicks for Marketing Pages."
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    data_marketing_pages = cache["marketing_pages"][key]
                    
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
                        subAutoTestCase += f"\n     + Username: {username}"
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
                periods = ["last_month", "last_week", "current_month"]
                device_types = ["All", "PC / Laptop", "Mobile"]
                
                for period in periods:
                    for device_type in device_types:
                        device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                        period_display = period.replace("_", " ")
                        
                        if subAutoTestCase:
                            subAutoTestCase += '\n\n'
                            
                        subAutoTestCase += f"- Verify that {data_type_display} for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display} are equal to {data_type_display} for {compare_with_display}."
                        
                        key = f"{period}_{device_type}"
                        data_referrers = cache["referrers"][key]
                        data_pages = cache[compare_with][key]
                        
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
                            subAutoTestCase += f"\n     + Username: {username}"
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
        
        periods = ["last_month", "last_week", "current_month"]
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
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, clicking on a Site URL shows the Website URLs sub-table"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    
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
                
                    subAutoTestCase += f"\n     + Username: {username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if not data_referrers.get("has_data", True):
                        subAutoTestCase += f"\n     + No data found for Referrers."
                    elif not has_site_urls:
                        subAutoTestCase += f"\n     + No valid Site URLs found (all are 'none' or empty)."
                    elif has_sub_tables:
                        subAutoTestCase += f"\n     + Verified: Sub-data table is displayed when clicking on Site URLs."
                    else:
                        subAutoTestCase += f"\n     + Failed: No sub-data tables found for any Site URL."
            
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
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, the sum of Website URL values match the Site URL values"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    
                    subAutoTestCase += f"\n     + Username: {username}"
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
            time_periods = ["last_month", "current_month"]
            
            for period in time_periods:
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total Signups for Referrers in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_referrers_signups = 0
                device_signups = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    
                    referrers_signups = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_signups += self.parse_int(site_data["signups"])
                    
                    device_signups[device_type] = referrers_signups
                    
                    if device_type == "All":
                        all_referrers_signups = referrers_signups
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                subAutoTestCase += f"\n     + Username: {username}"
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
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total FDM for Referrers in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                
                all_referrers_fdm = 0
                device_fdm = {}
                
                for device_type in ["All", "PC / Laptop", "Mobile"]:
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    
                    referrers_fdm = 0
                    if data_referrers.get("has_data", True):
                        for site_data in data_referrers["site_urls_data"]:
                            referrers_fdm += self.parse_int(site_data["fdm"])
                    
                    device_fdm[device_type] = referrers_fdm
                    
                    if device_type == "All":
                        all_referrers_fdm = referrers_fdm
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                
                subAutoTestCase += f"\n     + Username: {username}"
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
            periods = ["last_month", "last_week", "current_month"]
            device_types = ["All", "PC / Laptop", "Mobile"]
            
            for period in periods:
                period_display = period.replace("_", " ")
                
                for device_type in device_types:
                    device_display = "Desktop" if device_type == "PC / Laptop" else device_type
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                    
                    subAutoTestCase += f"- Verify that for Referrers {period_display} {'' if device_type == 'All' else 'by ' + device_display}, if Total Clicks has data, then Unique Clicks also has data"
                    
                    key = f"{period}_{device_type}"
                    data_referrers = cache["referrers"][key]
                    
                    subAutoTestCase += f"\n     + Username: {username}"
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