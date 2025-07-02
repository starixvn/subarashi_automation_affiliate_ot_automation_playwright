# AFF 12B Automation Framework

A comprehensive web automation testing framework built with Python, Playwright, and pytest, specifically designed for testing the OT affiliate system. This framework provides robust browser automation, API testing, database validation, and comprehensive reporting capabilities.

## 🚀 Quick Start

**Want to get started immediately? Follow these 4 steps:**

```bash
# 1. Install Python 3.13+ and uv
pip install uv

# 2. Clone and setup
git clone <repository-url>
cd AFF_12B_Automation_Python_Playwright
uv venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -e . && playwright install

# 3. Create basic environment file
mkdir -p config/environments/common
echo "ADMIN_12BET_URL=http://aff-12b.nexdev.net/Admin" > config/environments/common/.env.local

# 4. Run demo test
pytest test_suites/TestSuites_01_Demo.py -v
```

**✅ If the demo test runs successfully, you're ready to go!**  
**❌ If it fails, check the [Complete Setup Guide](#-installation) below.**

---

## 🎯 Features

### Core Capabilities
- **Multi-Browser Support**: Chromium, Chrome, Firefox, Safari with headless/headful modes
- **Multi-Environment**: Local, uat, and production environment configurations
- **Cross-Platform**: Windows, macOS, and Linux support
- **Page Object Model**: Clean separation of test logic and page elements
- **Data-Driven Testing**: JSON and Excel-based test data management

### Advanced Features
- **Database Testing**: SQL Server integration with connection pooling
- **API Testing**: RESTful API testing with comprehensive assertion methods
- **Google Sheets Integration**: Automated test result reporting and tracking
- **Multi-Channel Notifications**: Slack, Telegram, and MS Teams integration
- **Smart Waiting**: Intelligent element waiting strategies and network idle detection
- **Cryptographic Security**: Encrypted credential management
- **Comprehensive Logging**: Multi-level logging with colored console output
- **Error Handling**: Custom exception hierarchy with detailed error tracking
- **Performance Monitoring**: Execution time tracking and performance metrics

## 📋 Prerequisites

### System Requirements
- **Python**: 3.13 or higher
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 18.04+)
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Disk Space**: At least 2GB free space

### Required Software
- Git for version control
- A modern web browser (Chrome, Firefox, or Edge)

## 🛠️ Installation

### 1. Install Python and uv Package Manager

First, ensure Python 3.13+ is installed on your system:

```bash
# Check Python version
python --version

# If Python is not installed or version is below 3.13, download from:
# https://www.python.org/downloads/
```

Install the `uv` package manager for faster dependency management:

```bash
pip install uv
```

### 2. Clone the Repository

```bash
git clone <repository-url>
cd AFF_12B_Automation_Python_Playwright
```

### 3. Create Virtual Environment and Install Dependencies

```bash
# Create virtual environment using uv
uv venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
uv pip install -e .

# Install Playwright browsers
playwright install
```

### 4. Install Development Dependencies (Optional)

```bash
uv pip install -e ".[dev]"
```

## ⚙️ Configuration

### Environment Configuration

The framework uses a sophisticated configuration system with support for multiple environments and sites.

#### 1. Create Environment Files

Create environment-specific configuration files in the `config/environments/` directory:

```
config/
├── environments/
│   ├── common/
│   │   ├── .env.local
│   │   ├── .env.uat
│   │   └── .env.prod
│   ├── admin/
│   │   ├── .env.local
│   │   ├── .env.uat
│   │   └── .env.prod
│   └── user/
│       ├── .env.local
│       ├── .env.uat
│       └── .env.prod
```

#### 2. Example Environment File (.env.local)

```env
# Database Configuration
DB_USERNAME=your_db_username
DB_PASSWORD=your_db_password

# Application URLs
ADMIN_12BET_URL=http://aff-12b.nexdev.net/Admin
USER_12BET_URL=http://aff-12b.nexdev.net

# Authentication Credentials
ADMIN_12BET_USERNAME=your_admin_username
ADMIN_12BET_PASSWORD=your_password_key
ADMIN_12BET_SALT_PASSWORD=your_salt_key
ADMIN_12BET_ENCRYPTED_PASSWORD=your_encrypted_password

USER_12BET_USERNAME=your_user_username
USER_12BET_PASSWORD=your_user_password_key
USER_12BET_SALT_PASSWORD=your_user_salt_key
USER_12BET_ENCRYPTED_PASSWORD=your_user_encrypted_password

# Notification Settings
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_IDS=chat_id_1,chat_id_2
TEAMS_CONVERSATION_IDS=conversation_id_1,conversation_id_2
SLACK_CHANNEL_IDS=channel_id_1,channel_id_2
SLACK_BOT_TOKEN=your_slack_bot_token
```

#### 3. Google Sheets Configuration (Complete Setup Guide)

The framework integrates with Google Sheets for automated test result reporting. Here's the complete setup process:

##### Step 3.1: Create Google Service Account

1. **Go to Google Cloud Console**: https://console.cloud.google.com/
2. **Create or select a project**:
   - Click "Select a project" → "New Project"
   - Name it "Automation Framework" → Create

3. **Enable Google Sheets API**:
   - Go to "APIs & Services" → "Library"
   - Search "Google Sheets API" → Enable

4. **Create Service Account**:
   - Go to "APIs & Services" → "Credentials"
   - Click "Create Credentials" → "Service Account"
   - Name: "automation-service-account"
   - Role: "Editor" → Create

5. **Generate JSON Key**:
   - Click on your service account
   - Go to "Keys" tab → "Add Key" → "Create new key"
   - Choose "JSON" → Download the file

##### Step 3.2: Setup Credentials File

Place the downloaded JSON file at:
```
config/secrets/client_secret.json
```

**Example content structure**:
```json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "automation-service-account@your-project.iam.gserviceaccount.com",
  "client_id": "123456789",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

##### Step 3.3: Create Google Sheets Template

1. **Create a new Google Sheet**: https://sheets.google.com/
2. **Name it**: "Automation Test Results"
3. **Create sheets for each test module**:
   - Demo_Message (for demo tests)
   - Login_Tests (for login tests)
   - Your_Module_Tests (for your custom tests)

4. **Setup column headers** (in each sheet) - **CRITICAL: Must match exactly**:
   ```
   A: Categories (Test category grouping)
   B: Sub Categories (Sub-category classification)
   C: Checklist (Test step description - what is being verified)
   D: Expectation (Expected behavior/result)
   E: Auto_Testcase (EXACT test method name from TestSuites file)
   F: Sub_Auto_Testcases (Detailed execution log and steps)
   G: Local (Local environment test results)
   H: UAT (UAT environment test results)
   I: PRO (Production environment test results)
   J: Latest Date Run (Most recent execution timestamp)
   K: Latest Env Run (Most recent execution environment)
   L: Duration (Test execution time)
   ```

   **⚠️ CRITICAL REQUIREMENT for Column E (Auto_Testcase):**
   
   Column E must contain the **EXACT method name** from your test suite file:
   ```python
   # In your TestSuites file:
   def TestCase_04_verify_marketing_pages_total_clicks_match_referrers(self):
   
   # In Google Sheets Column E, enter exactly:
   TestCase_04_verify_marketing_pages_total_clicks_match_referrers
   ```
   
   **Examples of correct Auto_Testcase entries:**
   - `TestCase_01_Verify_UI_Message_Page`
   - `TestCase_04_verify_marketing_pages_total_clicks_match_referrers`  
   - `TestCase_05_verify_marketing_pages_total_clicks_match_landing_pages`
   - `TestCase_06_verify_marketing_pages_signups_match_referrers`
   - `TestCase_07_verify_marketing_pages_signups_match_landing_pages`

##### Step 3.4: Share Sheet with Service Account

1. **Copy the service account email** from your JSON file:
   ```
   automation-service-account@your-project.iam.gserviceaccount.com
   ```

2. **Share your Google Sheet**:
   - Click "Share" button in your Google Sheet
   - Paste the service account email
   - Give "Editor" permissions
   - Uncheck "Notify people" → Send

##### Step 3.5: Configure Framework

1. **Get your Google Sheets ID** from the URL:
   ```
   https://docs.google.com/spreadsheets/d/1ABC123xyz789_EXAMPLE_ID/edit
                                    ^^^^^^^^^^^^^^^^^^^
                                    This is your sheet ID
   ```

2. **Update `src/test_data/common/data_common.py`**:
   ```python
   # Replace with your actual Google Sheets ID
   TestCase_Spread_Sheet_Id = "1ABC123xyz789_EXAMPLE_ID"
   
   # Test execution status codes (don't change these)
   TestCase_Auto_Status = ["Passed", "Failed", "Not-Test"]
   ```

##### Step 3.6: Test Google Sheets Integration

Run this validation test:
```bash
# This will test Google Sheets connectivity
python -c "
from src.utils.services.utils.google_methods import GoogleMethods
gm = GoogleMethods()
print('✅ Google Sheets integration working!')
"
```

**Common Issues and Solutions**:

- **"Insufficient Permission"**: Service account needs Editor access to the sheet
- **"File not found"**: Check `client_secret.json` path and format
- **"API not enabled"**: Enable Google Sheets API in Google Cloud Console
- **"Invalid credentials"**: Re-download and replace the JSON file

### Framework Settings

Key configuration options in `config/constants/settings.py`:

```python
# Browser Configuration
BROWSER = "chromium"  # chromium, chrome, firefox, safari
HEADLESS_MODE = False  # True for headless execution
TIMEOUT = 30  # Default timeout in seconds

# Feature Toggles
ENABLE_BROWSER = True   # Enable browser automation
ENABLE_TRACE = True     # Enable Playwright tracing
ENABLE_DB = True        # Enable database connections

