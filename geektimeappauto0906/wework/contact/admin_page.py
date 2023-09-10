from __future__ import annotations

from appium.webdriver.common.appiumby import AppiumBy

from framework.base_page import BasePage
from wework.contact.list_page import ListPage


class AdminPage(BasePage):
    _add_member = dict(by=AppiumBy.ID, value="com.tencent.wework:id/fuy")
    _input_username = dict(by=AppiumBy.ID, value="com.tencent.wework:id/byn")
    _input_phone = dict(by=AppiumBy.ID, value="com.tencent.wework:id/i53")
    _save = dict(by=AppiumBy.ID, value="com.tencent.wework:id/az1")
    _cancel = dict(by=AppiumBy.ID, value="com.tencent.wework:id/l6w")
    _manual = dict(by=AppiumBy.XPATH, value='//*[@text="手动输入添加"]')

    def 添加成员(self, name, phone) -> AdminPage:
        self.click(**self._add_member)
        self.click(**self._manual)
        self.send_keys(**self._input_username, text=name)
        self.send_keys(**self._input_phone, text=phone)
        self.click(**self._save)
        #利用隐式等待
        self.driver.find_element(**self._manual)
        self.back()

        return self

    def 添加子部门(self, name) -> AdminPage:
        ...

    def 修改部门名字(self, name) -> AdminPage:
        ...

    def 取消(self) -> ListPage:
        self.click(**self._cancel)
        return ListPage(self.driver)
