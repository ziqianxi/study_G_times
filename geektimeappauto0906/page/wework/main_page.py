import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.wework.base_page import BasePage
from page.wework.contact_page import ContactPage
from utils import get_project_path


class MainPage(BasePage):
    def __init__(self, driver: WebDriver = None):
        """
        自动登录 进入后台
        """

        if driver is None:
            super().__init__(driver)
            self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
            self.screenshot()

            with open(get_project_path('data/cookies.json')) as f:
                cookies = json.load(f)

            for cookie in cookies:
                self.driver.add_cookie(cookie)

            self.driver.refresh()
            self.screenshot()
        else:
            ...

    def to_contact(self) -> ContactPage:
        # self.driver.find_element(By.CSS_SELECTOR, '#menu_contacts').click()
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, '通讯录').click()
        self.click(By.CSS_SELECTOR, '#menu_contacts')
        return ContactPage(self.driver)