# Logging Configuration
LOG_LEVEL = "INFO"      # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_TO_CONSOLE = True   # Console logging
LOG_TO_FILE = True      # File logging
```

## 📁 Project Structure Walkthrough

Understanding the project structure is crucial for implementing tests correctly:

### Complete Directory Structure
```
AFF_12B_Automation_Python_Playwright/
├── 📋 config/                    # Configuration management
│   ├── constants/
│   │   └── settings.py          # Framework settings & environment config
│   ├── environments/            # Environment-specific configurations
│   │   ├── common/              # Shared environment settings
│   │   │   ├── .env.local      # Local environment variables
│   │   │   ├── .env.uat        # UAT environment variables  
│   │   │   └── .env.prod       # Production environment variables
│   │   ├── admin/              # Admin-specific environment settings
│   │   └── user/               # User-specific environment settings
│   └── secrets/                # Secure credential files
│       └── client_secret.json  # Google Service Account credentials
│
├── 🧪 test_suites/              # Test execution entry points
│   ├── TestSuites_01_Demo.py   # Demo test implementation
│   ├── functional_testing/     # Feature-specific test suites
│   ├── smoke_test/             # Quick validation tests
│   └── e2e/                    # End-to-end test scenarios
│
├── 📂 src/                      # Framework source code
│   ├── 🎬 actions/              # Business logic layer (WHERE YOU IMPLEMENT TEST LOGIC)
│   │   ├── action_demo.py      # Example: Demo action implementation
│   │   ├── common/             # Shared actions and utilities
│   │   │   ├── action_common.py # Base class for all actions
│   │   │   ├── compare_data/   # Data comparison utilities
│   │   │   └── get_data_on_function/ # Data extraction utilities
│   │   ├── admin/              # Admin-specific actions
│   │   │   ├── authentication/ # Login/logout actions
│   │   │   ├── customer/       # Customer management actions
│   │   │   ├── domain/         # Domain management actions
│   │   │   └── ...            # Other admin modules
│   │   └── user/               # User-specific actions
│   │       ├── functional/     # User functional test actions
│   │       └── ui/            # User UI test actions
│   │
│   ├── 📄 interfaces/          # Page Object Model (WHERE YOU DEFINE UI ELEMENTS)
│   │   ├── demo_elements.py    # Example: Demo page elements
│   │   ├── admin/              # Admin page elements
│   │   │   ├── authentication/
│   │   │   │   └── login.py   # Login page elements
│   │   │   ├── customer/       # Customer page elements
│   │   │   └── ...            # Other admin page elements
│   │   └── user/               # User page elements
│   │
│   ├── 📊 test_data/           # Test data management (WHERE YOU DEFINE TEST DATA)
│   │   ├── demo_test_data.py   # Example: Demo test data
│   │   ├── common/             # Shared test data
│   │   │   └── data_common.py  # Common test configurations
│   │   ├── admin/              # Admin test data
│   │   └── user/               # User test data
│   │
│   ├── 🔧 utils/               # Core framework utilities (THE HEART - DON'T MODIFY)
│   │   ├── core/               # Core functionality
│   │   │   ├── decorators.py   # Retry, monitoring, timing decorators
│   │   │   ├── exceptions.py   # Custom exception hierarchy
│   │   │   ├── logging.py      # Advanced logging system
│   │   │   ├── validation.py   # Input validation utilities
│   │   │   └── utils.py        # Common utilities
│   │   └── services/           # Service layer implementation
│   │       ├── api_utils/      # API testing services
│   │       ├── db_utils/       # Database services
│   │       ├── page_utils/     # Browser automation services
│   │       └── utils/          # Main utilities orchestrator
│   │
│   └── 🏃 jobs/                # Background job executors
│       └── common/             # Data baseline collection jobs
│
├── 📋 pyproject.toml           # Project dependencies and configuration
├── 🧪 pytest.ini              # pytest configuration
├── 🛠️ conftest.py             # pytest fixtures and configuration
└── 📖 README.md               # This documentation
```

### Key Files for Beginners 🔰

**Start with these files to understand the framework:**

1. **`test_suites/TestSuites_01_Demo.py`** - See how tests are structured
2. **`src/actions/action_demo.py`** - Learn how to implement test logic
3. **`src/interfaces/demo_elements.py`** - Understand page element definitions
4. **`src/test_data/demo_test_data.py`** - See how test data is organized
5. **`config/constants/settings.py`** - Framework configuration options

### Typical Implementation Flow 🔄

```
1. 📄 Define UI elements → src/interfaces/your_module_elements.py
2. 📊 Create test data → src/test_data/your_module_test_data.py  
3. 🎬 Implement actions → src/actions/your_module.py
4. 🧪 Create test suite → test_suites/TestSuites_XX_YourModule.py
5. ⚙️ Configure environment → config/environments/
```

## 🏗️ Architecture

### Core Framework Architecture - "The Heart of the System"

The framework's core is built around a sophisticated service-oriented architecture with multiple layers of abstraction, providing maximum flexibility and maintainability.

#### Module Organization and Import Strategy

The framework uses a hierarchical import system that allows for clean dependency management:

```python
# Main utils package (__init__.py)
from src.utils.core import (
    # All core exceptions, decorators, logging, validation
)
from src.utils.services import api, db, ui, utilities

# Service layer organization
src/utils/services/
├── __init__.py           # Exports all service classes
├── api_utils/            # API testing services
│   ├── __init__.py      # api class with multiple inheritance
│   ├── assertion_methods.py
│   ├── extraction_methods.py
│   └── request_methods.py
├── db_utils/             # Database services
│   ├── __init__.py      # db class with multiple inheritance
│   ├── connection_methods.py
│   ├── data_methods.py
│   └── query_methods.py
├── page_utils/           # Browser automation services
│   ├── __init__.py      # ui class with multiple inheritance
│   ├── element_methods.py
│   ├── extraction_methods.py
│   ├── file_methods.py
│   ├── frame_methods.py
│   ├── navigation_methods.py
│   ├── screenshot_methods.py
│   ├── verification_methods.py
│   └── waits.py
└── utils/                # Utility services
    ├── __init__.py      # utilities class (main entry point)
    ├── assertion_methods.py
    ├── browser_methods.py
    ├── crypto_methods.py
    ├── file_methods.py
    ├── google_methods.py
    └── report_methods.py
```

### Core Components Deep Dive

#### 1. Core Utilities (`src/utils/core/`) - The Foundation

##### **decorators.py** - The Intelligence Layer
```python
# Sophisticated retry mechanism with exponential backoff
@retry(max_attempts=3, delay_seconds=1.0, backoff_factor=2.0)
def unstable_operation():
    pass

# Performance monitoring with conditional logging
@monitor_performance(threshold_seconds=5.0)
def tracked_operation():
    pass

# Automatic test execution time tracking for Google Sheets
@measure_test_execution_time
def test_method():
    pass

# Exception conversion and logging
@log_exceptions(log_level="ERROR", re_raise=True)
def risky_operation():
    pass
```

**Key Features:**
- **Smart Retry Logic**: Supports both fixed and dynamic retry attempts based on instance methods
- **Performance Monitoring**: Automatic execution time tracking with configurable thresholds
- **Test Execution Measurement**: Integrates with Google Sheets for automatic duration reporting
- **Exception Handling**: Comprehensive exception logging with optional re-raising

##### **exceptions.py** - Hierarchical Error Management
```python
# Base exception with rich context
class AutomationException(Exception):
    def __init__(self, message, details=None, context=None, 
                 original_exception=None, operation="unknown", test_case=None):
        # Rich exception data with JSON export capability

# Specialized exceptions for different domains
class ElementNotFoundException(ElementException):
    # Browser element-specific errors with selector context

class APIException(ServiceException):
    # API-specific errors with request/response context

class DatabaseException(ServiceException):
    # Database-specific errors with query context
```

**Exception Hierarchy:**
- **AutomationException** (Base)
  - **ValidationException** (Input validation errors)
  - **ServiceException** (Service layer errors)
    - **APIException** (API testing errors)
    - **DatabaseException** (Database operation errors)
  - **BrowserException** (Browser automation errors)
    - **ElementException** (Element interaction errors)
    - **NavigationException** (Page navigation errors)
    - **TimeoutException** (Waiting operation errors)
  - **IoException** (File/Network I/O errors)
  - **NotificationException** (Reporting system errors)

##### **logging.py** - Advanced Logging System
```python
# Custom log levels
TRACE = 5      # Most detailed debugging
VERBOSE = 15   # Detailed debugging
NOTICE = 25    # Important notices
SUCCESS = 35   # Success messages

# Colored console output with auto-detection
class ColoredFormatter(logging.Formatter):
    # Automatic color application based on terminal support

# Enhanced logger class
class AutomationLogger(logging.Logger):
    def trace(self, msg, *args, **kwargs):
        self.log(TRACE, msg, *args, **kwargs)
```

**Features:**
- **Multi-Level Logging**: TRACE, DEBUG, VERBOSE, INFO, NOTICE, SUCCESS, WARNING, ERROR, CRITICAL
- **Colored Console Output**: Automatic color detection and application
- **File and Console Logging**: Simultaneous output to both destinations
- **Timestamped Log Files**: Automatic file naming with timestamps

##### **validation.py** - Comprehensive Input Validation
```python
# Type validation with detailed error messages
def validate_type(value, expected_type, name="value"):
    # Supports single types and tuple of types

# Range validation for numeric values
def validate_range(value, min_value=None, max_value=None, name="value"):
    # Inclusive range checking with optional bounds

# Pattern validation with regex
def validate_string_pattern(value, pattern, name="value"):
    # Regex pattern matching with clear error messages

# File system validation
def validate_file_exists(file_path, name="file"):
    # Path validation with existence checking
```

##### **utils.py** - Core Utilities and Patterns
```python
# Singleton pattern implementation
class Singleton(type):
    # Thread-safe singleton metaclass

# Unique ID generation
def generate_unique_id(prefix="", length=8):
    # Timestamp-based unique ID generation

# Smart waiting with custom conditions
def wait_until(condition, timeout=10.0, poll_interval=0.5):
    # Flexible condition waiting with timeout

# Advanced retry mechanism
def retry_on_exception(func, max_attempts=3, delay=1.0, backoff_factor=2.0):
    # Function-level retry with exponential backoff
```

#### 2. Service Layer Architecture (`src/utils/services/`)

The service layer uses **multiple inheritance** to create powerful, feature-rich service classes:

##### **API Testing Services** (`api_utils/`)
```python
# Multiple inheritance pattern
class api(RequestMethods, AssertionMethods, ExtractionMethods):
    def __init__(self, api: APIRequestContext):
        # Initialize all parent classes
        RequestMethods.__init__(self)
        AssertionMethods.__init__(self)
        ExtractionMethods.__init__(self)
        self.api = api
```

**Components:**
- **RequestMethods**: HTTP operations (GET, POST, PUT, DELETE) with debugging
- **AssertionMethods**: Response validation and status code checking
- **ExtractionMethods**: JSON path extraction and regex matching

**Usage Example:**
```python
# Unified API testing interface
response = self.utils.api.get("https://api.example.com/users")

# API-specific assertion methods
self.utils.api.assert_status_code(response, 200)
self.utils.api.assert_response_contains(response, "user_data")

# Extract data using JSONPath (from extraction methods)
user_name = self.utils.api.extract_by_jsonpath(response, "$.users[0].name")

# Set authentication if needed
self.utils.api.set_auth("your_bearer_token")
```

##### **Database Services** (`db_utils/`)
```python
class db(ConnectionMethods, QueryMethods, DataMethods):
    def __init__(self):
        # Shared connection attributes across all methods
        ConnectionMethods.__init__(self)
        QueryMethods.__init__(self)
        DataMethods.__init__(self)
