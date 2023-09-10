# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


class TestClock:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        # app入口
        caps['appPackage'] = 'com.google.android.deskclock'
        caps['appActivity'] = "com.android.deskclock.DeskClock"
        # 当界面不停变化的时候，不要等界面处于空闲状态
        caps['settings[waitForIdleTimeout]'] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)
        # self.driver.get()

    @pytest.mark.parametrize('city', [
        'beijing',
        'tokyo',
        'hongkong',
    ])
    def test_add_city(self, city):
        driver = self.driver
        el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock")
        el1.click()
        el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities")
        el2.click()
        el3 = driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/search_src_text")
        el3.send_keys(city)
        el4 = driver.find_element(by=AppiumBy.ID, value="com.google.android.deskclock:id/city_name")
        el4.click()
        el4.send_keys(city)
        el5 = driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/city_name")
        el5.click()

     def test_watch(self):
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="STOPWATCH"]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Start').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Pause').click()

    def teardown_class(self):
        self.driver.quit()

