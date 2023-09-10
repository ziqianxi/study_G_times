import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By


class GetCookie:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def get_cookie(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys('11sunming@163.com')
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys('ziqianxi1994428S.')
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        cookies = self.driver.get_cookies()
        with open('../data/cookies.json', 'w') as f:
            json.dump(cookies, f)

    def cookie_use(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.implicitly_wait(30)
        self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
        with open('../data/cookies.json') as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

        sleep(5)

        return




# # cook = GetCookie()
# if __name__ == '__main__':
#     cook.cookie_use()
