from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.wework.base_page import BasePage


class ContactPage(BasePage):

    def __init__(self, driver: WebDriver = None):
        super().__init__(driver)
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, '立即邀请')))

    def add_memeber(self, name, account, email=None, mobile=None, depart=None) -> 'ContactPage':
        def loop_click(driver):
            # 显式等待 有的时候有些按钮是不生效
            # self.driver.find_element(By.PARTIAL_LINK_TEXT, '添加成员').click()
            self.click(By.PARTIAL_LINK_TEXT, '添加成员')
            return self.driver.find_element(By.NAME, 'username')

        # 显式等待 可能会需要一定时间加载网页
        WebDriverWait(self.driver, 20).until(loop_click)
        # self.driver.find_element(By.NAME, 'username').send_keys(name)
        self.send_keys(By.NAME, 'username', name)
        self.driver.find_element(By.NAME, 'acctid').send_keys(account)
        # self.driver.find_element(By.NAME, 'mobile').send_keys(mobile)
        self.send_keys(By.NAME, 'mobile', mobile)
        # todo: 支持email
        self.click(By.LINK_TEXT, '保存')
        # todo

        sleep(3)

        return self

    def import_form_file(self, path) -> 'ContactPage':
        ...

    def search(self, keyword) -> 'ContactPage':
        self.driver.find_element(By.CSS_SELECTOR, '#memberSearchInput').send_keys(keyword)
        self.screenshot()
        return self

    def get_first_search_result(self) -> dict:
        # 异步加载问题
        WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.find_element(By.CSS_SELECTOR, '.member_display_cover_detail_name').text != '')
        name = self.driver.find_element(By.CSS_SELECTOR, '.member_display_cover_detail_name').text
        # 有多个相同的控件
        account = self.driver.find_elements(By.CSS_SELECTOR, '.member_display_cover_detail_bottom')[-1].text
        r = {
            'name': name,
            'account': account
        }
        print(r)
        return r
