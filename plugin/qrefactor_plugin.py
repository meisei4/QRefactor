from qgis.PyQt.QtWidgets import QAction
from .qrefactor_dialog import QRefactorDialog


class QRefactorPlugin:
    def __init__(self, iface):
        self.action = None
        self.iface = iface
        self.dialog = None

    def unload(self):
        self.iface.removePluginMenu("QRefactor", self.action)
        self.iface.removeToolBarIcon(self.action)

    def show_dialog(self):
        if self.dialog is None:
            self.dialog = QRefactorDialog()
        self.dialog.show()
