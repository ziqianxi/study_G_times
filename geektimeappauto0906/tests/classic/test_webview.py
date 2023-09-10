import os.path
from time import sleep

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.classic import get_project_dir


class TestWebView:
    def setup_class(self):
        caps = {}
        caps["platformName"] = "android"
        caps['appPackage'] = "io.appium.android.apis"
        caps['appActivity'] = ".ApiDemos"
        caps["appium:settings[waitForIdleTimeout]"] = 0
        caps["appium:ensureWebviewsHavePages"] = True
        caps["appium:nativeWebScreenshot"] = True
        caps["appium:newCommandTimeout"] = 3600
        caps["appium:connectHardwareKeyboard"] = True

        caps['chromedriverExecutableDir'] = os.path.join(get_project_dir(), 'bin')
        caps['showChromedriverLog'] = True

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views")
        el1.click()

        size = self.driver.get_window_size()
        width_max = size['width']
        height_max = size['height']

        def swipe_to(driver):
            driver.swipe(width_max * 0.5, height_max * 0.8, width_max * 0.5, height_max * 0.2)
            return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WebView")

        WebDriverWait(self.driver, 10).until(swipe_to).click()

    def test_webview_native(self):
        # el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="WebView")
        # el2.click()
        for i in range(3):
            sleep(1)
            print(self.driver.contexts)
            print(self.driver.page_source)
            print("===")

        # driver.find_element(AppiumBy.ID, 'i_am_a_textbox').send_keys('ceshiren.com')
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="i has no focus"]').send_keys("ceshiren.com")

    def test_webview_context(self):
        print(self.driver.contexts)
        WebDriverWait(self.driver, 10).until(lambda x: len(self.driver.contexts) == 2)
        print(self.driver.contexts)

        print("===native===")
        print(self.driver.page_source)

        webview = self.driver.contexts[-1]
        self.driver.switch_to.context(webview)
        print("===webview===")
        print(self.driver.page_source)

        self.driver.find_element(By.CSS_SELECTOR, '#i_am_a_textbox').send_keys("ceshiren.com")


