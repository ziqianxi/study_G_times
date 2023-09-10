from page.main_page import MainPage


class TestSearchPO:
    def setup_class(self):
        self.main = MainPage()

    def setup(self):
        self.search = self.main.to_search_advance()

    def teardown_class(self):
        self.main.close()

    def test_search(self):
        assert 'selenium' in str(self.search.search('selenium')
                                 .get_search_result()[0]).lower()

    def test_search2(self):
        assert 'chromedriver' in str(self.search.search('selenium chromedriver')
                                     .get_search_result()[0]).lower()
