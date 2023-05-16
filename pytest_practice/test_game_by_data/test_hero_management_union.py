import pytest

from pytest_practice.game.hero_management import HeroManagement
from pytest_practice.test_game_by_data.load_utils import LoadUtils




class TestHero1:
    # 完成对所有内容的测试。
    def test_create_hero_name_success(self, get_hero_name,get_hero_volume,get_hero_power):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_management = HeroManagement()
        hero_management.create_hero(get_hero_name, get_hero_volume, get_hero_power)
        res = hero_management.find_hero(get_hero_name)
        assert res.get("name") == get_hero_name
        assert res.get("volume") == get_hero_volume
        assert res.get('power') == get_hero_power