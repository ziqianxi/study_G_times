from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_browser_reuse():
    options = Options()
    options.debugger_address = '127.0.0.1:9222'
    driver = webdriver.Chrome(options=options)
    driver.get('https://ceshiren.com/t/topic/24851')


