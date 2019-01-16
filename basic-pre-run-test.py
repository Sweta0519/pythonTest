# Basic test with pre-run executable
from selenium import webdriver
from sauceclient import SauceClient
import time
import os

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_caps = {
    'platform': "windows 7",
    'browserName': "internet explorer",
    'version': "11.0",
    'name': "My Windows Bgrd PreRun.exe Test",
    'prerun': {
        'executable':'sauce-storage:BrowserAuthenticationAdv.exe',
        'background': 'true',
    #    'args': [ '--silent', '-a', '-q' ]
    }
}

driver = webdriver.Remote(command_executor="https://%s:%s@ondemand.saucelabs.com/wd/hub" % (username, access_key), desired_capabilities=desired_caps)
time.sleep(3)
driver.maximize_window()
driver.get("https://saucelabs.com")

driver.quit()
