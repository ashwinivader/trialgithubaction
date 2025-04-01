import tempfile
import shutil
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service
import time
import pytest

# Set up the Chrome WebDriver using WebDriver Manager
#driver = webdriver.Chrome()

# Create a temporary directory for the user data


def testlaunch():
        options = ChromeOptions()
        #driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.get("https://dev-www.astm.org/")
        time.sleep(2)
        driver.quit()