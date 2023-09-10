import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_cookie_get():
    driver = webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    WebDriverWait(driver, 600).until(expected_conditions.url_contains('wework_admin/frame'))
    cookies = driver.get_cookies()
    with open('../../data/cookies.json', 'w') as f:
        json.dump(cookies, f)



def test_cookie_use():
    driver=webdriver.Chrome()
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')

    with open('../../data/cookies.json') as f:
        cookies=json.load(f)

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()

    sleep(3600)


