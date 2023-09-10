import os.path

import pyyaml
import yaml

from tests.classic import get_project_dir


class PO:
    def __init__(self):
        self.methods = {}

    def load(self, path):
        with open(path, encoding='UTF-8') as f:
            self.methods = yaml.load(f)

    # def __getattribute__(self, item):
    #     print(item)

    def __getattr__(self, method):
        return lambda: self.run(self.methods.get(method, []))

    def run(self, steps: list[dict]):
        for step in steps:
            for k, v in step.items():
                if k == 'click':
                    self.driver.click(**v)
                elif k == 'send_keys':
                    self.send_keys(**v)

def test_po():
    po = PO()
    po.login()
