import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Browser settings
BROWSER_TYPE = os.getenv('BROWSER_TYPE', 'chromium')  # 'chromium', 'firefox', or 'webkit'
HEADLESS = os.getenv('HEADLESS', 'True') == 'True'  # Run browser in headless mode
SLOW_MO = int(os.getenv('SLOW_MO', '0'))  # Slow down execution by the specified amount of milliseconds

# Timeout settings
PAGE_LOAD_TIMEOUT = int(os.getenv('PAGE_LOAD_TIMEOUT', '30000'))  # Page load timeout in milliseconds
IMPLICIT_WAIT = int(os.getenv('IMPLICIT_WAIT', '5000'))  # Implicit wait timeout in milliseconds

# Base URL
BASE_URL = os.getenv('BASE_URL', 'https://www.saucedemo.com/')

# Test account credentials
TEST_USERNAME = os.getenv('TEST_USERNAME', 'standard_user')
TEST_PASSWORD = os.getenv('TEST_PASSWORD', 'secret_sauce')

# Screenshot settings
SCREENSHOTS_DIR = os.getenv('SCREENSHOTS_DIR', 'screenshots/')
