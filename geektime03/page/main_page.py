import json

from selenium import webdriver
from selenium.webdriver.common.by import By

from geektime03.page.cookie import GetCookie
from geektime03.page.search_page import SearchPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def login():
    GetCookie.cookie_use()


class MainPage:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_topic_list(self) -> list[dict]:
        ...

    # def get_cookie(self):
    #     self.driver.get('https://ceshiren.com/')
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
    #     self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys('11sunming@163.com')
    #     self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys('ziqianxi1994428S.')
    #     self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    #     cookies = self.driver.get_cookies()
    #     with open('../data/cookies.json', 'w') as f:
    #         json.dump(cookies, f)
    #
    # def cookie_use(self):
    #     self.driver.get('https://ceshiren.com/')
    #     self.driver.implicitly_wait(30)
    #     self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
    #     with open('../data/cookies.json') as f:
    #         cookies = json.load(f)
    #
    #     for cookie in cookies:
    #         self.driver.add_cookie(cookie)
    #
    #     self.driver.refresh()
    #     return


    def to_search_advance(self) -> SearchPage:
        # 打开浏览器
        self.driver.get('https://ceshiren.com/')
        # 显式等待
        WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".d-icon-search")))
        self.driver.find_element(By.CSS_SELECTOR, '#search-button[title=搜索]').click()
        self.driver.find_element(By.CSS_SELECTOR, '.show-advanced-search').click()
        return SearchPage(self.driver)





    def close(self):
        self.driver.quit()