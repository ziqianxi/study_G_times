from clock.page.main_page import MainPage


class TestClock:
    def setup_class(self):
        # app启动并进入默认的clock页面
        # BasePage("base_page.yaml")
        self.clock = MainPage()

    def setup(self):
        ...

    def test_clock(self):
        city = self.clock.add_city('beijing').get_city_list()[-1]
        assert str(city['name']).lower() == 'beijing'
        assert city['time'] - self.clock.get_default_time() == 0

        city = self.clock.add_city('tokyo').get_city_list()[-1]
        assert str(city['name']).lower() == 'tokyo'
        assert city['time'] - self.clock.get_default_time() == 1
