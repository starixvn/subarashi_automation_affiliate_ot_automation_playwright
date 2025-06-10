REFERRERS_API = "/Portal/UserPanel/Referrers/GetReferrersList"
REFERRERS_DETAILS_API = "/Portal/UserPanel/Referrers/GetWebsiteUrlList"

DEVICE_TYPE_MAPPING = {
    "All": -1,
    "PC / Laptop": 1,
    "Mobile": 2
}

REFERRERS_REQUIRED_HEADERS = {
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "X-Requested-With": "XMLHttpRequest"
}

REFERRERS_REQUEST_BODY_TEMPLATE = {
    "deviceType": -1,
    "fromDate": None,
    "toDate": None,
    "affId": None
}

REFERRERS_DETAILS_REQUEST_BODY_TEMPLATE = {
    "deviceType": -1,
    "fromDate": None,
    "toDate": None,
    "referrerUrl": None,
    "affId": None,
    "pageIndex": 1,
    "pageSize": 20
} 