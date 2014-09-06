import os
import sys
from PySide import QtGui, QtCore

DIR = os.path.dirname(__file__)

class comboBox(QtGui.QComboBox):
    '''
    Inherits QComboBox and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our line init.
        '''
        super(comboBox, self).__init__(parent)
        self.setObjectName(name)

class labelWidget(QtGui.QLabel):
    '''
    Inherits QLabel and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our label init.
        '''
        super(labelWidget, self).__init__(parent)

        self.setText(name)
        self.setObjectName("{0}_lbl".format(name))

        #Font.
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)


class UI(QtGui.QWidget):
    '''
    QMainWindow for OScan.
    '''
    def __init__(self, parent=None):
        '''
        @param parent - QMainWindow to parent to.
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
        #Width label.
        self.width_Lbl = labelWidget("Width :")
        self.height_Lbl = labelWidget("Height:")

        self.central_boxLayout.addWidget(self.width_Lbl)
        self.central_boxLayout.addWidget(self.height_Lbl)

    def create_connections(self):
        '''
        Creates connections between controls.
        '''
        pass
