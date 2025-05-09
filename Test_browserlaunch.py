import tempfile
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
import time
import pytest
from selenium.webdriver.chrome.options import Options
import logging

# Set up the Chrome WebDriver using WebDriver Manager
#driver = webdriver.Chrome()

# Create a temporary directory for the user data
# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

def testlaunch():
        print("Trial")
        #options = ChromeOptions()
        #driver=webdriver.Chrome()
        #options = ChromeOptions()
        # Set a unique user data directory for each session to avoid conflicts
        #options.add_argument("user-data-dir=/tmp/chrome-user-data")
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)



        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=options)
        driver.get("https://dev-www.astm.org/")
        time.sleep(1)
        print('Page Title:', driver.title)
        logger.info('Page Title:', driver.title)
        assert 'Home | ASTM' in driver.title
        driver.quit()