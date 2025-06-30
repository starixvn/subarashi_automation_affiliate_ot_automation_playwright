from config.constants.settings import *
env = ENVIRONMENT
import random
from datetime import datetime, timedelta

from src.actions.common.action_common import Common
from src.actions.common.get_data_on_function.get_data_customer import GetDataCustomer
from src.test_data.common.data_common import *
from src.actions.common.get_data_on_function.get_data_player import GetDataPlayer

from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_month import DataMarketingPagesLastMonth
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_last_week import DataMarketingPagesLastWeek
from src.test_data.common.data_click_statistics.data_marketing_pages.data_marketing_pages_yesterday import DataMarketingPagesYesterday

Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
    "Marketing_Pages_Last_Month": DataMarketingPagesLastMonth.data_marketing_pages_last_month,
    "Marketing_Pages_Last_Week": DataMarketingPagesLastWeek.data_marketing_pages_last_week,
    "Marketing_Pages_Yesterday": DataMarketingPagesYesterday.data_marketing_pages_yesterday,
}
Checklist_Sheet_Name = "Compare_Data_Clickstatistics"

class CompareDataMarketingPage(GetDataCustomer):
    _cache_data = None
    _cache_username = None
    
    def __init__(self):
        super().__init__()
        self.get_data_customer = GetDataCustomer()

    @staticmethod
    def clear_cache():
        Common.clear_cache_for_class(CompareDataMarketingPage)

    def _compare_channels_data(self, baseline_channels_data, current_channels_data):
        language_mapping = Common.get_language_mapping()
        
        mismatches = []
        
        if len(baseline_channels_data) != len(current_channels_data):
            mismatches.append(f"Number of channels mismatch. Baseline: {len(baseline_channels_data)}, Current: {len(current_channels_data)}")
        
        for baseline_channel_data in baseline_channels_data:
            channel_name = baseline_channel_data.get("channel_name") or ""
            language = baseline_channel_data.get("language") or ""
            language_lower = language.lower()
            
            if language_lower in language_mapping:
                language_code = language_mapping[language_lower]
            else:
                language_code = language_lower
            
            channel_found = False
            for current_channel in current_channels_data:
                current_language = current_channel.get("language") or ""
                current_language_lower = current_language.lower()
                
                if current_language_lower in language_mapping:
                    current_language_code = language_mapping[current_language_lower]
                else:
                    current_language_code = current_language_lower
                
                current_channel_name = current_channel.get("channel_name") or ""
                if current_channel_name.lower() == channel_name.lower() and current_language_code == language_code:
                    channel_found = True
                    
                    baseline_total_click = baseline_channel_data["total_click"]
                    current_total_click = current_channel["total_click"]
                    baseline_unique_click = baseline_channel_data["unique_click"]
                    current_unique_click = current_channel["unique_click"]
                    baseline_signups = baseline_channel_data["signups"]
                    current_signups = current_channel["signups"]
                    baseline_fdm = baseline_channel_data["fdm"]
                    current_fdm = current_channel["fdm"]
                    
                    if current_total_click != baseline_total_click:
                        mismatches.append(f"Total clicks mismatch for channel {channel_name} - {language}. Baseline: {baseline_total_click}, Current: {current_total_click}")
                    if current_unique_click != baseline_unique_click:
                        mismatches.append(f"Unique clicks mismatch for channel {channel_name} - {language}. Baseline: {baseline_unique_click}, Current: {current_unique_click}")
                    if current_signups != baseline_signups:
                        mismatches.append(f"Signups mismatch for channel {channel_name} - {language}. Baseline: {baseline_signups}, Current: {current_signups}")
                    if current_fdm != baseline_fdm:
                        mismatches.append(f"FDM mismatch for channel {channel_name} - {language}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                    break
            
            if not channel_found:
                mismatches.append(f"Channel '{channel_name} - {language}' not found in current data")
        
        return mismatches
    
    def _compare_channel_details(self, baseline_channel_details_data, current_channel_details_data):
        mismatches = []
        
        for channel_key, baseline_urls in baseline_channel_details_data.items():
            if channel_key and "none" in str(channel_key).lower():
                continue
            
            if channel_key not in current_channel_details_data:
                mismatches.append(f"Channel details for '{channel_key}' not found in current data")
                continue
            
            current_urls = current_channel_details_data[channel_key]
            
            if len(baseline_urls) != len(current_urls):
                mismatches.append(f"Number of URLs mismatch for channel {channel_key}. Baseline: {len(baseline_urls)}, Current: {len(current_urls)}")
            
            for baseline_url in baseline_urls:
                url_found = False
                baseline_url_value = str(baseline_url.get("url", "")).strip()
                
                is_empty_url = baseline_url_value == "" or baseline_url_value.lower() == "none"
                
                for current_url in current_urls:
                    current_url_value = str(current_url.get("url", "")).strip()
                    current_is_empty_url = current_url_value == "" or current_url_value.lower() == "none"
                    
                    url_match = False
                    if is_empty_url and current_is_empty_url:
                        url_match = True
                    elif not is_empty_url and not current_is_empty_url and current_url_value == baseline_url_value:
                        url_match = True
                    
                    if url_match:
                        url_found = True
                        
                        baseline_total_clicks = self.parse_int(baseline_url.get("total_clicks", 0))
                        current_total_clicks = self.parse_int(current_url.get("total_clicks", 0))
                        baseline_unique_clicks = self.parse_int(baseline_url.get("unique_clicks", 0))
                        current_unique_clicks = self.parse_int(current_url.get("unique_clicks", 0))
                        baseline_signups = self.parse_int(baseline_url.get("signups", 0))
                        current_signups = self.parse_int(current_url.get("signups", 0))
                        baseline_fdm = self.parse_int(baseline_url.get("fdm", 0))
                        current_fdm = self.parse_int(current_url.get("fdm", 0))
                        
                        url_identifier = baseline_url_value if baseline_url_value else f"[empty URL in channel {channel_key}]"
                        
                        if current_total_clicks != baseline_total_clicks:
                            mismatches.append(f"Total clicks mismatch for URL {url_identifier}. Baseline: {baseline_total_clicks}, Current: {current_total_clicks}")
                        if current_unique_clicks != baseline_unique_clicks:
                            mismatches.append(f"Unique clicks mismatch for URL {url_identifier}. Baseline: {baseline_unique_clicks}, Current: {current_unique_clicks}")
                        if current_signups != baseline_signups:
                            mismatches.append(f"Signups mismatch for URL {url_identifier}. Baseline: {baseline_signups}, Current: {current_signups}")
                        if current_fdm != baseline_fdm:
                            mismatches.append(f"FDM mismatch for URL {url_identifier}. Baseline: {baseline_fdm}, Current: {current_fdm}")
                        break
                
                if not url_found and not is_empty_url:
                    mismatches.append(f"URL '{baseline_url_value}' not found in current data for channel {channel_key}")
                elif not url_found and is_empty_url:
                    mismatches.append(f"Empty URL entry not found in current data for channel {channel_key}")
        
        return mismatches
    
    def parse_int(self, text):
        return Common.parse_int(text)
    
    def parse_fraction(self, text):
        return Common.parse_fraction(text)
    
    def _get_username_for_period(self, period, fallback_username):
        return Common.get_username_for_period_device(period, "All", Data, fallback_username)
    
    def _get_username(self):
        return Common.get_username()
        
    def _get_date_range(self, period):
        return Common.get_date_range(period)

    def preload_all_data(self):
        if CompareDataMarketingPage._cache_data is not None:
            return CompareDataMarketingPage._cache_data, CompareDataMarketingPage._cache_username
        
        cache = {
            "marketing_pages": {},
            "referrers": {},
            "landing_pages": {},
            "statistics": {}
        }
        
        if "Marketing_Pages_Last_Month" not in Data or not Data["Marketing_Pages_Last_Month"]:
            raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
        
        baseline_last_month = Data["Marketing_Pages_Last_Month"]
        username = baseline_last_month["metadata"]["filters"]["username"]
        
        baseline_data_map = {
            "last_month": Data["Marketing_Pages_Last_Month"],
            "last_week": Data["Marketing_Pages_Last_Week"],
            "yesterday": Data["Marketing_Pages_Yesterday"]
        }
        
        periods_with_data = set()
        
        for period in ["last_month", "last_week", "yesterday"]:
            if period not in baseline_data_map or not baseline_data_map[period]:
                cache["marketing_pages"][period] = {"has_data": False, "channels_data": [], "channel_details_data": {}}
                continue
                
            baseline_period_data = baseline_data_map[period]
            baseline_has_data = baseline_period_data["metadata"].get("has_data", True)
            
            if not baseline_has_data:
                cache["marketing_pages"][period] = {"has_data": False, "channels_data": [], "channel_details_data": {}}
                continue
            
            baseline_from_date = baseline_period_data["metadata"]["period"]["from_date"]
            baseline_to_date = baseline_period_data["metadata"]["period"]["to_date"]
            baseline_language = baseline_period_data["metadata"]["filters"]["language"]
            baseline_include_inactive = baseline_period_data["metadata"]["filters"].get("include_inactive_tracking", False)
            
            cache[period] = {
                "date_range": {
                    "from_date": baseline_from_date,
                    "to_date": baseline_to_date
                }
            }
            
            data_marketing_pages = self.get_data_marketing_pages_in_customer(
                username, baseline_language, baseline_from_date, baseline_to_date, baseline_include_inactive, get_detail=True
            )
            cache["marketing_pages"][period] = data_marketing_pages
            
            if data_marketing_pages.get("has_data", True):
                periods_with_data.add(period)
        
        for period in periods_with_data:
            period_info = cache[period]
            baseline_from_date = period_info["date_range"]["from_date"]
            baseline_to_date = period_info["date_range"]["to_date"]
            
            data_referrers = self.get_data_referrers_in_customer(
                username, baseline_from_date, baseline_to_date, "All", get_detail=False
            )
            cache["referrers"][period] = data_referrers
        
        for period in periods_with_data:
            period_info = cache[period]
            baseline_from_date = period_info["date_range"]["from_date"]
            baseline_to_date = period_info["date_range"]["to_date"]
            
            data_landing_pages = self.get_data_landing_pages_in_customer(
                username, "All", "All", baseline_from_date, baseline_to_date, "All", get_detail=False
            )
            cache["landing_pages"][period] = data_landing_pages

        if "last_month" in periods_with_data:
            baseline_period_data = Data["Marketing_Pages_Last_Month"]
            baseline_from_date = baseline_period_data["metadata"]["period"]["from_date"]
            month_date = datetime.strptime(baseline_from_date, "%m-%d-%Y").strftime("%m-%Y")
            
            cache["statistics"]["last_month"] = self.get_data_statistics_in_customer(
                username, month_date
            )
        
        CompareDataMarketingPage._cache_data = cache
        CompareDataMarketingPage._cache_username = username
        return cache, username

    def check_data_marketing_pages_filter_by_date_language(self, testcase):
        subAutoTestCase = ''
        mainChecklist = [
            "Verify that the Marketing Page data displays correctly according to the date picker.",
            "Verify that the Marketing Page data displays correctly according to the Language filter."
        ]
        indexChl = 0
        try:
            if "Marketing_Pages_Last_Month" not in Data or not Data["Marketing_Pages_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
                
            subAutoTestCase = '- Verify that the data displayed is correct according to the date picker'
            
            date_ranges = {
                "Last Month": Data["Marketing_Pages_Last_Month"],
                "Last Week": Data["Marketing_Pages_Last_Week"],
                "Yesterday": Data["Marketing_Pages_Yesterday"]
            }
            
            for period_name, baseline_data in date_ranges.items():
                username = baseline_data["metadata"]["filters"]["username"]
                language = baseline_data["metadata"]["filters"]["language"]
                from_date = baseline_data["metadata"]["period"]["from_date"]
                to_date = baseline_data["metadata"]["period"]["to_date"]
                include_inactive = baseline_data["metadata"]["filters"].get("include_inactive_tracking", False)
                
                current_data = self.get_data_marketing_pages_in_customer(username, language, from_date, to_date, include_inactive)
                
                baseline_has_data = baseline_data["metadata"].get("has_data", True)
                current_has_data = current_data.get("has_data", True)
                
                if not baseline_has_data and not current_has_data:
                    subAutoTestCase += f"\n     + {period_name}: No data expected - verified no data is present"
                elif not baseline_has_data and current_has_data:
                    raise Exception(f"{period_name}: Baseline data has no results but current query returned data. This suggests a data inconsistency.")
                elif baseline_has_data and not current_has_data:
                    raise Exception(f"{period_name}: No current data found for user {username} from {from_date} to {to_date} with language {language}, but baseline data exists")
                else:
                    normalized_baseline_channels = self._normalize_channels_data_for_comparison(baseline_data["channels_data"])
                    normalized_current_channels = self._normalize_channels_data_for_comparison(current_data["channels_data"])
                    normalized_baseline_details = self._normalize_channel_details_for_comparison(baseline_data["channel_details_data"])
                    normalized_current_details = self._normalize_channel_details_for_comparison(current_data["channel_details_data"])
                    
                    channel_mismatches = self._compare_channels_data(normalized_baseline_channels, normalized_current_channels)
                    detail_mismatches = self._compare_channel_details(normalized_baseline_details, normalized_current_details)
                    
                    all_mismatches = channel_mismatches + detail_mismatches
                    
                    if all_mismatches:
                        subAutoTestCase += f"\n     + {period_name}: Data mismatches found ({len(all_mismatches)} issues) for user {username}"
                        for i, mismatch in enumerate(all_mismatches):
                            subAutoTestCase += f"\n       - {mismatch}"
                    else:
                        subAutoTestCase += f"\n     + {period_name}: Successfully verified data with date range {from_date} to {to_date}"
            
            self.utils.update_result_to_ggsheet(Data["TestCase_spread_sheet_id"], mainChecklist[indexChl], testcase, subAutoTestCase, Data["TestCase_Auto_Status"][0], sheet_name=Checklist_Sheet_Name)
            indexChl += 1
            subAutoTestCase = ''
            
            subAutoTestCase = '- Verify that the data displayed is correct according to the Language filter'
            
            baseline_data = Data["Marketing_Pages_Last_Month"]
            username = baseline_data["metadata"]["filters"]["username"]
            from_date = baseline_data["metadata"]["period"]["from_date"]
            to_date = baseline_data["metadata"]["period"]["to_date"]
            include_inactive = baseline_data["metadata"]["filters"].get("include_inactive_tracking", False)
            
            languages = set()
            for channel_key, url_details in baseline_data["channel_details_data"].items():
                for url_data in url_details:
                    url_language = url_data.get("language") or ""
                    if url_language and url_language.lower() not in ["none", "-", "null"] and url_language.strip() != "":
                        languages.add(url_language)
            
            if languages:
                test_language = next(iter(languages))
                subAutoTestCase += f"\n     + Testing language filter with: '{test_language}'"
                
                current_data_filtered = self.get_data_marketing_pages_in_customer(username, test_language, from_date, to_date, include_inactive)
                
                if not current_data_filtered.get("has_data", True):
                    subAutoTestCase += f"\n     + No data found when filtering for language '{test_language}'"
                else:
                    language_verification_passed = True
                    mismatched_languages = []
                    total_urls_checked = 0
                    matching_urls = 0
                    
                    for channel_key, url_details in current_data_filtered["channel_details_data"].items():
                        for url_data in url_details:
                            total_urls_checked += 1
                            url_language = url_data.get("language") or ""
                            
                            if url_language and url_language.lower() not in ["none", "-", "null"] and url_language != "":
                                if url_language.lower() == (test_language or "").lower():
                                    matching_urls += 1
                                else:
                                    language_verification_passed = False
                                    mismatched_languages.append(f"URL '{url_data.get('url', '')}' has language '{url_language}' instead of '{test_language}'")
                            else:
                                matching_urls += 1
                    
                    if language_verification_passed:
                        subAutoTestCase += f"\n     + Language filter verification passed: Found {matching_urls}/{total_urls_checked} URLs with correct language filter"
                        
                        baseline_language_data = self._extract_baseline_language_data(baseline_data, test_language)
                        if baseline_language_data:
                            filter_comparison_result = self._compare_language_filtered_data(baseline_language_data, current_data_filtered)
                            if filter_comparison_result:
                                subAutoTestCase += f"\n     + Language filter data comparison: {filter_comparison_result}"
                            else:
                                subAutoTestCase += f"\n     + Successfully verified: Language filtered data matches expected baseline structure"
                        else:
                            subAutoTestCase += f"\n     + Note: No baseline data found for language '{test_language}' to compare against"
                    else:
                        subAutoTestCase += f"\n     + Language filter verification failed: Found {len(mismatched_languages)} mismatched languages"
                        for mismatch in mismatched_languages[:5]:  # Show first 5 mismatches
                            subAutoTestCase += f"\n       - {mismatch}"
                        if len(mismatched_languages) > 5:
                            subAutoTestCase += f"\n       - ... and {len(mismatched_languages) - 5} more mismatches"
            else:
                subAutoTestCase += "\n     + No valid language found in baseline data to test the filter"
            
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

    def _normalize_channels_data_for_comparison(self, channels_data):
        normalized = []
        for channel in channels_data:
            normalized_channel = {
                "channel_name": channel["channel_name"],
                "language": channel["language"],
                "total_click": self.parse_int(channel["total_click"]),
                "unique_click": self.parse_int(channel["unique_click"]),
                "signups": self.parse_int(channel["signups"]),
                "fdm": self.parse_int(channel["fdm"])
            }
            normalized.append(normalized_channel)
        return normalized

    def _normalize_channel_details_for_comparison(self, channel_details_data):
        normalized = {}
        
        for channel_key, url_details in channel_details_data.items():
            if " - " in channel_key:
                parts = channel_key.split(" - ", 1)
                if parts[0].isdigit():
                    normalized_key = channel_key
                else:
                    normalized_key = channel_key
            else:
                normalized_key = channel_key
            
            normalized_urls = []
            for url_data in url_details:
                normalized_url = {
                    "url": url_data.get("url", ""),
                    "language": url_data.get("language", ""),
                    "total_clicks": self.parse_int(url_data.get("total_clicks", 0)),
                    "unique_clicks": self.parse_int(url_data.get("unique_clicks", 0)),
                    "signups": self.parse_int(url_data.get("signups", 0)),
                    "fdm": self.parse_int(url_data.get("fdm", 0))
                }
                normalized_urls.append(normalized_url)
            
            normalized[normalized_key] = normalized_urls
        
        return normalized

    def _extract_baseline_language_data(self, baseline_data, target_language):
        language_data = {
            "channels_data": [],
            "channel_details_data": {}
        }
        
        if target_language is None:
            target_language = ""
        
        for channel in baseline_data["channels_data"]:
            channel_name = channel["channel_name"]
            channel_language = channel.get("language") or ""
            
            channel_key_candidates = [
                f"1 - {channel_name}",
                f"2 - {channel_name}",
                f"{channel_name} - {channel_language}" if channel_language else f"{channel_name}",
                f"{channel_name} - {target_language}" if target_language else f"{channel_name}"
            ]
            
            has_target_language = False
            for key_candidate in channel_key_candidates:
                if key_candidate in baseline_data["channel_details_data"]:
                    for url_data in baseline_data["channel_details_data"][key_candidate]:
                        url_language = url_data.get("language") or ""
                        if url_language.lower() == target_language.lower():
                            has_target_language = True
                            break
                    if has_target_language:
                        break
            
            if has_target_language:
                language_data["channels_data"].append(channel)
        
        for channel_key, url_details in baseline_data["channel_details_data"].items():
            filtered_urls = []
            for url_data in url_details:
                url_language = url_data.get("language") or ""
                if url_language.lower() == target_language.lower():
                    filtered_urls.append(url_data)
            
            if filtered_urls:
                language_data["channel_details_data"][channel_key] = filtered_urls
        
        return language_data if language_data["channels_data"] or language_data["channel_details_data"] else None

    def _compare_language_filtered_data(self, baseline_language_data, current_filtered_data):
        issues = []
        
        baseline_url_count = sum(len(urls) for urls in baseline_language_data["channel_details_data"].values())
        current_url_count = sum(len(urls) for urls in current_filtered_data.get("channel_details_data", {}).values())
        
        if baseline_url_count != current_url_count:
            issues.append(f"URL count mismatch - Baseline: {baseline_url_count}, Current: {current_url_count}")
        
        baseline_total_clicks = sum(self.parse_int(ch["total_click"]) for ch in baseline_language_data["channels_data"])
        current_total_clicks = sum(self.parse_int(ch["total_click"]) for ch in current_filtered_data.get("channels_data", []))
        
        if baseline_total_clicks != current_total_clicks:
            issues.append(f"Total clicks mismatch - Baseline: {baseline_total_clicks}, Current: {current_total_clicks}")
        
        return "; ".join(issues) if issues else None

    def check_data_marketing_pages_collapsed_expanded_match(self, testcase):
        subAutoTestCase = '- Verify that the sum of the collapsed data equals the data in the expanded section'
        mainChecklist = ["Verify that the sum of the collapsed data equals the data in the expanded section."]
        indexChl = 0
        
        try:
            if "Marketing_Pages_Last_Month" not in Data or not Data["Marketing_Pages_Last_Month"]:
                raise Exception("Baseline data not found. Please run the job to collect baseline data first.")
            
            baseline_data_map = {
                "Last Month": Data["Marketing_Pages_Last_Month"],
                "Last Week": Data["Marketing_Pages_Last_Week"],
                "Yesterday": Data["Marketing_Pages_Yesterday"]
            }
            
            for period_name, baseline_data in baseline_data_map.items():
                if not baseline_data or not baseline_data.get("metadata", {}).get("has_data", True):
                    continue
                    
                if subAutoTestCase and not subAutoTestCase.endswith('section'):
                    subAutoTestCase += '\n\n'
                
                period_lower = period_name.lower().replace(" ", "_")
                subAutoTestCase += f"- Verify for {period_lower} that channel totals match the sum of their detail URLs"
                
                username = baseline_data["metadata"]["filters"]["username"]
                from_date = baseline_data["metadata"]["period"]["from_date"]
                to_date = baseline_data["metadata"]["period"]["to_date"]
                
                subAutoTestCase += f"\n     + Username: {username}"
                subAutoTestCase += f"\n     + From Date: {from_date}"
                subAutoTestCase += f"\n     + To Date: {to_date}"
                
                mismatches = []
                
                for channel_data in baseline_data["channels_data"]:
                    channel_name = channel_data.get("channel_name") or ""
                    
                    matching_channel_key = None
                    for detail_key in baseline_data["channel_details_data"].keys():
                        if detail_key and detail_key.endswith(f" - {channel_name}"):
                            matching_channel_key = detail_key
                            break
                    
                    if not matching_channel_key:
                        for detail_key in baseline_data["channel_details_data"].keys():
                            if channel_name and detail_key and channel_name.lower() in str(detail_key).lower():
                                matching_channel_key = detail_key
                                break
                    
                    if not matching_channel_key:
                        mismatches.append(f"Channel details not found for channel '{channel_name}'. Available keys: {list(baseline_data['channel_details_data'].keys())}")
                        continue
                    
                    channel_details = baseline_data["channel_details_data"][matching_channel_key]
                    
                    if not channel_details:
                        mismatches.append(f"Channel '{channel_name}' (key: {matching_channel_key}) has empty detail data")
                        continue
                    
                    detail_total_clicks = 0
                    detail_unique_clicks = 0
                    detail_signups = 0
                    detail_fdm = 0
                    
                    url_count = 0
                    for url_data in channel_details:
                        url_count += 1
                        detail_total_clicks += self.parse_int(url_data.get("total_clicks", 0))
                        detail_unique_clicks += self.parse_int(url_data.get("unique_clicks", 0))
                        detail_signups += self.parse_int(url_data.get("signups", 0))
                        detail_fdm += self.parse_int(url_data.get("fdm", 0))
                    
                    channel_total_click = self.parse_int(channel_data["total_click"])
                    channel_unique_click = self.parse_int(channel_data["unique_click"])
                    channel_signups = self.parse_int(channel_data["signups"])
                    channel_fdm = self.parse_int(channel_data["fdm"])
                    
                    debug_info = f"[DEBUG] Channel '{channel_name}' (key: {matching_channel_key}): {url_count} URLs found. "
                    debug_info += f"Channel totals: TC={channel_total_click}, UC={channel_unique_click}, S={channel_signups}, F={channel_fdm}. "
                    debug_info += f"Sum of details: TC={detail_total_clicks}, UC={detail_unique_clicks}, S={detail_signups}, F={detail_fdm}"
                    
                    if detail_total_clicks != channel_total_click:
                        mismatches.append(f"Total clicks mismatch for channel '{channel_name}': Channel={channel_total_click}, Sum of details={detail_total_clicks}. {debug_info}")
                    
                    if detail_unique_clicks != channel_unique_click:
                        mismatches.append(f"Unique clicks mismatch for channel '{channel_name}': Channel={channel_unique_click}, Sum of details={detail_unique_clicks}. {debug_info}")
                    
                    if detail_signups != channel_signups:
                        mismatches.append(f"Signups mismatch for channel '{channel_name}': Channel={channel_signups}, Sum of details={detail_signups}. {debug_info}")
                    
                    if detail_fdm != channel_fdm:
                        mismatches.append(f"FDM mismatch for channel '{channel_name}': Channel={channel_fdm}, Sum of details={detail_fdm}. {debug_info}")
                
                if mismatches:
                    subAutoTestCase += f"\n     + Failed: {len(mismatches)} mismatches found:"
                    for mismatch in mismatches:
                        subAutoTestCase += f"\n       - {mismatch}"
                else:
                    subAutoTestCase += f"\n     + Verified: All channel totals match the sum of their detail URLs."
            
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

    def check_data_marketing_pages_click_statistics_compare(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Referrers.",
            "Verify that the Total Clicks on the Marketing Page equal the Total Clicks of Landing Pages."
        ]
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if period not in cache:
                    continue
                    
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                    
                subAutoTestCase += f"- Verify that Total Clicks for Marketing Pages {period_display} are equal to Total Clicks for Referrers."
                
                data_marketing_pages = cache["marketing_pages"][period]
                data_referrers = cache["referrers"].get(period, {"has_data": False})
                
                marketing_pages_total_clicks = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                
                referrers_total_clicks = 0
                if data_referrers.get("has_data", True):
                    for site_data in data_referrers["site_urls_data"]:
                        referrers_total_clicks += self.parse_int(site_data["total_click"])
                
                has_data = data_marketing_pages.get("has_data", True) and data_referrers.get("has_data", True)
                
                if has_data:
                    current_username = self._get_username_for_period(period, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if marketing_pages_total_clicks == referrers_total_clicks:
                        subAutoTestCase += f"\n     + Total Clicks match: {marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + Total Clicks mismatch: Marketing Pages={marketing_pages_total_clicks}, Referrers={referrers_total_clicks}"
                else:
                    subAutoTestCase += f"\n     + No data found for Total Clicks for Marketing Pages or Referrers."
            
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
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                    
                subAutoTestCase += f"- Verify that Total Clicks for Marketing Pages {period_display} are equal to Total Clicks for Landing Pages."
                
                data_marketing_pages = cache["marketing_pages"][period]
                data_landing_pages = cache["landing_pages"].get(period, {"has_data": False})
                
                marketing_pages_total_clicks = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_total_clicks += self.parse_int(channel["total_click"])
                
                landing_pages_total_clicks = 0
                if data_landing_pages.get("has_data", True):
                    for page_data in data_landing_pages["pages_data"]:
                        landing_pages_total_clicks += self.parse_int(page_data["total_click"])
                
                has_data = data_marketing_pages.get("has_data", True) and data_landing_pages.get("has_data", True)
                
                if has_data:
                    current_username = self._get_username_for_period(period, username)
                    subAutoTestCase += f"\n     + Username: {current_username}"
                    subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                    subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                    
                    if marketing_pages_total_clicks == landing_pages_total_clicks:
                        subAutoTestCase += f"\n     + Total Clicks match: {marketing_pages_total_clicks}"
                    else:
                        subAutoTestCase += f"\n     + Total Clicks mismatch: Marketing Pages={marketing_pages_total_clicks}, Landing Pages={landing_pages_total_clicks}"
                else:
                    subAutoTestCase += f"\n     + No data found for Total Clicks for Marketing Pages or Landing Pages."
            
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
            "Verify that the Signups on the Marketing Page equal the Signups of Referrers.",
            "Verify that the Signups on the Marketing Page equal the Signups of Landing Pages.",
            "Verify that the FDM on the Marketing Page equals the FDM of Referrers.",
            "Verify that the FDM on the Marketing Page equals the FDM of Landing Pages."
        ]
        
        try:
            for checklist_index, comparison_type in enumerate([
                {"data_type": "signups", "compare_with": "referrers"},
                {"data_type": "signups", "compare_with": "landing_pages"},
                {"data_type": "fdm", "compare_with": "referrers"},
                {"data_type": "fdm", "compare_with": "landing_pages"}
            ]):
                data_type = comparison_type["data_type"]
                compare_with = comparison_type["compare_with"]
                
                data_type_display = data_type.capitalize()
                compare_with_display = "Referrers" if compare_with == "referrers" else "Landing Pages"
                
                subAutoTestCase = ''
                periods = ["last_month", "last_week", "yesterday"]
                
                for period in periods:
                    if period not in cache:
                        continue
                        
                    period_display = period.replace("_", " ")
                    
                    if subAutoTestCase:
                        subAutoTestCase += '\n\n'
                        
                    subAutoTestCase += f"- Verify that {data_type_display} for Marketing Pages {period_display} are equal to {data_type_display} for {compare_with_display}."
                    
                    data_marketing_pages = cache["marketing_pages"][period]
                    
                    data_compare = cache[compare_with].get(period, {"has_data": False})
                    
                    marketing_pages_value = 0
                    if data_marketing_pages.get("has_data", True):
                        for channel in data_marketing_pages["channels_data"]:
                            marketing_pages_value += self.parse_int(channel[data_type])
                    
                    compare_value = 0
                    if data_compare.get("has_data", True):
                        if compare_with == "referrers":
                            for site_data in data_compare["site_urls_data"]:
                                compare_value += self.parse_int(site_data[data_type])
                        else:
                            for page_data in data_compare["pages_data"]:
                                compare_value += self.parse_int(page_data[data_type])
                    
                    has_data = data_marketing_pages.get("has_data", True) and data_compare.get("has_data", True)
                    
                    if has_data:
                        current_username = self._get_username_for_period(period, username)
                        subAutoTestCase += f"\n     + Username: {current_username}"
                        subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                        subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                        
                        if marketing_pages_value == compare_value:
                            subAutoTestCase += f"\n     + {data_type_display} match: {marketing_pages_value}"
                        else:
                            subAutoTestCase += f"\n     + {data_type_display} mismatch: Marketing Pages={marketing_pages_value}, {compare_with_display}={compare_value}"
                    else:
                        subAutoTestCase += f"\n     + No data found for {data_type_display} for Marketing Pages or {compare_with_display}."
                
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

    def verify_signups_fdm_statistics_match(self, testcase):
        cache, username = self.preload_all_data()
        
        mainChecklist = [
            "Verify that the total Signups for the month equal the total Signups in the Statistics data table.",
            "Verify that the total FDM for the month equals the total FDM in the Statistics data table."
        ]
        
        indexChl = 0
        
        try:
            subAutoTestCase = ''
            time_periods = ["last_month"]
            
            for period in time_periods:
                if period not in cache["statistics"]:
                    continue
                    
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that total Signups for Marketing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                data_marketing_pages = cache["marketing_pages"][period]
                
                marketing_pages_signups = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_signups += self.parse_int(channel["signups"])
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_signups = self.parse_int(new_signups_fdm[0])
                
                current_username = self._get_username_for_period(period, username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if marketing_pages_signups == statistics_signups:
                    subAutoTestCase += f"\n     + Signups match: Statistics={statistics_signups}, Marketing Pages={marketing_pages_signups}"
                else:
                    subAutoTestCase += f"\n     + Signups mismatch: Statistics={statistics_signups}, Marketing Pages={marketing_pages_signups}"
            
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
                
                subAutoTestCase += f"- Verify that total FDM for Marketing Pages in {period_display} match the Statistics data table"
                
                data_statistics = cache["statistics"][period]
                data_marketing_pages = cache["marketing_pages"][period]
                
                marketing_pages_fdm = 0
                if data_marketing_pages.get("has_data", True):
                    for channel in data_marketing_pages["channels_data"]:
                        marketing_pages_fdm += self.parse_int(channel["fdm"])
                
                new_signups_fdm = str(data_statistics["new_signups_month"]).split('/')
                statistics_fdm = self.parse_int(new_signups_fdm[1]) if len(new_signups_fdm) > 1 else 0
                
                current_username = self._get_username_for_period(period, username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if marketing_pages_fdm == statistics_fdm:
                    subAutoTestCase += f"\n     + FDM match: Statistics={statistics_fdm}, Marketing Pages={marketing_pages_fdm}"
                else:
                    subAutoTestCase += f"\n     + FDM mismatch: Statistics={statistics_fdm}, Marketing Pages={marketing_pages_fdm}"
            
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
            "Verify that if there is data in the Total Clicks column, the Unique Click column also contains data."
        ]
        
        indexChl = 0
        subAutoTestCase = ''
        
        try:
            periods = ["last_month", "last_week", "yesterday"]
            
            for period in periods:
                if period not in cache:
                    continue
                    
                period_display = period.replace("_", " ")
                
                if subAutoTestCase:
                    subAutoTestCase += '\n\n'
                
                subAutoTestCase += f"- Verify that for Marketing Pages {period_display}, if Total Clicks has data, then Unique Clicks also has data"
                
                data_marketing_pages = cache["marketing_pages"][period]
                
                current_username = self._get_username_for_period(period, username)
                subAutoTestCase += f"\n     + Username: {current_username}"
                subAutoTestCase += f"\n     + From Date: {cache[period]['date_range']['from_date']}"
                subAutoTestCase += f"\n     + To Date: {cache[period]['date_range']['to_date']}"
                
                if not data_marketing_pages.get("has_data", True):
                    subAutoTestCase += f"\n     + No data found for Marketing Pages."
                    continue
                
                violations = []
                total_channels = 0
                channels_with_total_clicks = 0
                
                for channel_data in data_marketing_pages["channels_data"]:
                    channel_name = channel_data["channel_name"]
                    language = channel_data["language"]
                    channel_key = f"{channel_name} - {language}"
                    total_clicks = self.parse_int(channel_data["total_click"])
                    unique_clicks = self.parse_int(channel_data["unique_click"])
                    
                    total_channels += 1
                    
                    if total_clicks > 0:
                        channels_with_total_clicks += 1
                        if unique_clicks == 0:
                            violations.append(f"Channel '{channel_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                
                for channel_key, url_details in data_marketing_pages["channel_details_data"].items():
                    for url_data in url_details:
                        url = url_data["url"]
                        total_clicks = self.parse_int(url_data["total_clicks"])
                        unique_clicks = self.parse_int(url_data["unique_clicks"])
                        
                        if total_clicks > 0 and unique_clicks == 0:
                            violations.append(f"URL '{url}' under Channel '{channel_key}' has Total Clicks ({total_clicks}) but no Unique Clicks")
                
                if not channels_with_total_clicks:
                    subAutoTestCase += f"\n     + No channels with Total Clicks data found."
                elif violations:
                    subAutoTestCase += f"\n     + Failed: {len(violations)} channels/URLs have Total Clicks but no Unique Clicks:"
                    for violation in violations:
                        subAutoTestCase += f"\n       - {violation}"
                else:
                    subAutoTestCase += f"\n     + Verified: All {channels_with_total_clicks} channels/URLs with Total Clicks also have Unique Clicks data."
            
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