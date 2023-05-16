import pytest
from pytest_practice.test_game_by_data import load_utils
import yaml


# 不知道什么原因，在一个包里也导入不了。所以只能写在一起了
def loadUtils(yaml_path):
    # 读取yaml文件
    with open(yaml_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope='function')
def data():
    print("测试开始")
    yield
    print('测试结束')


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的用例名name和用例标识nodeid的中文信息显示在控制台上
    """
    for i in items:
        i.name = i.name.encode("utf-8").decode("unicode_escape")
        i._nodeid = i.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(params=loadUtils('data.yaml')['name'])
def get_hero_name(request):
    yield request.param


@pytest.fixture(params=loadUtils('data.yaml')['volume'])
def get_hero_volume(request):
    yield request.param


@pytest.fixture(params=loadUtils('data.yaml')['power'])
def get_hero_power(request):
    yield request.param

# 导入不了同一目录下的loadutils类，所以只能注释了
# @pytest.fixture(params=loadUtils.load_yaml('data.yaml'))
# def get_hero(request):
#     yield request.param
