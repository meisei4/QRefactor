import os
from plugin.core.refactor import Refactor, update_layer_source

class QRefactorPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.refactor = Refactor()

    def initGui(self):
        # Placeholder for GUI initialization if needed in the future
        pass

    def unload(self):
        # Placeholder for GUI unload if needed in the future
        pass

    def run(self):
        # Example method to demonstrate core functionality
        update_layer_source("example_layer", "/new/path/to/layer")
