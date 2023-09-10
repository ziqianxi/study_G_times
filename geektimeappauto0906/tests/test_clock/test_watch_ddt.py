import os.path
from time import sleep

from clock.page.main_page import MainPage
from tests.classic import get_project_dir


class TestClock:
    def setup_class(self):
        # app启动并进入默认的clock页面
        self.watch = MainPage().to_watch()
        self.watch.load(os.path.join(get_project_dir(), 'clock', 'page', 'demo_page.yaml'))

    def teardown_class(self):
        self.watch.quit()

    def setup(self):
        ...

    def test_reset(self):
        self.watch.start2()
        sleep(1)
        self.watch.reset2()
        assert self.watch.get_total_time() == 0
