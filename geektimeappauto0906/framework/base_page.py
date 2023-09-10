from typing import Any

import allure
import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.remote.webdriver import WebDriver

from framework.retry import retry


class BasePage:
    def __init__(self, driver=None, caps=None, yaml_file=None):

        self.methods: dict[str, list[dict]] = []
        """
        MainPage() driver==None
        WatchPage(self.driver)  driver !=None

        :param driver:
        :param caps:
        """
        if driver is not None:
            self.driver: WebDriver = driver
        else:
            if caps is None:
                caps = {}
            caps["platformName"] = "android"
            # 当界面不停变化的时候，不要等界面处于空闲状态
            caps['settings[waitForIdleTimeout]'] = 0
            caps["appium:ensureWebviewsHavePages"] = True
            caps["appium:nativeWebScreenshot"] = True
            caps["appium:newCommandTimeout"] = 3600
            caps["appium:connectHardwareKeyboard"] = True
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)

    def quit(self):
        self.driver.quit()

    def back(self):
        self.driver.back()

    @retry
    def find(self, by, value):
        r = self.driver.find_element(by, value)
        return r

    @retry
    def click(self, by, value):
        self.driver.find_element(by, value).click()
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    @retry
    def send_keys(self, by, value, text):
        self.driver.find_element(by, value).send_keys(text)
        allure.attach(body=self.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)

    def exception_handle(self):
        # 电话call
        if 'package="com.android.systemui" class="android.widget.Button" text="Decline" content-desc="Decline"' in self.driver.page_source:
            # 拒绝电话
            # self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Decline').click()
            self.click(AppiumBy.ACCESSIBILITY_ID, 'Decline')
        # 弹框 用户调查 升级 广告
        elif 'package="com.google.android.apps.nexuslauncher' in self.driver.page_source:
            package = 'com.google.android.deskclock'
            activity = "com.android.deskclock.DeskClock"
            self.driver.start_activity(package, activity)

    def load(self, path):
        with open(path, encoding='UTF-8') as f:
            self.methods = yaml.unsafe_load(f)

    def __getattr__(self, method):
        def run():
            self.run(self.methods.get(method, []))

        return run

    def run(self, steps: list[dict[str, Any]]):
        for step in steps:
            for k, v in step.items():
                print(k)
                print(v)

                k = k.lower()
                if k == 'click' and isinstance(v, dict):
                    print(v.keys())
                    print(v.values())
                    self.click(list(v.keys())[0], list(v.values())[0])
                elif k == 'send_keys':
                    self.send_keys(*v)
