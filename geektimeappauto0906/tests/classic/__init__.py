import os.path


def get_project_dir():
    return os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
