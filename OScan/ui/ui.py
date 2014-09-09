import os
from PySide import QtGui, QtCore

DIR = os.path.dirname(__file__)


class LineEdit(QtGui.QLineEdit):
    '''
    Inherits QLineEdit and creates it.
    '''
    def __init__(self, name, value, parent=None):
        '''
        Our line init.
        '''
        super(LineEdit, self).__init__(parent)
        self.setObjectName(name)
        self.setText(value)


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
        self.setMinimum(0.0)
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
        self.setMinimum(0.0)
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

        self.setWindowTitle("OScanUI")
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
        self.camGrp_layout = GroupBox("Camera Settings")
        self.outGrp_layout = GroupBox("Output Settings")

        self.cam_gridLayout = QtGui.QGridLayout()
        self.cam_gridLayout.setContentsMargins(10, 5, 10, 5)

        self.output_gridLayout = QtGui.QGridLayout()
        self.output_gridLayout.setContentsMargins(10, 5, 10, 5)

        self.create_camLayout()
        self.create_outLayout()

        #Camera settings layout.
        self.cam_gridLayout.addWidget(self.width_Lbl,     0, 0)
        self.cam_gridLayout.addWidget(self.width_spnBox,  0, 1)
        self.cam_gridLayout.addWidget(self.ppw_spnBox,    1, 1)
        self.cam_gridLayout.addWidget(self.width_cmbBox,  1, 2)
        self.cam_gridLayout.addWidget(self.height_Lbl,    2, 0)
        self.cam_gridLayout.addWidget(self.height_spnBox, 2, 1)
        self.cam_gridLayout.addWidget(self.pph_spnBox,    3, 1)
        self.cam_gridLayout.addWidget(self.height_cmbBox, 3, 2)
        self.cam_gridLayout.addWidget(self.aper_Lbl,      4, 0)
        self.cam_gridLayout.addWidget(self.hAper,         4, 1)
        self.cam_gridLayout.addWidget(self.vAper,         4, 2)

        #Output settings layout.
        self.output_gridLayout.addWidget(self.outRes_Lbl,      0, 0)
        self.output_gridLayout.addWidget(self.outWidth_lEdit,  0, 1)
        self.output_gridLayout.addWidget(self.outHeight_lEdit, 0, 2)
        self.output_gridLayout.addWidget(self.outAper_Lbl,     1, 0)
        self.output_gridLayout.addWidget(self.outAperH_lEdit,  1, 1)
        self.output_gridLayout.addWidget(self.outAperV_lEdit,  1, 2)

        #Set group layouts.
        self.camGrp_layout.setLayout(self.cam_gridLayout)
        self.outGrp_layout.setLayout(self.output_gridLayout)

        #Final add to central.
        self.central_boxLayout.addWidget(self.camGrp_layout)
        self.central_boxLayout.addWidget(self.outGrp_layout)

    def create_outLayout(self):
        '''
        Builds the output layout.
        '''
        #Output values.
        self.outRes_Lbl = Label("Resolution:")

        #Res
        self.outRes_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                      QtGui.QSizePolicy.Minimum)
        self.outWidth_lEdit = LineEdit("outWidth_lEdit", "2254")
        self.outWidth_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
        self.outWidth_lEdit.setReadOnly(True)

        self.outHeight_lEdit = LineEdit("outHeight_lEdit", "1188")
        self.outHeight_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                           QtGui.QSizePolicy.Minimum)
        self.outHeight_lEdit.setReadOnly(True)

        #Output values.
        self.outAper_Lbl = Label("Aperture H/V: ")
        self.outAper_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                       QtGui.QSizePolicy.Minimum)
        self.outAperH_lEdit = LineEdit("outAper_lEdit", "1.0399705")
        self.outAperH_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
        self.outAperH_lEdit.setReadOnly(True)

        self.outAperV_lEdit = LineEdit("outAper_lEdit", ".5481298")
        self.outAperV_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
        self.outAperV_lEdit.setReadOnly(True)

    def create_camLayout(self):
        '''
        Builds the camera settings layout.
        '''
        #Width items
        self.width_Lbl = Label("Width:")
        self.width_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                     QtGui.QSizePolicy.Minimum)
        self.width_spnBox = SpinBox("width_spnBox", 1920)
        self.width_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Minimum)

        #Width Percent/pixel comboBox.
        self.width_cmbBox = ComboBox("width_cmbBox")
        self.width_cmbBox.addItem("Percent")
        self.width_cmbBox.addItem("Pixels")
        self.width_cmbBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Minimum)
        self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 0.0)
        self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)

        #Height items
        self.height_Lbl = Label("Height:")
        self.height_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                      QtGui.QSizePolicy.Minimum)
        self.height_spnBox = SpinBox("height_spnBox", 1080)
        self.height_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Minimum)

        #Height Percent/pixel layout.
        self.height_cmbBox = ComboBox("height_cmbBox")
        self.height_cmbBox.addItem("Percent")
        self.height_cmbBox.addItem("Pixels")
        self.height_cmbBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Minimum)
        self.pph_spnBox = DoubleSpinBox("pph_spnBox", 0.0)
        self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)

        #Camera aperture.
        self.aper_Lbl = Label("Aperture H/V: ")
        self.aper_Lbl.setSizePolicy(QtGui.QSizePolicy.Maximum,
                                    QtGui.QSizePolicy.Minimum)
        self.hAper = DoubleSpinBox("hAper_spnBox", 0.9449244)
        self.hAper.setDecimals(5)
        self.hAper.setValue(0.9449244)
        self.hAper.setSingleStep(.1)
        self.vAper = DoubleSpinBox("vAper_spnBox", 0.4982999)
        self.vAper.setDecimals(5)
        self.vAper.setValue(0.4982999)
        self.vAper.setSingleStep(.1)

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
            self.pph_spnBox = SpinBox("pph_spnBox", 0.0)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)

        elif index == 0:
            self.pph_spnBox = DoubleSpinBox("pph_spnBox", 0.0)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)

        self.cam_gridLayout.addWidget(self.pph_spnBox, 3, 1)

    def replaceWSpinBox(self, index):
        '''
        Switches QSpinBox with QDoubleSpinBox.
        @param index - Index value of current spin box.
        '''
        self.ppw_spnBox.deleteLater()

        if index == 1:
            self.ppw_spnBox = SpinBox("ppw_spnBox", 0.0)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)

        elif index == 0:
            self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 0.0)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)

        self.cam_gridLayout.addWidget(self.ppw_spnBox, 1, 1)
