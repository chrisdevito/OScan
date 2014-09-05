import os
import sys
from PySide import QtGui, QtCore

#Relative path.
DIR = os.path.dirname(__file__)


class comboBox(QtGui.QComboBox):
    '''
    Returns a radio button for our UI.
    '''
    def __init__(self, name, parent=None):
        '''
        Our line init.
        '''
        super(comboBox, self).__init__(parent)
        self.setObjectName(name)


class UI(QtGui.QWidget):
    '''
    QMainWindow for OScan.
    '''
    def __init__(self, parent=None):
        '''
        @param parent - Window to parent to.
        '''
        super(UI, self).__init__(parent)

        self.setWindowTitle("OScan")
        self.resize(400, 400)
        self.setObjectName("OScanUI")

        with open(os.path.join(DIR, "style.css")) as f:
            self.setStyleSheet(f.read())

        #Center the window.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Our main layout
        self.central_boxLayout = QtGui.QVBoxLayout()
        self.central_boxLayout.setSpacing(2)
        self.central_boxLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.central_boxLayout)

        self.create_layout()
        self.create_connections()

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

    def create_layout(self):
        '''
        Creates our layout.
        '''
        self.typeCmboBox = comboBox("Calculate")
        self.central_boxLayout.addWidget(self.typeCmboBox)

    def create_connections(self):
        '''
        Creates connections between controls.
        '''
        pass
