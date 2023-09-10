from utils import get_project_path


def test_get_project_dir():
    path=get_project_path('data/cookies.json')
    print(path)
    assert 'cookies.json' in path
