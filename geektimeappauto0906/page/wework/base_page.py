import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if driver is None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver

    def refresh(self):
        self.driver.refresh()

    def click(self, by, value):
        """
        click和sendkeys可能也会抛异常，需要封装

        递归+异常处理
        :param by: 
        :param value: 
        :return: 
        """
        self.driver.find_element(by, value).click()
        self.screenshot()

    def send_keys(self, by, value, content):
        self.driver.find_element(by, value).send_keys(content)
        self.screenshot()

    def screenshot(self):
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
