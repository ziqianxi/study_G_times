from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

import wework
from framework.base_page import BasePage
# from wework.contact.admin_page import AdminPage
from wework.contact.profile_page import ProfilePage


class ListPage(BasePage):
    _search_button = dict(by=AppiumBy.ID, value='com.tencent.wework:id/l76')
    _item = dict(by=AppiumBy.ID, value='com.tencent.wework:id/c07')
    _admin = dict(by=AppiumBy.ID, value='com.tencent.wework:id/l71')
    _input = dict(by=AppiumBy.CLASS_NAME, value='android.widget.EditText')

    def 管理(self) -> 'AdminPage':
        self.click(**self._admin)
        from wework.contact.admin_page import AdminPage
        return AdminPage(self.driver)

    def 搜索(self, keyword) -> ProfilePage:
        self.click(**self._search_button)
        self.send_keys(**self._input, text=keyword)
        self.click(**self._item)
        return ProfilePage(self.driver)

    def 浏览(self, name) -> ProfilePage:
        ...