```

**Components:**
- **ConnectionMethods**: SQL Server connection management with environment validation
- **QueryMethods**: SELECT queries with result formatting
- **DataMethods**: INSERT/UPDATE operations with transaction support

**Usage Example:**
```python
# Database operations with automatic cleanup
self.utils.db.connect("server_name", "database_name")
results = self.utils.db.query_and_get_all("SELECT * FROM users")

# Get specific column values
user_names = self.utils.db.get_value_in_column("SELECT * FROM users", "username")

# Execute non-SELECT queries
self.utils.db.query("INSERT INTO test_results VALUES ('test', 'passed')", 'insert')
self.utils.db.close()
```

##### **Page Automation Services** (`page_utils/`)
```python
class ui(NavigationMethods, ElementMethods, ExtractionMethods, 
         FrameMethods, VerificationMethods, FileMethods, 
         ScreenshotMethods, SmartWaits):
    def __init__(self, page: Page):
        # Initialize all interaction methods
        # 8 different method classes for comprehensive page automation
```

**Components:**
- **NavigationMethods**: Page navigation and URL management
- **ElementMethods**: Element interaction (click, input, select)
- **ExtractionMethods**: Text and attribute extraction
- **FrameMethods**: iFrame and popup handling
- **VerificationMethods**: Element existence and state verification
- **FileMethods**: File upload and download operations
- **ScreenshotMethods**: Screen capture functionality
- **SmartWaits**: Intelligent waiting strategies

**Usage Example:**
```python
# Comprehensive page automation
self.utils.page.navigate("https://example.com")
self.utils.page.wait_for_element_ready("//button[@id='login']")
self.utils.page.input("//input[@name='username']", "testuser")
self.utils.page.click_with_retry("//button[@type='submit']")
self.utils.page.wait_for_network_idle()
```

##### **Utility Services** (`utils/`)
```python
class utilities(BrowserMethods, AssertionMethods, FileMethods, 
                GoogleMethods, ReportMethods):
    def __init__(self):
        # Main entry point - initializes browser, API, and database services
        self.page = ui(browser_page)    # Page automation
        self.api = api(api_context)     # API testing
        self.db = db()                  # Database operations
```

**Components:**
- **BrowserMethods**: Browser lifecycle management
- **AssertionMethods**: Test assertion utilities
- **FileMethods**: File operations and Excel handling
- **GoogleMethods**: Google Sheets integration
- **ReportMethods**: Multi-channel notification system

#### 3. Configuration Management (`config/constants/settings.py`)

The configuration system provides sophisticated environment management:

```python
# Dynamic environment loading
def load_env_config():
    env_files = [
        CONFIG_DIR / "environments" / "common" / f".env.{ENVIRONMENT}",
        CONFIG_DIR / "environments" / SITE / f".env.{ENVIRONMENT}"
    ]
    # Load and merge configuration from multiple sources

# Environment-specific URL configuration
if ENVIRONMENT == "prod":
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "https://aff-12b.12bet.net/Admin")
elif ENVIRONMENT == "uat":
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "https://aff-12b-uat.12bet.net/Admin")
else:
    ADMIN_12BET_URL = ENV_CONFIG.get("ADMIN_12BET_URL", "http://aff-12b.nexdev.net/Admin")

# Configuration validation and debugging
def get_config_summary():
    return {
        "environment": ENVIRONMENT,
        "site": SITE,
        "url": ADMIN_12BET_URL if SITE.lower() == "admin" else USER_12BET_URL,
        "browser": BROWSER,
        "headless": HEADLESS_MODE,
        "debug": DEBUG_MODE,
        "database_enabled": ENABLE_DB,
        "env_files_loaded": len([f for f in env_files if f.exists()])
    }
```

#### 4. Integration Patterns and Data Flow

##### **Test Execution Flow:**
1. **pytest** loads configuration from `conftest.py`
2. **Test class** inherits from `unittest.TestCase`
3. **setUpClass** initializes `ActionDemo` which inherits from `Common`
4. **Common.setup()** creates `utilities()` instance
5. **utilities** initializes browser, API, and database services
6. **Test methods** use decorators for timing and error handling
7. **Google Sheets integration** automatically reports results
8. **tearDownClass** triggers cleanup and notifications

##### **Error Handling Flow:**
1. **Custom exceptions** capture detailed context
2. **Decorators** log exceptions with full stack traces
3. **Test tracking** system captures failed test names
4. **Google Sheets** receives failure status and details
5. **Notification system** sends alerts via multiple channels

##### **Service Integration Pattern:**
```python
# All services accessible through unified interface
self.utils.page.click("//button[@id='submit']")        # Browser automation
self.utils.api.get("https://api.example.com/status")   # API testing  
self.utils.db.query("SELECT * FROM test_results")      # Database operations
self.utils.update_result_to_ggsheet(...)               # Google Sheets reporting
self.utils.send_message_to_slack()                     # Notifications
```

This architecture provides:
- **Unified Interface**: Single entry point for all testing operations
- **Modular Design**: Each service can be used independently
- **Comprehensive Error Handling**: Rich exception context and automatic logging
- **Performance Monitoring**: Built-in timing and metrics collection
- **Automatic Reporting**: Integration with Google Sheets and notification systems

#### 5. Multiple Inheritance Implementation Details

The framework extensively uses **multiple inheritance** to create feature-rich service classes. Here's how each `__init__.py` file implements this pattern:

##### **API Utils (`src/utils/services/api_utils/__init__.py`)**
```python
class api(RequestMethods, AssertionMethods, ExtractionMethods):
    TcName = TC_NAME  # Shared test case tracking
    
    def __init__(self, api: APIRequestContext):
        # Validate input
        validate_not_none(api, "api")
        validate_type(api, APIRequestContext, "api")
        
        # Initialize all parent classes
        RequestMethods.__init__(self)      # HTTP operations
        AssertionMethods.__init__(self)    # Response validation
        ExtractionMethods.__init__(self)   # Data extraction
        
        self.api = api  # Shared Playwright API context
```

**Key Features:**
- **Shared API Context**: All methods use the same Playwright APIRequestContext
- **Test Tracking**: Integrated test case failure tracking
- **Validation**: Input validation on initialization
- **Method Composition**: Three specialized method classes combined

##### **Database Utils (`src/utils/services/db_utils/__init__.py`)**
```python
class db(ConnectionMethods, QueryMethods, DataMethods):
    dbconnect: Optional[pyodbc.Connection] = None
    dbcursor: Optional[pyodbc.Cursor] = None
    TcName = TC_NAME  # Shared test case tracking
    
    def __init__(self):
        # Initialize all parent classes
        ConnectionMethods.__init__(self)   # Connection management
        QueryMethods.__init__(self)        # Query execution
        DataMethods.__init__(self)         # Data manipulation
        
        # Shared attributes across all classes
        # All classes inherit the same connection objects
```

**Key Features:**
- **Shared Connection State**: All method classes share the same database connection
- **Transaction Support**: Automatic transaction management across operations
- **Environment Validation**: Built-in environment checking
- **Connection Pooling**: Automatic connection lifecycle management

##### **Page Utils (`src/utils/services/page_utils/__init__.py`)**
```python
class ui(NavigationMethods, ElementMethods, ExtractionMethods, 
         FrameMethods, VerificationMethods, FileMethods, 
         ScreenshotMethods, SmartWaits):
    TcName = TC_NAME  # Shared test case tracking
    page: Page        # Playwright Page object
    
    def __init__(self, page: Page):
        validate_not_none(page, "page")
        validate_type(page, Page, "page")
        
        # Initialize all 8 method classes
        NavigationMethods.__init__(self, page)    # Page navigation
        ElementMethods.__init__(self, page)       # Element interactions
        ExtractionMethods.__init__(self, page)    # Data extraction
        FrameMethods.__init__(self, page)         # Frame handling
        VerificationMethods.__init__(self, page)  # Element verification
        FileMethods.__init__(self, page)          # File operations
        ScreenshotMethods.__init__(self, page)    # Screen capture
        SmartWaits.__init__(self, page)           # Intelligent waiting
        
        # Configure page timeouts
        self.page.set_default_timeout(TIMEOUT*1000)
        self.page.set_default_navigation_timeout(TIMEOUT*1000)
```

**Key Features:**
- **8-Class Composition**: Most comprehensive multiple inheritance in the framework
- **Shared Page Context**: All methods operate on the same Playwright Page object
- **Timeout Configuration**: Automatic timeout setup
- **Method Specialization**: Each class handles specific aspects of page automation

##### **Main Utils (`src/utils/services/utils/__init__.py`)**
```python
class utilities(BrowserMethods, AssertionMethods, FileMethods, 
                GoogleMethods, ReportMethods):
    tcsF = TC_NAME        # Test case failure tracking
    FuncName = None       # Current test function name
    page: Optional['ui'] = None    # Page automation service
    api: Optional['api'] = None    # API testing service  
    db: Optional['db'] = None      # Database service
    
    def __init__(self):
        # Initialize parent classes
        BrowserMethods.__init__(self)
        
        # Extract test function name from pytest context
        current_test = os.getenv('PYTEST_CURRENT_TEST')
        if current_test:
            match = re.search('TestSuites_([0-9]{2}|DemoSite)_(.*).py', current_test)
            if match:
                self.FuncName = str(match.group(2)).replace("_", " ")
        
        # Initialize services based on configuration
        if ENABLE_BROWSER:
            self.initialize_browser()  # Creates self.page
            
        if ENABLE_DB:
            from src.utils.services.db_utils import db
            self.db = db()
```

**Key Features:**
- **Service Orchestration**: Main entry point that initializes all other services
- **Conditional Initialization**: Services initialized based on configuration
- **Test Context Awareness**: Automatically extracts current test name
- **Resource Management**: Handles browser, API, and database lifecycle

##### **Services Package (`src/utils/services/__init__.py`)**
```python
from src.utils.services.api_utils import api
from src.utils.services.db_utils import db
from src.utils.services.page_utils import ui
from src.utils.services.utils import utilities

__all__ = [
    'api',      # API testing service
    'db',       # Database service
    'ui',       # Page automation service
    'utilities' # Main orchestrator service
]
```

##### **Core Utils Package (`src/utils/core/__init__.py`)**
```python
# Exception hierarchy exports
from src.utils.core.exceptions import (
    AutomationException, ValidationException, ServiceException,
    APIException, DatabaseException, BrowserException,
    ElementException, ElementNotFoundException,
    # ... 20+ exception classes
)

