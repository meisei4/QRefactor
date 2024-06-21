import os
from qgis.utils import iface


def main():
    plugin = QRefactorPlugin(iface)


class QRefactorPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu("QRefactor", action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        # Plugin functionality goes here
        pass
