import pytest
from pytest_practice.test_game_by_data.load_utils import LoadUtils



# 不知道什么原因，又可以导入了
# import yaml
# def loadUtils(yaml_path):
#     # 读取yaml文件
#     with open(yaml_path, 'r') as f:
#         return yaml.safe_load(f)


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


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['name']["effective"])
def get_hero_name_effective(request):
    yield request.param


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['name']["Invalid"])
def get_hero_name_invalid(request):
    yield request.param


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['volume']["effective"])
def get_hero_volume_effective(request):
    yield request.param


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['volume']["Invalid"])
def get_hero_volume_invalid(request):
    yield request.param


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['power']["effective"])
def get_hero_power_effective(request):
    yield request.param


@pytest.fixture(params=LoadUtils.load_yaml('data.yaml')['power']["Invalid"])
def get_hero_power_invalid(request):
    yield request.param

