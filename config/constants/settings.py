import os
import pytest
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
CONFIG_DIR = Path(__file__).parent.parent

ENVIRONMENT = os.getenv('PYTEST_ENV', 'local')
SITE = os.getenv('PYTEST_SITE', 'admin')
DEBUG_MODE = os.getenv('PYTEST_DEBUG_MODE', 'false').lower() == 'true'
HEADLESS_MODE = os.getenv('PYTEST_HEADLESS', 'false').lower() == 'true'
BROWSER = os.getenv('PYTEST_BROWSER', 'chromium')

def load_env_config():
    env_files = [
        CONFIG_DIR / "environments" / "common" / f".env.{ENVIRONMENT}",
        CONFIG_DIR / "environments" / SITE / f".env.{ENVIRONMENT}"
    ]
    
    config = {}
    for env_file in env_files:
        if env_file.exists():
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
    
    return config

ENV_CONFIG = load_env_config()
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
ENABLE_DB = True

DB_USERNAME = ENV_CONFIG.get("DB_USERNAME", "default_user")
DB_PASSWORD = ENV_CONFIG.get("DB_PASSWORD", "default_pass")

TELEGRAM_BOT_TOKEN = ENV_CONFIG.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_CHAT_IDS = [int(x.strip()) for x in ENV_CONFIG.get("TELEGRAM_CHAT_IDS", "").split(",") if x.strip()]

TEAMS_CONVERSATION_IDS = [x.strip() for x in ENV_CONFIG.get("TEAMS_CONVERSATION_IDS", "").split(",") if x.strip()]

SLACK_CHANNEL_ID = [x.strip() for x in ENV_CONFIG.get("SLACK_CHANNEL_IDS", "").split(",") if x.strip()]
SLACK_BOT_TOKEN = ENV_CONFIG.get("SLACK_BOT_TOKEN", "")

if ENVIRONMENT == "prod":
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "https://aff-12b.12bet.net/Admin")
    USER_12BET_URL = ENV_CONFIG.get("USER_12BET_URL", "https://aff-12b.12bet.net")
elif ENVIRONMENT == "staging":
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "https://aff-12b-staging.12bet.net/Admin")
    USER_12BET_URL = ENV_CONFIG.get("USER_12BET_URL", "https://aff-12b-staging.12bet.net")
else:
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "http://aff-12b.nexdev.net/Admin")
    USER_12BET_URL = ENV_CONFIG.get("USER_12BET_URL", "http://aff-12b.nexdev.net")

ADMIN_12BET_USERNAME = ENV_CONFIG.get("ADMIN_12BET_USERNAME", "default_admin")
ADMIN_12BET_PASSWORD = ENV_CONFIG.get("ADMIN_12BET_PASSWORD", "default_pass")
ADMIN_12BET_SALT_PASSWORD = ENV_CONFIG.get("ADMIN_12BET_SALT_PASSWORD", "default_salt")
ADMIN_12BET_ENCRYPTED_PASSWORD = ENV_CONFIG.get("ADMIN_12BET_ENCRYPTED_PASSWORD", "default_encrypted_password")

USER_12BET_USERNAME = ENV_CONFIG.get("USER_12BET_USERNAME", "default_user")
USER_12BET_PASSWORD = ENV_CONFIG.get("USER_12BET_PASSWORD", "default_pass")
USER_12BET_SALT_PASSWORD = ENV_CONFIG.get("USER_12BET_SALT_PASSWORD", "default_salt")
USER_12BET_ENCRYPTED_PASSWORD = ENV_CONFIG.get("USER_12BET_ENCRYPTED_PASSWORD", "default_encrypted_password")

def get_config_summary():
    return {
        "environment": ENVIRONMENT,
        "site": SITE,
        "url": ADMIN_12BET_URL if SITE.lower() == "admin" else USER_12BET_URL,
        "browser": BROWSER,
        "headless": HEADLESS_MODE,
        "debug": DEBUG_MODE,
        "database_enabled": ENABLE_DB,
        "env_files_loaded": len([f for f in [
            CONFIG_DIR / "environments" / "common" / f".env.{ENVIRONMENT}",
            CONFIG_DIR / "environments" / SITE / f".env.{ENVIRONMENT}"
        ] if f.exists()])
    }

if DEBUG_MODE:
    print("🔧 Configuration Summary:")
    for key, value in get_config_summary().items():
        print(f"   {key}: {value}")