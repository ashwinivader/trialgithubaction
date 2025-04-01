from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService

# Set up the Chrome WebDriver using WebDriver Manager
#driver = webdriver.Chrome()
options = ChromeOptions()
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

# Open Google
driver.get("https://dev-www.astm.org/")

# Optional: Wait for a few seconds to see the browser (not required, just for demo purposes)
import time
time.sleep(5)

# Close the browser
driver.quit()