# Logging system exports
from src.utils.core.logging import (
    get_logger, AutomationLogger,
    TRACE, VERBOSE, NOTICE, SUCCESS,
)

# Decorator exports
from src.utils.core.decorators import (
    retry, log_exceptions, monitor_performance, convert_exceptions,
)

# Validation utilities exports
from src.utils.core.validation import (
    validate_not_none, validate_type, validate_range,
    validate_email, validate_url, validate_file_exists,
    # ... 20+ validation functions
)

# Utility functions exports
from src.utils.core.utils import (
    generate_unique_id, get_timestamp, load_json_file,
    ensure_directory_exists, format_duration,
    # ... 15+ utility functions
)

# Test tracking exports
from src.utils.core.test_tracker import (
    ExtractTestCaseFailed, TC_NAME
)

# Complete __all__ list with 50+ exports
__all__ = [
    # All exports listed for clean imports
]
```

##### **Main Utils Package (`src/utils/__init__.py`)**
```python
# Centralized import strategy
from src.utils.core import (
    # All core functionality
    AutomationException, ValidationException,
    retry, log_exceptions, monitor_performance,
    get_logger, validate_not_none, validate_type,
    # ... 40+ core imports
)

from src.utils.services import api, db, ui, utilities

# Master export list
__all__ = [
    # All 50+ exports available at package level
    'api', 'db', 'ui', 'utilities'
]
```

#### 6. Design Patterns and Best Practices

##### **Mixin Pattern Implementation**
Each method class acts as a mixin, providing specific functionality:

```python
# Each mixin provides focused functionality
class RequestMethods:           # HTTP operations mixin
class AssertionMethods:         # Validation mixin  
class ExtractionMethods:        # Data extraction mixin

# Combined via multiple inheritance
class api(RequestMethods, AssertionMethods, ExtractionMethods):
    # Full-featured API testing service
```

##### **Shared State Management**
```python
# Database services share connection state
class ConnectionMethods:
    def __init__(self):
        self.dbconnect = None  # Shared connection
        self.cursor = None     # Shared cursor

class QueryMethods:
    def query(self, sql):
        # Uses shared self.cursor from ConnectionMethods
        return self.cursor.execute(sql)

class DataMethods:
    def insert_data(self, table, data):
        # Uses shared self.dbconnect for transactions
        self.dbconnect.commit()
```

##### **Service Integration Pattern**
```python
# Main utilities class provides unified access
class utilities:
    def __init__(self):
        # Create service instances
        browser_page = self.create_browser_page()
        api_context = self.create_api_context()
        
        # Initialize service objects
        self.page = ui(browser_page)    # Page automation
        self.api = api(api_context)     # API testing
        self.db = db()                  # Database operations
        
    # All services accessible through single interface
    def get_user_data(self, user_id):
        # Can combine page, API, and database operations
        self.page.navigate(f"/user/{user_id}")
        api_data = self.api.get(f"/api/users/{user_id}")
        db_data = self.db.query(f"SELECT * FROM users WHERE id = {user_id}")
        return {"page": self.page.get_text("//h1"), "api": api_data, "db": db_data}
```

This sophisticated architecture enables:
- **Code Reusability**: Method classes can be mixed and matched
- **Clean Separation**: Each class has a single responsibility
- **Easy Testing**: Individual method classes can be tested independently
- **Scalability**: New functionality can be added as new mixin classes
- **Type Safety**: Full type hints and validation throughout

#### 7. Performance Monitoring and Test Tracking Integration

The framework includes sophisticated performance monitoring and test tracking capabilities:

##### **Test Execution Time Tracking**
```python
# Automatic test duration measurement with Google Sheets integration
@measure_test_execution_time
def TestCase_001_Verify_UI_Message_Page(self):
    # Framework automatically:
    # 1. Captures start time
    # 2. Executes test method
    # 3. Calculates duration
    # 4. Updates Google Sheets with execution time
    # 5. Handles errors gracefully
    
# Implementation in decorators.py
_test_case_last_checklist = {}  # Global cache for test metadata

