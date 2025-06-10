import sys
import os
import pytest
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent

try:
    ENVIRONMENT = pytest.config.getoption('--env')
    SITE = pytest.config.getoption('--site')
    DEBUG_MODE = pytest.config.getoption('--debug_mode').lower() == 'true'
    HEADLESS_MODE = pytest.config.getoption('--headless').lower() == 'true'
    BROWSER = pytest.config.getoption('--browser')
except (AttributeError, ValueError):
    ENVIRONMENT = 'prod'
    SITE = 'admin'
    DEBUG_MODE = False
    HEADLESS_MODE = False
    BROWSER = 'chromium'

LANGUAGE = "en"
TIMEOUT = 30
ENABLE_BROWSER = True
ENABLE_TRACE = True
TRACE_PATH = "Trace\\trace.zip"


PROJECT_ROOT = str(ROOT_DIR)
LOG_LEVEL = "INFO"
LOG_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "logs")
LOG_FILENAME_TEMPLATE = "automation_{timestamp}.log"
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
LOG_TO_CONSOLE = True
LOG_TO_FILE = True


TELEGRAM_BOT_TOKEN = "7209718301:AAFjWzuvx0y27X2GiaAyNac1dp0zC_TrBuY"
TELEGRAM_CHAT_IDS = [5111377213]

TEAMS_CONVERSATION_IDS = ["a:1K7NcW8nE2v-QmtKdO5A-QCWscNlYzLCP4K-pWnQbLNa53nXO3hS15q-n1kuR6nxBoJ4MOYn25ymdeqbXesooWLSmQ3U-IFr8F3wK3ofzUjqJ1UV9v7jPUBeaI8dYmUkv"]

SLACK_CHANNEL_ID = ["C08USD10388"]
SLACK_BOT_TOKEN = "xoxb-8352731735536-8948054884291-UtxoV2jErsvn0wMDOe9d8ZYt"

ENABLE_DB = True
DB_USERNAME = "vnTestAutomation"
DB_PASSWORD = "@TestAutomation#"

ADMIN_12BET_URL= {
    "local": "http://aff-12b.nexdev.net/Admin",
    "uat": "https://aff15.starixuat.com/Admin",
    "prod": "https://affmanager.easymon5678.com/"}

ADMIN_12BET_USERNAME = {
    "local": "AAautomationtesting",
    "uat": "AAStarixQC02",
    "prod": "AAStarixQC02"
}

ADMIN_12BET_PASSWORD = {
    "local": "Nexcel-SUN",
    "uat": "WhatIsPassword",
    "prod": "WhatIsPassword"
}

ADMIN_12BET_SALT_PASSWORD = {
    "local": b'\x88\x05\xa8\xe2\xab\x05/>\x16\x9b\x13\xdf\xba\xa3\xe79',
    "uat": b'z`\xca\x1b\x95V\x11N\xaf\xd5\tn\xd6\xd9O\x08',
    "prod": b'z`\xca\x1b\x95V\x11N\xaf\xd5\tn\xd6\xd9O\x08'
}
ADMIN_12BET_ENCRYPTED_PASSWORD = {
    "local": b'gAAAAABmcl_WeYFYWquz9xURv9eSjs7wKqx9DBmt3GtoytZswEIbwCb_ouHnTE8D39_5uCcp4DRD2KtN0wzMZZuVHaeIS5cn1Q==',
    "uat": b'gAAAAABoR6aqesTX-oZyln_nZPmYk3sYb2nRR4SnnV3olK1qYNat5YDKgLYt-89eWP5FpNgHogTKuIGjI1HseGbLMFKYtzzCWA==',
    "prod": b'gAAAAABoR6aqesTX-oZyln_nZPmYk3sYb2nRR4SnnV3olK1qYNat5YDKgLYt-89eWP5FpNgHogTKuIGjI1HseGbLMFKYtzzCWA=='
}

USER_12BET_URL = {
    "local": "https://aff-12b.nexdev.net/UserAsian",
    "uat": "https://aff15.starixuat.com/UserAsian",
    "prod": "https://affiliate.easymon5678.com/"}

USER_12BET_USERNAME = {
    "local": "12betaff001",
    "uat": "12betaff001",
    "prod": "12betaff001"
}
USER_12BET_PASSWORD = {
    "local": "1234aa",
    "uat": "1234aa",
    "prod": "1234aa"
}
USER_12BET_SALT_PASSWORD = {
    "local": b'\x88\x05\xa8\xe2\xab\x05/>\x16\x9b\x13\xdf\xba\xa3\xe79',
    "uat": b'\x88\x05\xa8\xe2\xab\x05/>\x16\x9b\x13\xdf\xba\xa3\xe79',
    "prod": b'\x88\x05\xa8\xe2\xab\x05/>\x16\x9b\x13\xdf\xba\xa3\xe79'
}
USER_12BET_ENCRYPTED_PASSWORD = {
    "local": b'gAAAAABmcl_WeYFYWquz9xURv9eSjs7wKqx9DBmt3GtoytZswEIbwCb_ouHnTE8D39_5uCcp4DRD2KtN0wzMZZuVHaeIS5cn1Q==',
    "uat": b'gAAAAABmcl_WeYFYWquz9xURv9eSjs7wKqx9DBmt3GtoytZswEIbwCb_ouHnTE8D39_5uCcp4DRD2KtN0wzMZZuVHaeIS5cn1Q==',
    "prod": b'gAAAAABmcl_WeYFYWquz9xURv9eSjs7wKqx9DBmt3GtoytZswEIbwCb_ouHnTE8D39_5uCcp4DRD2KtN0wzMZZuVHaeIS5cn1Q=='
}