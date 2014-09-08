import os
import sys
from functools import partial
from PySide import QtGui, QtCore

DIR = os.path.dirname(__file__)


class SpinBox(QtGui.QSpinBox):
    '''
    Inherits QSpinBox and creates it.
    '''
    def __init__(self, name, value, parent=None):
        '''
        Our line init.
        '''
        super(SpinBox, self).__init__(parent)
        self.setObjectName(name)
        self.setMaximum(100000)
        self.setMinimum(-100000)
        self.setValue(value)


class DoubleSpinBox(QtGui.QDoubleSpinBox):
    '''
    Inherits QDoubleSpinBox and creates it.
    '''
    def __init__(self, name, value, parent=None):
        '''
        Our line init.
        '''
        super(DoubleSpinBox, self).__init__(parent)
        self.setObjectName(name)
        self.setMaximum(100000)
        self.setMinimum(-100000)
        self.setValue(value)


class ComboBox(QtGui.QComboBox):
    '''
    Inherits QComboBox and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our line init.
        '''
        super(ComboBox, self).__init__(parent)
        self.setObjectName(name)


class Label(QtGui.QLabel):
    '''
    Inherits QLabel and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our label init.
        '''
        super(Label, self).__init__(parent)

        self.setText(name)
        self.setObjectName("{0}_lbl".format(name))

        #Font.
        font = QtGui.QFont()
        font.setPointSize(10)
        self.setFont(font)


class GroupBox(QtGui.QGroupBox):
    '''
    Inherits QGroupBox and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our label init.
        '''
        super(GroupBox, self).__init__(name, parent)
        self.setObjectName("{0}_grpBox".format(name))


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
        self.resize(250, 200)
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
        Creates our OScan layout.
        '''
        self.grp_layout = GroupBox("Pixel Dimensions")

        #Width items
        self.width_Lbl = Label("Width :")
        self.width_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                     QtGui.QSizePolicy.Minimum)
        self.width_spnBox = SpinBox("width_spnBox", 1920)

        #Width layout
        self.width_boxLayout = QtGui.QHBoxLayout()
        self.width_boxLayout.addWidget(self.width_Lbl)
        self.width_boxLayout.addWidget(self.width_spnBox)

        #Width Percent/pixel comboBox.
        self.width_cmbBox = ComboBox("width_cmbBox")
        self.width_cmbBox.addItem("Percent")
        self.width_cmbBox.addItem("Pixels")
        self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 100.0)
        self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                      QtGui.QSizePolicy.Minimum)

        #Width Percent/pixel layout.
        self.ppw_boxLayout = QtGui.QHBoxLayout()
        self.ppw_boxLayout.addWidget(self.ppw_spnBox)
        self.ppw_boxLayout.addWidget(self.width_cmbBox)
        self.ppw_boxLayout.setContentsMargins(48, 0, 0, 0)

        #Height items
        self.height_Lbl = Label("Height:")
        self.height_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                      QtGui.QSizePolicy.Minimum)
        self.height_spnBox = SpinBox("height_spnBox", 1080)

        #Height Percent/pixel layout.
        self.height_cmbBox = ComboBox("height_cmbBox")
        self.height_cmbBox.addItem("Percent")
        self.height_cmbBox.addItem("Pixels")
        self.pph_spnBox = DoubleSpinBox("pph_spnBox", 100.0)
        self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                      QtGui.QSizePolicy.Minimum)

        #Height Percent/pixel layout.
        self.pph_boxLayout = QtGui.QHBoxLayout()
        self.pph_boxLayout.addWidget(self.pph_spnBox)
        self.pph_boxLayout.addWidget(self.height_cmbBox)
        self.pph_boxLayout.setContentsMargins(48, 0, 0, 0)

        #Height layout
        self.height_boxLayout = QtGui.QHBoxLayout()
        self.height_boxLayout.addWidget(self.height_Lbl)
        self.height_boxLayout.addWidget(self.height_spnBox)

        #Main layout.
        self.main_boxLayout = QtGui.QVBoxLayout()
        self.main_boxLayout.addLayout(self.width_boxLayout)
        self.main_boxLayout.addLayout(self.ppw_boxLayout)
        self.main_boxLayout.addLayout(self.height_boxLayout)
        self.main_boxLayout.addLayout(self.pph_boxLayout)

        #Set group layout.
        self.grp_layout.setLayout(self.main_boxLayout)

        #Final add to central.
        self.central_boxLayout.addWidget(self.grp_layout)

    def create_connections(self):
        '''
        Creates connections between controls.
        '''
        self.width_cmbBox.currentIndexChanged.connect(self.replaceWSpinBox)
        self.height_cmbBox.currentIndexChanged.connect(self.replaceHSpinBox)

    def replaceHSpinBox(self, index):
        '''
        Switches QSpinBox with QDoubleSpinBox.
        @param index - Index value of current spin box.
        '''
        self.pph_spnBox.deleteLater()

        if index == 1:
            self.pph_spnBox = SpinBox("pph_spnBox", 1)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                          QtGui.QSizePolicy.Minimum)
        elif index == 0:
            self.pph_spnBox = DoubleSpinBox("pph_spnBox", 100.0)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                          QtGui.QSizePolicy.Minimum)

        self.pph_boxLayout.insertWidget(0, self.pph_spnBox)

    def replaceWSpinBox(self, index):
        '''
        Switches QSpinBox with QDoubleSpinBox.
        @param index - Index value of current spin box.
        '''
        self.ppw_spnBox.deleteLater()

        if index == 1:
            self.ppw_spnBox = SpinBox("ppw_spnBox", 1)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                          QtGui.QSizePolicy.Minimum)

        elif index == 0:
            self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 100.0)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                          QtGui.QSizePolicy.Minimum)

        self.ppw_boxLayout.insertWidget(0, self.ppw_spnBox)
