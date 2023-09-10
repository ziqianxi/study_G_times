

from appium.webdriver.common.appiumby import AppiumBy

from page.androidwork.base_page import BasePage


class ClockPage(BasePage):

    def __init__(self):
        super(ClockPage, self).__init__()

    def check_clock_via_city(self, city):
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Clock").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Cities").click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search").click()
        el = self.driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/search_src_text")
        el.click()
        el.send_keys(city)
        self.driver.find_element(by=AppiumBy.ID, value="com.android.deskclock:id/city_name").click()

    def stopwatch(self):
        self.driver.find_element(AppiumBy.XPATH, '//*[@text="STOPWATCH"]').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Start').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Lap').click()
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Pause').click()


