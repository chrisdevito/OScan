import os
import sys
from PySide import QtGui, QtCore
DIR = os.path.dirname(__file__)


class OScanViewer(QtGui.QDialog):
    '''
    Creates the overscan viewer.
    '''
    def __init__(self, parent=None, width=720, height=480):

        super(OScanViewer, self).__init__(parent)

        self.oScanX = 1.2
        self.oScanY = 1.2

        self.width = width
        self.height = height

        self.oWidth = int(self.width * self.oScanX)
        self.oHeight = int(self.height * self.oScanY)

        self.centerX = int((self.oWidth - self.width)/2.0)
        self.centerY = int((self.oHeight - self.height)/2.0)

        self.imgPath = os.path.join(DIR, "images/ponyo.jpeg")

        #Resize.
        self.setGeometry(0, 0, self.oWidth, self.oHeight)
        self.setWindowTitle('OScan Viewer')

        #Init ui.
        self.initUI()

        #Create layout.
        self.create_layout()

        #Delete on close.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        #Show.
        self.show()

    def initUI(self):
        '''
        Initilizes the ui.
        '''
        #Center the window.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #central layout.
        self.central_boxLayout = QtGui.QVBoxLayout()
        # self.central_boxLayout.setSpacing(10)
        # self.central_boxLayout.setContentsMargins(10, 10, 10, 10)
        self.setLayout(self.central_boxLayout)

    def create_layout(self):
        '''
        Creating a layout.
        '''
        #Our main layout
        self.oScan_Border = QtGui.QWidget()
        self.oScan_Border.setFixedWidth(self.oWidth)
        self.oScan_Border.setFixedHeight(self.oHeight)

        #Resolution center.
        self.res_Lbl = QtGui.QLabel()
        self.res_Lbl.setSizePolicy(
            QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        #Image.
        self.pixmap = QtGui.QPixmap(self.imgPath)
        self.pixmap = self.pixmap.scaled(
            QtCore.QSize(self.width, self.height),
            QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.res_Lbl.setPixmap(self.pixmap)
        self.res_Lbl.setScaledContents(True)

        #Stacked widget.
        self.main_Stack = QtGui.QStackedWidget()
        self.main_Stack.setFixedSize(self.oWidth, self.oHeight)
        self.main_Stack.addWidget(self.res_Lbl)
        self.central_boxLayout.addWidget(self.main_Stack)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = OScanViewer(width=720, height=480)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
