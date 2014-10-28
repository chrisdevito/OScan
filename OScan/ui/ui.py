import os
from decimal import Decimal
from PySide import QtGui, QtCore
from ..calculator import calculateOverscan
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


class CheckBox(QtGui.QCheckBox):
    '''
    Inherits QCheckBox and creates it.
    '''
    def __init__(self, name, parent=None):
        '''
        Our checkbox init.
        '''
        super(CheckBox, self).__init__(parent)
        self.setObjectName(name)
        self.setAutoExclusive(False)


class SpinBox(QtGui.QSpinBox):
    '''
    Inherits QSpinBox and creates it.
    '''
    def __init__(self, name, value, parent=None):
        '''
        Our spinbox init.
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
        Our double spinbox init.
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
        Our combo init.
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
        Our group init.
        '''
        super(GroupBox, self).__init__(name, parent)
        self.setObjectName("{0}_grpBox".format(name))


class UI(QtGui.QDialog):
    '''
    QDialog for OScan.
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

        #Store values to switch easy.
        self.initPixelW = 0.0
        self.initPixelH = 0.0
        self.initPerW = 10.0
        self.initPerH = 10.0

        #Init values for lock.
        self.lock = False
        self.resRatio = None
        self.oScanRatio = None

        #Center the window.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Our main layout
        self.central_boxLayout = QtGui.QVBoxLayout()
        self.central_boxLayout.setSpacing(10)
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
        self.camGrp_layout.setFlat(True)
        self.outGrp_layout.setFlat(True)

        self.cam_gridLayout = QtGui.QGridLayout()
        self.cam_gridLayout.setContentsMargins(10, 5, 10, 5)

        self.output_gridLayout = QtGui.QGridLayout()
        self.output_gridLayout.setContentsMargins(10, 5, 10, 5)

        self.chk_gridLayout = QtGui.QGridLayout()
        self.chk_gridLayout.setContentsMargins(10, 5, 10, 5)

        self.create_camLayout()
        self.create_outLayout()

        #Camera settings layout.
        self.cam_gridLayout.addWidget(self.widthHeight_Lbl, 0, 0)
        self.cam_gridLayout.addWidget(self.width_spnBox,    0, 1)
        self.cam_gridLayout.addWidget(self.height_spnBox,   0, 2)
        self.cam_gridLayout.addWidget(self.widthOScan_lbl,  1, 0)
        self.cam_gridLayout.addWidget(self.ppw_spnBox,      1, 1)
        self.cam_gridLayout.addWidget(self.width_cmbBox,    1, 2)
        self.cam_gridLayout.addWidget(self.heightOScan_lbl, 2, 0)
        self.cam_gridLayout.addWidget(self.pph_spnBox,      2, 1)
        self.cam_gridLayout.addWidget(self.height_cmbBox,   2, 2)
        self.cam_gridLayout.addWidget(self.aper_Lbl,        3, 0)
        self.cam_gridLayout.addWidget(self.hAper,           3, 1)
        self.cam_gridLayout.addWidget(self.vAper,           3, 2)

        #Output settings layout.
        self.output_gridLayout.addWidget(self.outRes_Lbl,      0, 0)
        self.output_gridLayout.addWidget(self.outWidth_lEdit,  0, 1)
        self.output_gridLayout.addWidget(self.outHeight_lEdit, 0, 2)
        self.output_gridLayout.addWidget(self.outAper_Lbl,     1, 0)
        self.output_gridLayout.addWidget(self.outAperH_lEdit,  1, 1)
        self.output_gridLayout.addWidget(self.outAperV_lEdit,  1, 2)

        #Add lock width/height.
        self.chk_gridLayout.addWidget(self.lockWH_lbl,      0, 0)
        self.chk_gridLayout.addWidget(self.lockWH_chkBox,   0, 1)
        self.chk_gridLayout.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)

        #Set group layouts.
        self.camGrp_layout.setLayout(self.cam_gridLayout)
        self.outGrp_layout.setLayout(self.output_gridLayout)

        #Final add to central.
        self.central_boxLayout.addWidget(self.camGrp_layout)
        self.central_boxLayout.addWidget(self.outGrp_layout)
        self.central_boxLayout.addLayout(self.chk_gridLayout)

    def create_outLayout(self):
        '''
        Builds the output layout.
        '''
        #Output values.
        self.outRes_Lbl = Label("Resolution W/H:")
        self.outRes_Lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.outRes_Lbl.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)
        #Res
        self.outWidth_lEdit = LineEdit("outWidth_lEdit", "2112")
        self.outWidth_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
        self.outWidth_lEdit.setReadOnly(True)

        self.outHeight_lEdit = LineEdit("outHeight_lEdit", "1188")
        self.outHeight_lEdit.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                           QtGui.QSizePolicy.Minimum)
        self.outHeight_lEdit.setReadOnly(True)

        #Output values.
        self.outAper_Lbl = Label("Aperture H/V:")
        self.outAper_Lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.outAper_Lbl.setSizePolicy(QtGui.QSizePolicy.Minimum,
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
        self.widthHeight_Lbl = Label("Resolution W/H:")
        self.widthHeight_Lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.widthHeight_Lbl.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                           QtGui.QSizePolicy.Minimum)
        self.width_spnBox = SpinBox("width_spnBox", 1920)
        self.width_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Minimum)
        self.width_spnBox.setMinimum(1.0)

        #Width Percent/pixel comboBox.
        self.widthOScan_lbl = Label("Overscan W:")
        self.widthOScan_lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.widthOScan_lbl.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
        self.width_cmbBox = ComboBox("width_cmbBox")
        self.width_cmbBox.addItem("Percent")
        self.width_cmbBox.addItem("Pixels")
        self.width_cmbBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Minimum)
        self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 10.0)
        self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)

        #Height items
        self.height_spnBox = SpinBox("height_spnBox", 1080)
        self.height_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Minimum)
        self.height_spnBox.setMinimum(1.0)

        #Height Percent/pixel layout.
        self.heightOScan_lbl = Label("Overscan H:")
        self.heightOScan_lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.height_cmbBox = ComboBox("height_cmbBox")
        self.height_cmbBox.addItem("Percent")
        self.height_cmbBox.addItem("Pixels")
        self.height_cmbBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                         QtGui.QSizePolicy.Minimum)
        self.pph_spnBox = DoubleSpinBox("pph_spnBox", 10.0)
        self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)

        #Camera aperture.
        self.aper_Lbl = Label("Aperture H/V:")
        self.aper_Lbl.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.hAper = DoubleSpinBox("hAper_spnBox", 0.9449244)
        self.hAper.setDecimals(7)
        self.hAper.setValue(0.9449244)
        self.hAper.setSingleStep(.01)
        self.vAper = DoubleSpinBox("vAper_spnBox", 0.4982999)
        self.vAper.setDecimals(7)
        self.vAper.setValue(0.4982999)
        self.vAper.setSingleStep(.01)
        self.vAper.setMinimum(.001)
        self.hAper.setMinimum(.001)

        #Lock wh.
        self.lockWH_lbl = Label("Constrain Proportions: ")
        self.lockWH_lbl.setAlignment(
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lockWH_lbl.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                      QtGui.QSizePolicy.Minimum)
        self.lockWH_chkBox = CheckBox("lockWH")
        self.lockWH_chkBox.setChecked(False)

    def create_connections(self):
        '''
        Creates connections between controls.
        '''
        self.width_cmbBox.currentIndexChanged.connect(self.replaceWSpinBox)
        self.height_cmbBox.currentIndexChanged.connect(self.replaceHSpinBox)
        self.width_cmbBox.currentIndexChanged.connect(self.calculate)
        self.height_cmbBox.currentIndexChanged.connect(self.calculate)
        self.width_spnBox.valueChanged.connect(self.widthLock)
        self.height_spnBox.valueChanged.connect(self.heightLock)
        self.ppw_spnBox.valueChanged.connect(self.oScanXLock)
        self.pph_spnBox.valueChanged.connect(self.oScanYLock)
        self.hAper.valueChanged.connect(self.calculate)
        self.vAper.valueChanged.connect(self.calculate)

        self.lockWH_chkBox.stateChanged.connect(self.setRatios)

    def oScanXLock(self):
        '''
        Deals with overscan X Lock.
        '''
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            xVal = float(self.ppw_spnBox.value())
            yVal = float(self.pph_spnBox.value())
            checkY = round(xVal * (1.0/self.oScanRatio))

            if self.pph_spnBox.hasFocus():
                self.calculate()

            elif not yVal == checkY:
                if self.width_cmbBox.currentIndex() == 0:
                    self.pph_spnBox.setValue(checkY)
                else:
                    self.pph_spnBox.setValue(int(checkY))
                return

            else:
                self.calculate()

        else:
            self.calculate()

    def oScanYLock(self):
        '''
        Deals with overscan Y Lock.
        '''
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            xVal = float(self.ppw_spnBox.value())
            yVal = float(self.pph_spnBox.value())
            checkX = round(yVal * self.oScanRatio)

            if self.ppw_spnBox.hasFocus():
                self.calculate()

            elif not xVal == checkX:
                if self.width_cmbBox.currentIndex() == 0:
                    self.ppw_spnBox.setValue(checkX)
                else:
                    self.ppw_spnBox.setValue(int(checkX))

                return

            else:
                self.calculate()

        else:
            self.calculate()

    def widthLock(self):
        '''
        Checks for width lock.
        '''
        isChecked = self.lockWH_chkBox.isChecked()

        if isChecked:
            hVal = float(self.width_spnBox.value())
            vVal = float(self.height_spnBox.value())
            checkV = round(hVal * (1.0/self.resRatio))

            if self.height_spnBox.hasFocus():
                self.calculate()

            if not vVal == checkV:
                self.height_spnBox.setValue(int(checkV))
                return

            else:
                self.calculate()
        else:
            self.calculate()

    def heightLock(self):
        '''
        Checks for height lock.
        '''
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            hVal = float(self.width_spnBox.value())
            vVal = float(self.height_spnBox.value())
            checkH = round(vVal * self.resRatio)

            if self.width_spnBox.hasFocus():
                self.calculate()

            elif not hVal == checkH:
                self.width_spnBox.setValue(int(checkH))
                return

            else:
                self.calculate()

        else:
            self.calculate()

    def setRatios(self):
        '''
        Checks for locked dimensions and builds a ratio for them.
        '''
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            self.lock = True
            self.resRatio = (float(self.width_spnBox.value()) /
                             float(self.height_spnBox.value()))
            try:
                self.oScanRatio = (float(self.ppw_spnBox.value()) /
                                   float(self.pph_spnBox.value()))
            except:
                self.oScanRatio = 1.0
        else:
            self.lock = False
            self.resRatio = None
            self.oScanRatio = None

    def replaceHSpinBox(self, index):
        '''
        Switches QSpinBox with QDoubleSpinBox.
        @param index - Index value of current spin box.
        '''
        if index == 1:
            self.initPerH = self.pph_spnBox.value()
            self.pph_spnBox.deleteLater()
            self.pph_spnBox = SpinBox("pph_spnBox", 0.0)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
            self.pph_spnBox.setValue(self.initPixelH)

        elif index == 0:
            self.initPixelH = self.pph_spnBox.value()
            self.pph_spnBox.deleteLater()
            self.pph_spnBox = DoubleSpinBox("pph_spnBox", 0.0)
            self.pph_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
            self.pph_spnBox.setValue(self.initPerH)

        #Add back to the layout.
        self.cam_gridLayout.addWidget(self.pph_spnBox, 2, 1)
        self.pph_spnBox.setFocus()
        self.pph_spnBox.valueChanged.connect(self.oScanYLock)

        #Keep locked.
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            if self.width_cmbBox.hasFocus():
                self.setRatios()
            else:
                self.width_cmbBox.setCurrentIndex(index)

    def replaceWSpinBox(self, index):
        '''
        Switches QSpinBox with QDoubleSpinBox.
        @param index - Index value of current spin box.
        '''
        if index == 1:
            self.initPerW = self.ppw_spnBox.value()
            self.ppw_spnBox.deleteLater()
            self.ppw_spnBox = SpinBox("ppw_spnBox", 0.0)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
            self.ppw_spnBox.setValue(self.initPixelW)

        elif index == 0:
            self.initPixelW = self.ppw_spnBox.value()
            self.ppw_spnBox.deleteLater()
            self.ppw_spnBox = DoubleSpinBox("ppw_spnBox", 0.0)
            self.ppw_spnBox.setSizePolicy(QtGui.QSizePolicy.Minimum,
                                          QtGui.QSizePolicy.Minimum)
            self.ppw_spnBox.setValue(self.initPerW)

        #Add back to the layout.
        self.cam_gridLayout.addWidget(self.ppw_spnBox, 1, 1)
        self.ppw_spnBox.setFocus()
        self.ppw_spnBox.valueChanged.connect(self.oScanXLock)

        #Keep locked.
        isChecked = self.lockWH_chkBox.isChecked()
        if isChecked:
            if self.height_cmbBox.hasFocus():
                self.setRatios()
            else:
                self.height_cmbBox.setCurrentIndex(index)

    def calculate(self):
        '''
        Runs the calculator and updates the output values.
        '''
        xRes = self.width_spnBox.value()
        yRes = self.height_spnBox.value()
        xAper = self.hAper.value()
        yAper = self.vAper.value()

        if self.width_cmbBox.currentIndex() == 0:
            oScanX = (self.ppw_spnBox.value() / 100) + 1
        else:
            oScanX = float(Decimal(str(xRes +
                           (self.ppw_spnBox.value()*2)))/Decimal(str(xRes)))

        if self.height_cmbBox.currentIndex() == 0:
            oScanY = (self.pph_spnBox.value() / 100) + 1
        else:
            oScanY = float(Decimal(str(yRes +
                           (self.pph_spnBox.value()*2)))/Decimal(str(yRes)))

        res, aper = calculateOverscan(oScanX=oScanX,
                                      oScanY=oScanY,
                                      xRes=xRes,
                                      yRes=yRes,
                                      xAper=xAper,
                                      yAper=yAper)

        self.outAperH_lEdit.setText(str(aper[0]))
        self.outAperV_lEdit.setText(str(aper[1]))
        self.outWidth_lEdit.setText(str(res[0]))
        self.outHeight_lEdit.setText(str(res[1]))