def measure_test_execution_time(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        test_name = func.__name__
        start_time = time.time()
        
        try:
            result = func(self, *args, **kwargs)
            end_time = time.time()
            execution_time = end_time - start_time
            duration = str(timedelta(seconds=int(execution_time)))
            
            # Automatic Google Sheets update
            if test_name in _test_case_last_checklist:
                self.utils.update_duration_only(
                    spread_sheet_id, test_name, duration, sheet_name
                )
                
        except Exception as e:
            # Even failures get duration tracking
            end_time = time.time()
            execution_time = end_time - start_time
            duration = str(timedelta(seconds=int(execution_time)))
            # Update duration and re-raise exception
            raise e
```

##### **Test Case Failure Tracking System**
```python
# Global test case tracking (test_tracker.py)
TC_NAME = []  # Global list of failed test cases

class ExtractTestCaseFailed:
    def extract_TestCaseFailed(self, error):
        # Automatic test case name extraction from pytest context
        if os.getenv('PYTEST_CURRENT_TEST'):
            test_case = str(re.search('::(TestCase.*) ', 
                           os.getenv('PYTEST_CURRENT_TEST')).group(1)).replace("_", " ")
            TC_NAME.append(test_case)
            logger.error(f"Test case failed: {test_case}")
            
        # All service classes inherit from this for automatic failure tracking
```

##### **Google Sheets Integration with Performance Data**
```python
# Real-time test result reporting (google_methods.py)
@track_last_checklist  # Decorator stores test metadata
def update_result_to_ggsheet(self, spread_sheet_id, checklist, auto_testcase, 
                           sub_auto_testcases, auto_status, sheet_name="Checklist", duration=None):
    
    # Multi-environment support
    env_column_map = {
        "local": "G",
        "uat": "H", 
        "prod": "I"
    }
    
    # Automatic timestamp and environment tracking
    today = datetime.now()
    toDate = datetime.strftime(today, "%m/%d/%Y %H:%M:%S")
    
    # Updates multiple columns simultaneously:
    # - Test case details
    # - Execution status (Passed/Failed/Not-Test)
    # - Execution timestamp
    # - Environment information
    # - Duration (if provided)
    # - Latest environment run
```

##### **Performance Monitoring Decorators**
```python
# Method-level performance monitoring
@monitor_performance(threshold_seconds=5.0)
def slow_database_operation(self):
    # Automatically logs execution time if > threshold
    
@retry(max_attempts=3, delay_seconds=1.0, backoff_factor=2.0)
def unstable_network_operation(self):
    # Sophisticated retry with performance tracking
    
# Implementation details
def monitor_performance(log_level="DEBUG", threshold_seconds=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                execution_time = time.time() - start_time
                
                # Conditional logging based on threshold
                if threshold_seconds is None or execution_time >= threshold_seconds:
                    logger.log(log_level, f"{func.__name__} executed in {execution_time:.4f} seconds")
                    
                return result
            except Exception as e:
                execution_time = time.time() - start_time
                logger.error(f"{func.__name__} failed after {execution_time:.4f} seconds")
                raise
```

##### **Smart Error Handling and Context Preservation**
```python
# Exception hierarchy with rich context (exceptions.py)
class AutomationException(Exception):
    def __init__(self, message, details=None, context=None, 
                 original_exception=None, operation="unknown", test_case=None):
        self.message = message
        self.details = details or ""
        self.context = context or {}
        self.original_exception = original_exception
        self.operation = operation
        self.test_case = test_case
        self.timestamp = datetime.now()
        self.traceback = traceback.format_exc() if original_exception else ""
    
    # Rich error reporting
    def to_dict(self):
        return {
            'type': self.__class__.__name__,
            'message': self.message,
            'details': self.details,
            'context': self.context,
            'operation': self.operation,
            'test_case': self.test_case,
            'timestamp': self.timestamp.isoformat(),
            'original_exception': str(self.original_exception) if self.original_exception else None
        }
    
    def get_full_message(self, include_traceback=False):
        # Comprehensive error message with full context
```

##### **Notification System Integration**
```python
# Multi-channel notifications (report_methods.py)
class ReportMethods:
    def prepare_message(self):
        # Intelligent report generation
        unique_failures = list(dict.fromkeys(TC_NAME))  # Deduplicate failures
        
        txt = f"AFFILIATE 12BET AUTOMATION REPORT\n"
        txt += f"📅 Date: {timestamp}\n"
        txt += f"📋 Test Suite: {self.FuncName}\n"
        txt += f"🌐 Environment: {self.env.upper()}\n"
        
        if unique_failures:
            txt += f"⚠️ Status: FAILED ({len(unique_failures)} test cases)\n"
            for idx, tc in enumerate(unique_failures, 1):
                txt += f"{idx}. {str(tc).replace('_', ' ')}\n"
        else:
            txt += f"✅ Status: PASSED (All test cases)\n"
            
    def send_message_to_slack(self):
        # Automatic Slack notifications with rich formatting
        
    def send_message_to_telegram(self):
        # Telegram integration with test results
        
    def send_message_to_team(self):
        # MS Teams notifications
```

##### **Resource Management and Cleanup**
```python
# Automatic resource cleanup (utilities.__init__.py)
def destroy(self):
    try:
        # Send notifications before cleanup
        self.send_message_to_slack()
        
        if ENABLE_BROWSER:
            if ENABLE_TRACE:
                # Save Playwright trace for debugging
                self.context.tracing.stop(path=TRACE_PATH)
            self.browser.close()
            self.playwright.stop()
        
        # Clear test case tracking
        self.tcsF.clear()
        if hasattr(self, 'page'): self.page.TcName.clear()
        if hasattr(self, 'api'): self.api.TcName.clear()
        if hasattr(self, 'db'): self.db.TcName.clear()
            
    except Exception as e:
        logger.error(f"Error during cleanup: {str(e)}")
```

##### **Smart Waiting and Network Optimization**
```python
# Intelligent waiting strategies (waits.py)
class SmartWaits:
    def wait_for_element_ready(self, selector, timeout=None):
        # Multi-step element readiness checking:
        # 1. Element attachment to DOM
        # 2. Element visibility
        # 3. Element stability (position doesn't change)
        # 4. Element interactability
        
    def adaptive_wait(self, base_seconds=1.0, reason="operation"):
        # Adaptive waiting based on system performance
        start = time.time()
        self.page.evaluate("document.readyState")
        response_time = time.time() - start
        
        if response_time > 0.5:
            actual_wait = base_seconds * 1.5  # Slow system
        elif response_time < 0.1:
            actual_wait = base_seconds * 0.7  # Fast system
        else:
            actual_wait = base_seconds  # Normal timing
            
    def wait_for_network_idle(self, timeout=30, idle_time=500):
        # Network activity monitoring for AJAX-heavy applications
```

This comprehensive monitoring and tracking system provides:
- **Real-time Performance Metrics**: Execution time tracking for all operations
- **Automatic Test Result Reporting**: Integration with Google Sheets for historical data
- **Multi-channel Notifications**: Slack, Telegram, and MS Teams alerts
- **Rich Error Context**: Detailed exception information with full context
- **Resource Management**: Automatic cleanup and trace collection
- **Adaptive Performance**: System-aware waiting and retry strategies
- **Test Case Tracking**: Global failure tracking across all test runs

### Core Components

#### 1. Core Utilities (`src/utils/core/`)

- **decorators.py**: Provides decorators for retry logic, performance monitoring, and error handling
- **exceptions.py**: Custom exception hierarchy for different error types
- **logging.py**: Advanced logging system with colored output and multiple levels
- **validation.py**: Input validation utilities
- **utils.py**: Common utility functions and singleton pattern implementation

#### 2. Service Layer (`src/utils/services/`)

**API Testing Services:**
- Request methods (GET, POST, PUT, DELETE)
- Response assertion and validation
- JSON path extraction
- API performance monitoring

**Database Services:**
- SQL Server connection management
- Query execution with transaction support
- Data insertion and validation
- Connection pooling and cleanup

**Page Automation Services:**
- Element interactions (click, input, select)
- Smart waiting strategies
- Frame and popup handling
- Screenshot and video recording
- Navigation and verification

**Utility Services:**
- Browser lifecycle management
- File operations and Excel handling
- Google Sheets integration
- Cryptographic operations
- Multi-channel reporting

#### 3. Page Object Model

The framework implements a clean Page Object Model pattern:

```python
# Example: demo_elements.py
class DemoElements:
    # Search functionality
    lbl_search_by = "//label[text()='Search By']"
    sel_search_by = "//select[@name='searchBy']"
    btn_search = "//button[contains(@class, 'btn-outline-primary')]"
    
    # Table elements
    tbl_message = "//div[@class='message-content']//table"
    th_creator = "//th[@title='Creator']"
    td_creator = "//td[@class='text-center' and @title]"
```

#### 4. Action Layer

Business logic is encapsulated in action classes:

```python
# Example: action_demo.py
class ActionDemo(Common):
    def verify_ui_message_page(self, testcase):
        mainChecklist = [
            "Verify that the button 'Add' is displayed",
            "Verify that the button 'Delete' is displayed"
        ]
        
        # Test implementation with Google Sheets reporting
        self.utils.update_result_to_ggsheet(
            Data["TestCase_spread_sheet_id"], 
            mainChecklist[0], 
            testcase, 
            subAutoTestCase, 
            Data["TestCase_Auto_Status"][0],
            sheet_name="Demo_Message"
        )
```

## 🚦 Usage

### Running Tests

#### Basic Test Execution

```bash
# Run all tests with default settings
pytest

# Run specific test file
pytest test_suites/TestSuites_01_Demo.py

# Run with custom environment and browser
pytest --env=uat --browser=firefox --headless=true

# Run with debug mode
pytest --env=local --debug_mode=true
```

#### Advanced Execution Options

```bash
# Run tests in parallel
pytest -n auto

# Generate detailed HTML report
pytest --html=reports/detailed_report.html --self-contained-html

# Run specific test markers
pytest -m smoke
pytest -m functional
pytest -m e2e

# Run with custom configurations
pytest --env=prod --site=user --browser=chromium --headless=false
```

### Command Line Options

| Option | Default | Description |
|--------|---------|-------------|
| `--env` | `local` | Environment: local, uat, prod |
| `--site` | `admin` | Site type: admin, user |
| `--browser` | `chrome` | Browser: chrome, chromium, firefox, safari |
| `--headless` | `false` | Run in headless mode: true, false |
| `--debug_mode` | `false` | Enable debug logging: true, false |

### Important Note: Assertion Methods

The framework provides two types of assertion methods:

#### API-Specific Assertions (api service)
```python
# Use for API response validation
self.utils.api.assert_status_code(response, 200)
self.utils.api.assert_response_contains(response, "expected_text")
```

#### General Utility Assertions (utilities service)  
```python
# Use for general data validation
self.utils.should_be_equal(actual_value, expected_value)
self.utils.should_contain(text, "substring")
self.utils.should_be_greater_than_or_equal(count, 1)
self.utils.should_not_contain(text, "unwanted_text")
```

## 📝 Step-by-Step Test Implementation Guide

### Overview: Framework Architecture Understanding

Before implementing any test case, you need to understand the framework's layered architecture:

```
📁 Your Test Implementation
├── 🎯 Test Suite Layer (TestSuites_XX_YourModule.py)
├── 🎬 Action Layer (src/actions/your_module.py) 
├── 📄 Page Object Layer (src/interfaces/your_elements.py)
├── 📊 Test Data Layer (src/test_data/your_test_data.py)
└── 🔧 Common Base (src/actions/common/action_common.py)
```

### Step 1: Understanding the Framework Flow

The framework follows this execution pattern:

1. **Test Suite** calls **Action Method**
2. **Action Method** uses **Page Elements** to interact with UI
3. **Action Method** uses **Test Data** for input values
4. **Action Method** reports results to **Google Sheets**
5. **Framework** handles errors and notifications automatically

### Step 2: Create Page Elements (Page Object Model)

**File Location**: `src/interfaces/your_module_elements.py`

**Purpose**: Define all UI elements using XPath locators

```python
# Example: src/interfaces/login_elements.py
class LoginElements:
    # Input fields
    inp_username = "//input[@name='username']"
    inp_password = "//input[@type='password']"
    
    # Buttons
    btn_login = "//button[@type='submit']"
    btn_forgot_password = "//a[contains(text(), 'Forgot Password')]"
    
    # Messages
    msg_error = "//div[@class='error-message']"
    msg_success = "//div[@class='success-message']"
    
    # Navigation elements
    lnk_dashboard = "//a[contains(@href, '/dashboard')]"
    
    # Form containers
    frm_login = "//form[@id='loginForm']"
    div_login_container = "//div[@class='login-container']"
```

**📚 Best Practices for Elements:**
- Use semantic names: `inp_username` not `input1`
- Group by functionality: inputs, buttons, messages
- Use stable locators: prefer `@id`, `@name` over complex paths
- Add comments for complex selectors

### Step 3: Create Test Data Management

**File Location**: `src/test_data/your_module_test_data.py`

**Purpose**: Centralize all test data and provide dynamic data generation

```python
# Example: src/test_data/login_test_data.py
from datetime import datetime

class LoginTestData:
    # Static test data
    valid_credentials = {
        "username": "admin",
        "password": "password123"
    }
    
    invalid_credentials = {
        "username": "invalid_user",
        "password": "wrong_password"
    }
    
    # API request templates
    api_templates = {
        "login_request": {
            "method": "POST",
            "headers": {"content-type": "application/json"},
            "body": {
                "username": "",
                "password": "",
                "remember_me": False
            }
        }
    }
    
    # Dynamic data generation
    @staticmethod
    def get_current_timestamp():
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    @classmethod
    def get_test_user(cls, user_type="admin"):
        base_data = {
            "created_date": cls.get_current_timestamp(),
            "status": "active"
        }
        
        user_types = {
            "admin": {**base_data, "username": "admin_user", "role": "administrator"},
            "normal": {**base_data, "username": "normal_user", "role": "user"}
        }
        
        return user_types.get(user_type, base_data)
```

### Step 4: Create Action Class (Business Logic)

**File Location**: `src/actions/your_module.py`

**Purpose**: Implement test logic and integrate with Google Sheets reporting

```python
# Example: src/actions/action_login.py
from src.actions.common.action_common import Common
from src.interfaces.login_elements import LoginElements as elm_login
from src.test_data.login_test_data import LoginTestData as data_login
from config.constants.settings import *
from src.test_data.common.data_common import *

# Google Sheets configuration
Data = {
    "TestCase_spread_sheet_id": TestCase_Spread_Sheet_Id,
    "TestCase_Auto_Status": TestCase_Auto_Status,
}
Checklist_Sheet_Name = "Login_Tests"

class ActionLogin(Common):
    
    def verify_login_functionality(self, testcase):
        """
        Test Method: Verify login functionality with valid and invalid credentials
        """
        try:
            # Define test checklist for Google Sheets reporting
            mainChecklist = [
                "Verify that login form is displayed correctly",
                "Verify that valid credentials allow successful login",
                "Verify that invalid credentials show error message",
                "Verify that user is redirected to dashboard after login"
            ]
            subAutoTestCase = ''
            indexChl = 0
            
            # Test Step 1: Verify login form display
            subAutoTestCase += f"- Navigate to login page and verify form elements"
            
            # Navigate to login page
            self.utils.page.navigate("https://your-app.com/login")
            self.utils.page.wait_for_element_ready(elm_login.frm_login, visible=True, enabled=True)
            
            # Verify form elements exist
            self.utils.page.verify_element_exist(elm_login.inp_username)
            self.utils.page.verify_element_exist(elm_login.inp_password)
            self.utils.page.verify_element_exist(elm_login.btn_login)
            
            subAutoTestCase += f"\n     + Login form displayed successfully"
            subAutoTestCase += f"\n     + Username field: {self.utils.page.does_element_exist(elm_login.inp_username)}"
            subAutoTestCase += f"\n     + Password field: {self.utils.page.does_element_exist(elm_login.inp_password)}"
            subAutoTestCase += f"\n     + Login button: {self.utils.page.does_element_exist(elm_login.btn_login)}"
            
            # Report to Google Sheets
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],  # 0 = Passed
                sheet_name=Checklist_Sheet_Name
            )
            indexChl += 1
            subAutoTestCase = ''
            
            # Test Step 2: Valid login test
            subAutoTestCase += f"- Test login with valid credentials"
            
            valid_creds = data_login.valid_credentials
            self.utils.page.input(elm_login.inp_username, valid_creds["username"])
            self.utils.page.input(elm_login.inp_password, valid_creds["password"])
            self.utils.page.click(elm_login.btn_login)
            
            # Wait for navigation
            self.utils.page.wait_for_element_ready(elm_login.lnk_dashboard, visible=True, enabled=True)
            
            subAutoTestCase += f"\n     + Username entered: {valid_creds['username']}"
            subAutoTestCase += f"\n     + Password entered: [HIDDEN]"
            subAutoTestCase += f"\n     + Login successful: Dashboard link visible"
            
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
            
            # Test Step 3: Invalid login test  
            subAutoTestCase += f"- Test login with invalid credentials"
            
            # Navigate back to login
            self.utils.page.navigate("https://your-app.com/login")
            self.utils.page.wait_for_element_ready(elm_login.frm_login, visible=True, enabled=True)
            
            invalid_creds = data_login.invalid_credentials
            self.utils.page.input(elm_login.inp_username, invalid_creds["username"])
            self.utils.page.input(elm_login.inp_password, invalid_creds["password"])
            self.utils.page.click(elm_login.btn_login)
            
            # Verify error message appears
            self.utils.page.wait_for_element_ready(elm_login.msg_error, visible=True, enabled=True)
            error_text = self.utils.page.get_text(elm_login.msg_error)
            
            subAutoTestCase += f"\n     + Invalid username: {invalid_creds['username']}"
            subAutoTestCase += f"\n     + Invalid password: [HIDDEN]"
            subAutoTestCase += f"\n     + Error message displayed: {error_text}"
            
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
            
            # Test Step 4: Dashboard redirection
            subAutoTestCase += f"- Verify dashboard redirection after successful login"
            
            # Login again with valid credentials
            self.utils.page.input(elm_login.inp_username, valid_creds["username"])
            self.utils.page.input(elm_login.inp_password, valid_creds["password"])
            self.utils.page.click(elm_login.btn_login)
            
            # Verify URL contains dashboard
            current_url = self.utils.page.get_current_url()
            dashboard_in_url = "dashboard" in current_url.lower()
            
            subAutoTestCase += f"\n     + Current URL: {current_url}"
            subAutoTestCase += f"\n     + Dashboard in URL: {dashboard_in_url}"
            subAutoTestCase += f"\n     + Redirection successful: {dashboard_in_url}"
            
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][0],
                sheet_name=Checklist_Sheet_Name
            )
            
        except Exception as e:
            # Error handling: Report failure to Google Sheets
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[indexChl], 
                testcase, 
                subAutoTestCase, 
                Data["TestCase_Auto_Status"][1],  # 1 = Failed
                sheet_name=Checklist_Sheet_Name
            )
            
            # Mark remaining checklist items as "Not-Test"
            indexChl += 1
            if indexChl < len(mainChecklist):
                for i in range(indexChl, len(mainChecklist)):
                    self.utils.update_result_to_ggsheet(
                        Data["TestCase_spread_sheet_id"], 
                        mainChecklist[i], 
                        testcase, 
                        "", 
                        Data["TestCase_Auto_Status"][2],  # 2 = Not-Test
                        sheet_name=Checklist_Sheet_Name
                    )
            
            # Extract and log the error
            self.utils.page.extract_TestCaseFailed(e)
