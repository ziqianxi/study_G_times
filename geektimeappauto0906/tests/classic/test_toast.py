from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait


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

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Views")
        el1.click()

        size = self.driver.get_window_size()
        width_max = size['width']
        height_max = size['height']

        def swipe_to(driver):
            driver.swipe(width_max * 0.5, height_max * 0.8, width_max * 0.5, height_max * 0.2)
            return driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Popup Menu")

        WebDriverWait(self.driver, 10).until(swipe_to).click()

    def test_toast(self):
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Make a Popup!').click()
        self.driver.find_element(AppiumBy.CSS_SELECTOR, '[text=Search]').click()
        print(self.driver.find_element(AppiumBy.XPATH, '//*[@class="android.widget.Toast"]').text)
