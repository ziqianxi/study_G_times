import os.path


def get_project_path(sub_path):
    return os.path.join(os.path.dirname(os.path.dirname(__file__)), sub_path)
