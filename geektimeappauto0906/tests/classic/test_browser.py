import os.path
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.classic import get_project_dir


class TestBrowser:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        # caps['appPackage'] = "io.appium.android.apis"
        # caps['appActivity'] = ".ApiDemos"
        caps['browserName'] = 'chrome'
        caps["appium:settings[waitForIdleTimeout]"] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        caps['chromedriverExecutableDir'] = os.path.join(get_project_dir(), 'bin')
        caps['showChromedriverLog'] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        self.driver.get('https://ceshiren.com')

    def test_web(self):
        self.driver.find_element(By.CSS_SELECTOR, '#search-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '.search-query').send_keys('appium')
        self.driver.find_element(By.CSS_SELECTOR, '.search-cta').click()
