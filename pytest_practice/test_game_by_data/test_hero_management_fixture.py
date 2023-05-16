"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import pytest

from pytest_practice.game.hero_management import HeroManagement
from pytest_practice.test_game_by_data.load_utils import LoadUtils


# 测试类与测试类的定义
class TestHero1:
    # 完成对姓名的测试。
    def test_create_hero_name(self, get_hero_name):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_management = HeroManagement()
        hero_management.create_hero(get_hero_name, 2, 20)
        res = hero_management.find_hero(get_hero_name)
        assert res.get("name") == get_hero_name

    # 完成对血量的测试。
    def test_create_hero_volume(self, get_hero_volume):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", get_hero_volume, 20)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("volume") == get_hero_volume

    # 完成对攻击力的测试。
    def test_create_hero_power(self, get_hero_power):
        """
        边界值以及等价类场景的测试用例
        """
        # print(f"英雄AD的血量为{volume}")
        hero_management = HeroManagement()
        hero_management.create_hero("jinx", 20, get_hero_power)
        res = hero_management.find_hero("jinx")
        assert res.get("name") == "jinx"
        assert res.get("power") == get_hero_power
