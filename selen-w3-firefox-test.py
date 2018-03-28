# Ran using Python -version: 3.6.4.  
# 17:45:14.169 INFO - Detected dialect: W3C appears in the selenium-server.log
# - Max Dobeck
from selenium import webdriver
from sauceclient import SauceClient
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platformName': "Windows 10",
    'browserName': "firefox",
    'browserVersion': "latest",
    'sauce:options':{
        "name":"Firefox W3C Test",
        "seleniumVersion":"3.9.1"
    }
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
driver.maximize_window()
driver.get("https://www.google.com")

sauce_client.jobs.update_job(driver.session_id, passed=True)

driver.quit()
