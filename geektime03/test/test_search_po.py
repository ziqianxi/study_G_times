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
        self.search.search_category("话题/帖子")
        assert "话题/帖子" == self.search.get_category()
        assert 'selenium' in str(self.search.search('selenium').get_search_result()[0]).lower()

    def test_search_category_2(self):
        self.search.search_category("类别/标签")
        assert "类别/标签" == self.search.get_category()
        assert 'python' in str(self.search.search('python').get_search_result()[0]).lower()

    def test_search_category_3(self):
        self.search.search_category("用户")
        assert "用户" == self.search.get_category()
        assert 'python' in str(self.search.search('python').get_search_result()[0]).lower()

    def test_set_ftr_and_fttime(self):
        self.search.search_ftr("hogwarts")
        self.search.search_fttime("晚于", "002023-09-01")
        time.sleep(3)
        assert "hogwarts" in self.search.get_search_result()[0].lower()
        assert "after:2023-09-01" in self.search.get_search_result()[0].lower()

    # login required before testing
    def test_matching_title_only(self):
        self.search.search_matching_title_only()
        assert "in:title" in self.search.get_search_result()[0].lower()