import time

from geektime03.page.main_page import MainPage


class TestSearchPO:

    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.search = self.main.to_search_advance()

    def teardown_class(self):
        self.main.close()

    def test_search(self):
        assert 'selenium' in str(self.search.search('selenium').get_search_result()[0]).lower()

    def test_search_category_1(self):
        self.search.search_category(0)
        assert "筛选条件：话题/帖子" == self.search.get_category()
        assert 'selenium' in str(self.search.search('selenium').get_search_result()[0]).lower()

    def test_search_category_2(self):
        self.search.search_category(1)
        assert "筛选条件：类别/标签" == self.search.get_category()

    def test_search_category_3(self):
        self.search.search_category(2)
        assert "筛选条件：用户" == self.search.get_category()

    def test_set_ftr(self):
        self.search.search_ftr("hogwarts")
        time.sleep(3)
        assert "hogwarts" in self.search.search_heading()

    def test_set_fttime(self):
        self.search.search_fttime(1, "002023-09-06")
        assert "after:2023-09-06" in self.search.search_text()
        # 这个能看到但是不太好断言

    # login required before testing
    def test_matching_title_only(self):
        self.search.login('11sunming@163.com', 'hogwarts')
        self.search.search_matching_title_only()
        # 断言输入框内选择按钮显示提示
        assert "in:title" in self.search.search_text()
