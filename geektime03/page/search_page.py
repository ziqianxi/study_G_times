import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class SearchPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def search(self, keyword) -> 'SearchPage':
        # 查询并输入内容
        query = self.driver.find_element(By.CSS_SELECTOR, 'input.search-query')
        query.clear()
        query.send_keys(keyword)
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar .search-cta').click()
        return self

    def open_filter(self):
        # 打开高级选项
        advanced_filters = self.driver.find_element(By.CSS_SELECTOR, '.search-filters .advanced-filters')
        open_status = advanced_filters.get_attribute("open")
        if open_status:
            pass
        else:
            advanced_filters.click()
        return self

    def search_category(self, title):
        time.sleep(2)
        # 选择类目
        # 点击并展示层级下的列表
        self.driver.find_element(By.CSS_SELECTOR, "#search-type-header").click()
        # 获取列表的值
        select_options = self.driver.find_elements(By.CSS_SELECTOR,
                                                   '.search-bar .select-kit-body .select-kit-row')
        # option = select_options.find_elements(By.TAG_NAME, "li")
        select_options[title].click()
        return self

    def get_category(self):
        category = self.driver.find_element(By.CSS_SELECTOR, '.search-bar  .select-kit-header').get_attribute('name')
        return category

    def search_ftr(self, keyword):
        # 筛选条件增加 发帖人
        self.driver.find_element(By.CSS_SELECTOR, "#search-posted-by-header").click()
        # 定位文本框，输入内容
        self.driver.find_element(By.NAME, "filter-input-search").send_keys(keyword)
        # 再出现的结果中点击一个
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.select-kit-collection')))
        self.driver.find_element(By.CSS_SELECTOR, '[data-index="0"]').click()

    def search_fttime(self, title, date):
        # 筛选 发布时间
        time.sleep(2)
        # 点击下拉按钮
        self.driver.find_element(By.CSS_SELECTOR, "#postTime-header .select-kit-header-wrapper").click()
        # 收集所有可点值
        select_options = self.driver.find_element(By.CSS_SELECTOR, ".select-kit-collection")
        option = select_options.find_elements(By.TAG_NAME, "li")
        option[title].click()
        # 传值
        self.driver.find_element(By.CSS_SELECTOR, 'input#search-post-date').send_keys(date)
        time.sleep(2)
        return self

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '.login-button').click()
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#login-account-password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#matching-title-only')))


    def search_matching_title_only(self) -> 'SearchPage':
        # 设置标题匹配按钮
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, '#matching-title-only').click()
        return self

    def get_search_result(self) -> list[str]:
        # 显式等待
        # 匹配搜索结果
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.topic-title')))

        locator = (By.CSS_SELECTOR, '.topic-title')

        title_list = []
        for element in self.driver.find_elements(By.CSS_SELECTOR, '.topic-title'):
            title_list.append(element.text)

        return title_list

    def search_heading(self):
        # 输入框顶部高亮文字校验
        self.driver.find_element(By.CSS_SELECTOR,'.search-bar span.d-button-label').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.result-count')))
        result = self.driver.find_element(By.CSS_SELECTOR, '.search-page-heading span.term').text
        return result

    def search_text(self):
        self.driver.find_element(By.CSS_SELECTOR, '.search-bar span.d-button-label').click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#ember15')))
        result = self.driver.find_element(By.CSS_SELECTOR, '#ember15').get_attribute('value')
        return result

    def close(self):
        self.driver.quit()