```

### Step 5: Create Test Suite

**File Location**: `test_suites/TestSuites_XX_YourModule.py`

**Purpose**: Execute test methods with proper setup and teardown

```python
# Example: test_suites/TestSuites_02_Login.py
# Must import, please don't fix it
import sys
from os.path import dirname as d
from os.path import abspath, join
root_dir = d(d(abspath(__file__)))
sys.path.append(root_dir)
import unittest
import inspect
import pytest
unittest.TestLoader.testMethodPrefix = "TestCase"
unittest.TestLoader.sortTestMethodsUsing = None

# Import your action class
from src.actions.action_login import ActionLogin
from src.utils.core.decorators import measure_test_execution_time

class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Setup executed once before all test methods"""
        cls.LoginFunc = ActionLogin()
        cls.LoginFunc.setup()  # Initialize browser and login to admin
        cls.utils = cls.LoginFunc.utils
    
    @classmethod
    def tearDownClass(cls):
        """Cleanup executed once after all test methods"""
        cls.LoginFunc.tearDown()  # Close browser and send notifications
    
    @pytest.mark.login  # Test marker for selective execution
    @measure_test_execution_time  # Automatic execution time tracking
    def TestCase_001_Verify_Login_Functionality(self):
        """Test Case 001: Verify complete login functionality"""
        # Get current test method name automatically
        test_method_name = inspect.currentframe().f_code.co_name
        
        # Execute the test
        self.LoginFunc.verify_login_functionality(test_method_name)
    
    @pytest.mark.login
    @measure_test_execution_time
    def TestCase_002_Verify_Password_Reset_Functionality(self):
        """Test Case 002: Verify password reset functionality"""
        test_method_name = inspect.currentframe().f_code.co_name
        self.LoginFunc.verify_password_reset_functionality(test_method_name)
```

### Step 6: Essential Framework Patterns

#### 6.1 Google Sheets Integration Pattern

```python
# Always follow this pattern for reporting
self.utils.update_result_to_ggsheet(
    Data["TestCase_spread_sheet_id"],    # Spreadsheet ID from data_common.py
    mainChecklist[indexChl],             # Current checklist item (Column C)
    testcase,                            # Test method name (Column E - Auto_Testcase)
    subAutoTestCase,                     # Detailed test steps (Column F - Sub_Auto_Testcases)
    Data["TestCase_Auto_Status"][0],     # Status: 0=Passed, 1=Failed, 2=Not-Test
    sheet_name=Checklist_Sheet_Name      # Sheet name in Google Sheets
)
```

**📋 Google Sheets Column Mapping:**
- **Column C (Checklist)**: `mainChecklist[indexChl]` - Test step description
- **Column E (Auto_Testcase)**: `testcase` - EXACT test method name from TestSuites file
- **Column F (Sub_Auto_Testcases)**: `subAutoTestCase` - Detailed execution log
- **Column G/H/I (Local/UAT/PRO)**: Automatic environment-specific result updates
- **Column J (Latest Date Run)**: Automatic timestamp updates
- **Column K (Latest Env Run)**: Automatic environment tracking
- **Column L (Duration)**: Automatic execution time tracking (via @measure_test_execution_time)

**⚠️ CRITICAL: The `testcase` parameter MUST be the exact method name:**
```python
def TestCase_04_verify_marketing_pages_total_clicks_match_referrers(self):
    """Test Case 004: Verify marketing pages total clicks match referrers"""
    # Get current test method name automatically
    test_method_name = inspect.currentframe().f_code.co_name
    
    # Pass EXACT method name to Google Sheets
    self.YourFunc.verify_marketing_pages_total_clicks_match_referrers(test_method_name)
    #                                                                 ^^^^^^^^^^^^^^^^
    #                                                    This goes to Column E exactly
```

#### 6.2 Error Handling Pattern

```python
try:
    # Your test logic here
    pass
except Exception as e:
    # Report current step as failed
    self.utils.update_result_to_ggsheet(
        Data["TestCase_spread_sheet_id"], 
        mainChecklist[indexChl], 
        testcase, 
        subAutoTestCase, 
        Data["TestCase_Auto_Status"][1],
        sheet_name=Checklist_Sheet_Name
    )
    
    # Mark remaining steps as "Not-Test"
    indexChl += 1
    if indexChl < len(mainChecklist):
        for i in range(indexChl, len(mainChecklist)):
            self.utils.update_result_to_ggsheet(
                Data["TestCase_spread_sheet_id"], 
                mainChecklist[i], 
                testcase, 
                "", 
                Data["TestCase_Auto_Status"][2],
                sheet_name=Checklist_Sheet_Name
            )
    
    # Extract error for logging and notifications
    self.utils.page.extract_TestCaseFailed(e)
```

#### 6.3 Common Utilities Usage

```python
# Page interactions
self.utils.page.navigate("https://example.com")
self.utils.page.input(element_selector, "text_value")
self.utils.page.click(element_selector)
self.utils.page.wait_for_element_ready(element_selector, visible=True, enabled=True)

# Assertions (use utilities service for general validation)
self.utils.should_be_equal(actual_value, expected_value)
self.utils.should_contain(text, "substring")
self.utils.should_be_greater_than_or_equal(count, 1)

# API testing (use api service for API-specific validation)
response = self.utils.api.get("https://api.example.com/endpoint")
self.utils.api.assert_status_code(response, 200)
self.utils.api.assert_response_contains(response, "expected_text")

# Database operations
self.utils.db.connect("server_name", "database_name")
results = self.utils.db.query_and_get_all("SELECT * FROM users")
self.utils.db.close()
```

### Step 7: Advanced Implementation Tips

#### 7.1 Data-Driven Testing

```python
def verify_login_with_multiple_users(self, testcase):
    """Test login with multiple user types"""
    user_types = ["admin", "normal", "guest"]
    
    for user_type in user_types:
        subAutoTestCase += f"\n\n→ Testing {user_type} login:"
        
        user_data = data_login.get_test_user(user_type)
        
        # Perform login test for this user type
        self.utils.page.input(elm_login.inp_username, user_data["username"])
        # ... rest of login logic
        
        subAutoTestCase += f"\n     + User type: {user_type}"
        subAutoTestCase += f"\n     + Username: {user_data['username']}"
        subAutoTestCase += f"\n     + Login result: {'Success' if success else 'Failed'}"
```

#### 7.2 Complex UI Interactions

```python
# Using helper methods from Common class
super().select_date_picker(elm_form.inp_date, "05-16-2025")
super().select_multiple_option(elm_form.div_options, ["Option1", "Option2"])
super().go_to_next_page()  # For pagination
```

#### 7.3 API Integration Testing

```python
def verify_api_integration(self, testcase):
    """Test API endpoints integration"""
    
    # Get data via API
    response = self.utils.api.get("https://api.example.com/users")
    self.utils.api.assert_status_code(response, 200)
    
    api_data = response.json()
    api_username = self.utils.api.extract_by_jsonpath(response, "$.users[0].name")
    
    # Compare with UI data
    ui_username = self.utils.page.get_text(elm_profile.lbl_username)
    self.utils.should_be_equal(api_username, ui_username)
```

### Step 8: Running Your Tests

```bash
# Run specific test file
pytest test_suites/TestSuites_02_Login.py

# Run with specific markers
pytest -m login

# Run with custom environment
pytest --env=staging --browser=chrome test_suites/TestSuites_02_Login.py

# Run with debug mode
pytest --debug_mode=true -s -v test_suites/TestSuites_02_Login.py
```

### Step 9: Best Practices Summary

#### ✅ DO:
- **Inherit from Common**: Always extend `Common` class for action classes
- **Use Page Objects**: Define all elements in separate element classes
- **Follow Naming Conventions**: `TestCase_XXX_Descriptive_Name` for test methods
- **Report Everything**: Use Google Sheets integration for all test steps
- **Handle Errors Properly**: Use the framework's error handling pattern
- **Use Framework Utilities**: Leverage `self.utils` for all interactions
- **Add Detailed Logging**: Include descriptive `subAutoTestCase` content

#### ❌ DON'T:
- **Skip Error Handling**: Never leave try-catch blocks empty
- **Hardcode Values**: Use test data classes instead
- **Ignore Framework Patterns**: Don't create custom reporting mechanisms
- **Mix Assertion Types**: Use api-specific assertions for APIs, utilities for general
- **Forget Cleanup**: Always call `tearDown()` in test classes
- **Skip Documentation**: Comment complex test logic

### Step 10: Debugging and Troubleshooting

#### Common Issues and Solutions:

1. **Element Not Found**:
   ```python
   # Use explicit waits
   self.utils.page.wait_for_element_ready(element, timeout=30)
   
   # Check if element exists before interaction
   if self.utils.page.does_element_exist(element):
       self.utils.page.click(element)
   ```

2. **Google Sheets Integration Issues**:
   - Verify `TestCase_Spread_Sheet_Id` in `data_common.py`
   - Check Google Service Account permissions  
   - Ensure sheet name matches `Checklist_Sheet_Name`
   - **CRITICAL**: Verify Column E (Auto_Testcase) contains exact method names
   - **CRITICAL**: Verify all 12 columns (A-L) are set up correctly
   ```python
   # Column E must match your test method exactly:
   def TestCase_04_verify_marketing_pages_total_clicks_match_referrers(self):
   # Column E value: TestCase_04_verify_marketing_pages_total_clicks_match_referrers
   ```

3. **Test Data Management**:
   ```python
   # Use dynamic data for time-sensitive tests
   timestamp = data_login.get_current_timestamp()
   unique_username = f"user_{timestamp}"
   ```

4. **Environment Configuration**:
   ```python
   # Use environment-specific data
   if ENVIRONMENT == "staging":
       base_url = "https://staging.example.com"
   else:
       base_url = "https://example.com"
   ```

Remember: The framework is designed to make testing easier, not harder. Follow these patterns consistently, and you'll have robust, maintainable, and well-documented test automation! 🚀

---

### Writing Tests

#### 1. Basic Test Structure

```python
import unittest
import pytest
from src.actions.action_demo import ActionDemo
from src.utils.core.decorators import measure_test_execution_time

class Demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.demo_func = ActionDemo()
        cls.demo_func.setup()
        cls.utils = cls.demo_func.utils

    @classmethod
    def tearDownClass(cls):
        cls.demo_func.tearDown()

    @pytest.mark.demo
    @measure_test_execution_time
    def TestCase_001_Verify_UI_Message_Page(self):
        self.demo_func.verify_ui_message_page(
            inspect.currentframe().f_code.co_name
        )
```

#### 2. Test Data Management

```python
# test_data/demo_test_data.py
class DemoTestData:
    test_data = {
        "creator": "AAVictor",
        "message": "test message",
        "important": "Yes"
    }
    
    @classmethod
    def get_test_data(cls, scenario="default"):
        base_data = {
            "creator": "AAVictor",
            "created_date": cls.get_current_timestamp(),
            "message": "test message"
        }
        scenarios = {
            "urgent": {**base_data, "priority": "urgent"},
            "normal": {**base_data, "priority": "normal"}
        }
        return scenarios.get(scenario, base_data)
```

#### 3. Page Interactions

```python
# Basic page interactions
self.utils.page.navigate("https://example.com")
self.utils.page.input("//input[@name='username']", "testuser")
self.utils.page.click("//button[@type='submit']")
self.utils.page.wait_for_element_ready("//div[@id='dashboard']")

# Advanced interactions
self.utils.page.select_options("//select[@name='country']", "US")
self.utils.page.upload_file("//input[@type='file']", "test_file.pdf") 
self.utils.page.screenshot("test_screenshot.png")

# Robust interactions with retry and scrolling
self.utils.page.click_with_retry("//button[@id='submit']", max_attempts=3)
self.utils.page.scroll_to_element("//div[@id='bottom']")
self.utils.page.hover("//div[@class='tooltip-trigger']")

# Key press and multiple selections
self.utils.page.press_key("Enter", "//input[@name='search']")
self.utils.page.select_multiple("//label", ["Option1", "Option2"])
```

#### 4. API Testing

```python
# API requests
response = self.utils.api.get("https://api.example.com/users")
self.utils.api.assert_status_code(response, 200)

# Alternative using utilities assertion methods
self.utils.should_be_equal(response.status, 200)

# JSON validation and assertions
data = response.json()
self.utils.should_contain(data["users"][0]["name"], "John")
self.utils.api.assert_response_contains(response, "John")
```

#### 5. Database Testing

```python
# Database operations
self.utils.db.connect("server", "database")
results = self.utils.db.query_and_get_all("SELECT * FROM users WHERE active = 1")
self.utils.should_be_greater_than_or_equal(len(results), 1)

# Alternative: Simple query for non-SELECT operations
self.utils.db.query("UPDATE users SET status = 'active' WHERE id = 1", 'update')

# Close connection
self.utils.db.close()
```

## 📊 Reporting and Monitoring

### Google Sheets Integration

The framework automatically reports test results to Google Sheets with:
- Test execution status (Passed/Failed/Not-Test)
- Execution duration
- Environment information
- Detailed error messages
- Historical test data

### Notification System

Multi-channel notifications are sent after test execution:

#### Slack Integration
```python
# Automatic Slack notifications
self.utils.send_message_to_slack()
```

#### Telegram Integration
```python
# Automatic Telegram notifications
self.utils.send_message_to_telegram()
```

#### MS Teams Integration
```python
# Automatic Teams notifications
self.utils.send_message_to_team()
```

### Logging and Debugging

#### Log Levels
- **TRACE**: Detailed debugging information
- **DEBUG**: General debugging information
- **INFO**: General information messages
- **WARNING**: Warning messages
- **ERROR**: Error messages
- **CRITICAL**: Critical error messages

#### Log Output
```
2024-01-15 10:30:45 - automation.page - INFO - Navigating to URL: https://example.com
2024-01-15 10:30:46 - automation.element - DEBUG - Clicking element: //button[@id='submit']
2024-01-15 10:30:47 - automation.api - DEBUG - GET request to https://api.example.com returned status code 200
```

### Performance Monitoring

The framework includes built-in performance monitoring:
- Test execution time tracking
- Browser performance metrics
- API response time monitoring
- Database query performance
- Memory usage tracking

## 🔧 Advanced Configuration

### Custom Decorators

The framework provides powerful decorators for common testing patterns:

#### Retry Decorator
```python
@retry(max_attempts=3, delay_seconds=2.0, backoff_factor=2.0)
def unstable_operation(self):
    # This will retry up to 3 times with exponential backoff
    pass
```

#### Performance Monitoring
```python
@monitor_performance(threshold_seconds=5.0)
def slow_operation(self):
    # This will log execution time if > 5 seconds
    pass
```

#### Exception Handling
```python
@log_exceptions(log_level="ERROR", re_raise=True)
def risky_operation(self):
    # This will log exceptions and optionally re-raise
    pass
```

### Custom Exceptions

The framework includes a comprehensive exception hierarchy:

```python
try:
    self.utils.page.click("//button[@id='missing']")
except ElementNotFoundException as e:
    logger.error(f"Element not found: {e.selector}")
    # Handle missing element gracefully
```

### Smart Waiting Strategies

Advanced waiting mechanisms for reliable test execution:

```python
# Wait for element to be ready
self.utils.page.wait_for_element_ready("//button[@id='submit']", 
                                      visible=True, 
                                      enabled=True, 
                                      stable=True)

# Wait for network to be idle
self.utils.page.wait_for_network_idle(timeout=30)

# Wait for custom condition
self.utils.page.wait_for_condition(
    lambda: len(self.utils.page.get_elements("//tr")) > 5,
    description="table to have more than 5 rows",
    timeout=15
)
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Browser Installation Issues
```bash
# Reinstall Playwright browsers
playwright install --force

# Install specific browser
playwright install chromium
```

#### 2. Environment Configuration Issues
- Verify environment files exist in correct locations
- Check file permissions and encoding (UTF-8)
- Validate environment variable syntax

#### 3. Database Connection Issues
- Verify SQL Server is accessible
- Check firewall settings
- Validate connection string format
- Ensure database user has required permissions

#### 4. Google Sheets Permission Issues
- Verify service account JSON file is valid
- Check Google Sheets sharing permissions
- Ensure Google Sheets API is enabled

#### 5. Element Not Found Issues
```python
# Use explicit waits
self.utils.page.wait_for_element_ready(selector, timeout=30)

# Use multiple selector strategies
selectors = ["//button[@id='submit']", "//input[@value='Submit']"]
found_selector = self.utils.page.wait_for_one_of_elements(selectors)
```

### Debug Mode

Enable comprehensive debugging:

```bash
pytest --debug_mode=true --env=local -s -v
```

This provides:
- Detailed step-by-step logging
- Element interaction screenshots
- Network request/response logging
- Database query logging
- Performance metrics

### Log Analysis

Log files are stored in the `logs/` directory with timestamps:
```
logs/
├── automation_20240115_103045.log
├── automation_20240115_143022.log
└── automation_20240116_091234.log
```

## 🤝 Contributing

### Development Setup

1. Fork the repository
2. Create a feature branch
3. Install development dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```
4. Set up pre-commit hooks:
   ```bash
   pre-commit install
   ```

### Code Quality

The framework includes comprehensive code quality tools:

```bash
# Format code
black src/ test_suites/

# Sort imports
isort src/ test_suites/

# Lint code
flake8 src/ test_suites/

# Type checking
mypy src/
```

### Testing Framework Changes

```bash
# Run core framework tests
pytest test_suites/TestSuites_01_Demo.py -v

# Run with multiple environments
pytest --env=local --env=uat --browser=chromium --browser=firefox
```

## 📦 Dependencies Overview

### Core Dependencies

| Package | Version | Purpose | Documentation |
|---------|---------|---------|---------------|
| **Python** | 3.13+ | Runtime environment | [python.org](https://python.org) |
| **uv** | Latest | Fast Python package manager | [uv docs](https://docs.astral.sh/uv/) |
| **playwright** | ^1.40.0 | Browser automation | [playwright.dev](https://playwright.dev/python/) |
| **pytest** | ^7.4.0 | Test framework | [pytest.org](https://docs.pytest.org/) |
| **requests** | ^2.31.0 | HTTP client for API testing | [requests docs](https://requests.readthedocs.io/) |
| **pyodbc** | ^4.0.39 | SQL Server database connectivity | [pyodbc docs](https://github.com/mkleehammer/pyodbc) |
| **gspread** | ^5.12.0 | Google Sheets integration | [gspread docs](https://docs.gspread.org/) |
| **cryptography** | ^41.0.0 | Encryption and security | [cryptography docs](https://cryptography.io/) |

### Development Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| **black** | ^23.0.0 | Code formatting |
| **isort** | ^5.12.0 | Import sorting |
| **flake8** | ^6.0.0 | Code linting |
| **mypy** | ^1.5.0 | Type checking |
| **pre-commit** | ^3.4.0 | Git hooks |

### Browser Dependencies

The framework automatically downloads browser binaries via Playwright:
- **Chromium**: Latest stable version
- **Chrome**: System-installed or Playwright-managed
- **Firefox**: Latest stable version  
- **Safari**: macOS only (system WebKit)

### System Requirements Matrix

| Component | Windows | macOS | Linux |
|-----------|---------|-------|-------|
| **Python 3.13+** | ✅ | ✅ | ✅ |
| **Browser Automation** | ✅ | ✅ | ✅ |
| **Database (SQL Server)** | ✅ | ✅ (via ODBC) | ✅ (via ODBC) |
| **Google Sheets** | ✅ | ✅ | ✅ |
| **Notifications** | ✅ | ✅ | ✅ |

## ❓ Frequently Asked Questions (FAQ)

### 🚀 Getting Started

**Q: I'm completely new to test automation. Where should I start?**  
A: Follow this learning path:
1. Run the Quick Start guide above
2. Study the demo files: `TestSuites_01_Demo.py`, `action_demo.py`, `demo_elements.py`
3. Try modifying the demo test with your own elements
4. Read the Step-by-Step Implementation Guide
5. Create your first simple test

**Q: What programming knowledge do I need?**  
A: Basic Python knowledge is sufficient:
- Variables and functions
- Classes and inheritance
- Basic error handling (try/except)
- Understanding of XPath selectors (can be learned quickly)

**Q: How long does it take to create a simple test?**  
A: Once familiar with the framework:
- Simple UI test: 30-60 minutes
- API integration test: 45-90 minutes  
- Database validation test: 30-45 minutes

### ⚙️ Configuration

**Q: Why does my test fail with "Element not found"?**  
A: Common causes and solutions:
```python
# 1. Add explicit waits
self.utils.page.wait_for_element_ready("//button[@id='submit']", timeout=30)

# 2. Check if element exists first
if self.utils.page.does_element_exist("//button[@id='submit']"):
    self.utils.page.click("//button[@id='submit']")

# 3. Use more robust selectors
# Instead of: "//button[1]"
# Use: "//button[@id='submit']" or "//button[contains(text(), 'Submit')]"
```

**Q: How do I run tests in different environments?**  
A: Use the environment flag:
```bash
pytest --env=local --site=admin   # Local admin site
pytest --env=uat --site=user      # UAT user site  
pytest --env=prod --site=admin    # Production admin (be careful!)
```

**Q: My Google Sheets integration isn't working. What should I check?**  
A: Follow this checklist:
1. ✅ Service account JSON file exists at `config/secrets/client_secret.json`
2. ✅ Google Sheets API is enabled in Google Cloud Console
3. ✅ Sheet is shared with the service account email
4. ✅ Sheet ID is correct in `src/test_data/common/data_common.py`
5. ✅ Sheet has the **EXACT** 12 column headers (A-L) as specified in setup guide
6. ✅ Column E (Auto_Testcase) contains exact test method names from TestSuites files

**Q: Why is my test not updating Google Sheets even though it runs successfully?**  
A: The most common issue is Column E (Auto_Testcase) mismatch:
```python
# ❌ WRONG - Column E in Google Sheets
TestCase 04 verify marketing pages

# ✅ CORRECT - Column E must match exactly  
TestCase_04_verify_marketing_pages_total_clicks_match_referrers

# Your test method name in TestSuites file:
def TestCase_04_verify_marketing_pages_total_clicks_match_referrers(self):
```

**Quick fix**: Copy the exact method name from your TestSuites file and paste it into Column E.

**Q: How do I verify my Google Sheets column setup is correct?**  
A: Your sheet should look exactly like this:
```
A: Categories | B: Sub Categories | C: Checklist | D: Expectation | 
E: Auto_Testcase | F: Sub_Auto_Testcases | G: Local | H: UAT | 
I: PRO | J: Latest Date Run | K: Latest Env Run | L: Duration
```
If you have different column names or order, the framework won't work properly.

### 🏗️ Framework Architecture

**Q: I want to create a new test module. What files do I need?**  
A: For a complete module, create these 4 files:
1. `src/interfaces/your_module_elements.py` - UI elements
2. `src/test_data/your_module_test_data.py` - Test data
3. `src/actions/action_your_module.py` - Test logic
4. `test_suites/TestSuites_XX_YourModule.py` - Test execution

**Q: Can I modify files in the `src/utils/` directory?**  
A: **Generally no**. The `utils` directory contains the framework core. Modifications here affect all tests. If you need new functionality, consider:
- Creating helper methods in your action class
- Extending the `Common` base class
- Discussing framework enhancements with the team

**Q: How do I handle dynamic elements (elements that change)?**  
A: Use these strategies:
```python
# 1. Partial text matching
"//button[contains(text(), 'Submit')]"

# 2. Multiple selector options
selectors = ["//button[@id='new-submit']", "//button[@id='old-submit']"]
found = self.utils.page.wait_for_one_of_elements(selectors)

# 3. Wait for element state changes
self.utils.page.wait_for_element_ready("//button", visible=True, enabled=True)
```

### 🧪 Test Implementation

**Q: How do I test file uploads?**  
A: Use the built-in file upload method:
```python
# Upload single file
self.utils.page.upload_file("//input[@type='file']", "path/to/test_file.pdf")

# For multiple files, call multiple times or check if element supports multiple
```

**Q: How do I handle popups and alerts?**  
A: Use the frame and popup methods:
```python
# Handle JavaScript alerts
alert_text = self.utils.page.handle_alert(action="accept")  # or "dismiss"

# Handle popup windows
popup_page = self.utils.page.wait_for_popup()
popup_page.click("//button[@id='confirm']")
popup_page.close()
```

**Q: How do I run tests in parallel?**  
A: Use pytest-xdist:
```bash
# Install the plugin
uv pip install pytest-xdist

# Run tests in parallel
pytest -n auto  # Use all available cores
pytest -n 4     # Use 4 parallel processes
```

### 📊 Reporting and Debugging

**Q: Where can I find test execution logs?**  
A: Logs are stored in multiple places:
- **Console output**: Real-time execution logs
- **Log files**: `logs/automation_YYYYMMDD_HHMMSS.log`
- **Google Sheets**: Test results and execution details
- **Playwright traces**: `traces/` directory (if enabled)

**Q: How do I debug a failing test?**  
A: Use these debugging approaches:
```bash
# 1. Run with debug mode and verbose output
pytest --debug_mode=true -s -v test_suites/YourTest.py

# 2. Run in non-headless mode to see browser actions  
pytest --headless=false test_suites/YourTest.py

# 3. Add breakpoints in your code
import pdb; pdb.set_trace()

# 4. Take screenshots at specific points
self.utils.page.screenshot("debug_screenshot.png")
```

### 🚨 Common Issues

**Q: "ModuleNotFoundError" when importing framework components**  
A: Ensure you're in the correct environment:
```bash
# Activate virtual environment
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Reinstall in development mode
uv pip install -e .
```

**Q: Tests are very slow. How can I speed them up?**  
A: Optimization strategies:
1. **Use headless mode**: `--headless=true`
2. **Disable traces**: Set `ENABLE_TRACE = False` in settings
3. **Optimize selectors**: Use ID/name attributes instead of complex XPath
4. **Reduce timeouts**: Only use long timeouts when necessary
5. **Run in parallel**: Use `pytest -n auto`

**Q: How do I handle test data that changes frequently?**  
A: Use dynamic data generation:
```python
class YourTestData:
    @staticmethod
    def get_unique_user():
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return {
            "username": f"test_user_{timestamp}",
            "email": f"test_{timestamp}@example.com"
        }
```

## 📚 Additional Resources

### Documentation
- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [Google Sheets API](https://developers.google.com/sheets/api)
- [XPath Tutorial](https://www.w3schools.com/xml/xpath_intro.asp)

### Framework Examples
- Demo test implementation: `test_suites/TestSuites_01_Demo.py`
- Page object examples: `src/interfaces/demo_elements.py`
- Action class examples: `src/actions/action_demo.py`
- Test data examples: `src/test_data/demo_test_data.py`

### Learning Resources
- **Python Basics**: [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- **XPath Selectors**: [XPath Cheat Sheet](https://devhints.io/xpath)
- **Playwright Concepts**: [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)

### Support
For questions and issues:
1. Check this FAQ section first
2. Review the troubleshooting section  
3. Study the demo implementation files
4. Search existing issues in the repository
5. Create a detailed issue report with logs and error messages

## 📄 License

This framework is proprietary software developed for OT affiliate system testing.

---

**Framework Version**: 0.1.0  
**Python Version**: 3.13+  
**Last Updated**: January 2025  
**README Accuracy**: Verified and corrected against actual framework implementation

---

## 💡 Tips for Beginners

### Your First 30 Minutes with the Framework

1. **⏱️ Minutes 1-5**: Run the Quick Start guide
2. **⏱️ Minutes 6-15**: Read through `test_suites/TestSuites_01_Demo.py` line by line
3. **⏱️ Minutes 16-25**: Examine `src/actions/action_demo.py` to understand test logic
4. **⏱️ Minutes 26-30**: Look at `src/interfaces/demo_elements.py` for element definitions

### Learning Path for New Automation Engineers

#### Week 1: Foundation
- ✅ Complete Quick Start setup
- ✅ Run demo test successfully  
- ✅ Understand the 4-layer architecture (Test Suite → Action → Elements → Data)
- ✅ Create a simple test by modifying the demo

#### Week 2: Core Concepts
- ✅ Learn XPath selector basics
- ✅ Understand Google Sheets integration
- ✅ Practice error handling patterns
- ✅ Implement your first original test case

#### Week 3: Advanced Features
- ✅ API testing integration
- ✅ Database validation
- ✅ Multi-environment testing
- ✅ Custom test data management

#### Week 4: Best Practices
- ✅ Performance optimization
- ✅ Test maintenance strategies
- ✅ Debugging techniques
- ✅ Framework contribution guidelines

### Quick Reference Commands

```bash
# Essential commands you'll use daily
pytest test_suites/TestSuites_01_Demo.py              # Run demo
pytest --env=local --headless=false                   # Debug mode
pytest --env=uat --site=admin                         # Different environment
pytest -v -s test_suites/YourTest.py                  # Verbose output
pytest --debug_mode=true                              # Full debugging
```

### Remember: 
🎯 **Start small** - Modify existing tests before creating new ones  
📚 **Read the code** - The demo files are your best teachers  
🤝 **Ask questions** - Check the FAQ section first, then ask the team  
🔄 **Practice regularly** - Consistent practice builds expertise  

**Happy Testing! 🚀**
