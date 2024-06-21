import os
from qgis.PyQt import uic
from qgis.PyQt.QtWidgets import QDialog

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'qrefactor_dialog_base.ui'))


class QRefactorDialog(QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        super(QRefactorDialog, self).__init__(parent)
        self.setupUi(self)
