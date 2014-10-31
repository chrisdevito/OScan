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

    def create_layout(self):
        '''
        Creating a layout.
        '''
        #Main grid layout.
        self.main_gridLayout = QtGui.QGridLayout()

        #Build border.
        self.oScan_Border = QtGui.QWidget()
        self.oScan_Border.setFixedWidth(self.oWidth)
        self.oScan_Border.setFixedHeight(self.oHeight)
        self.oScan_Border.setLayout(self.main_gridLayout)

        #Resolution label.
        self.res_Lbl = QtGui.QLabel()
        self.res_Lbl.setFixedWidth(self.width)
        self.res_Lbl.setFixedHeight(self.height)

        #Set image.
        self.pixmap = QtGui.QPixmap(self.imgPath)
        self.pixmap = self.pixmap.scaled(
            QtCore.QSize(self.width, self.height),
            QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        self.res_Lbl.setPixmap(self.pixmap)
        self.res_Lbl.setScaledContents(True)

        #Set layout and add widget.
        self.main_gridLayout.addWidget(self.res_Lbl, 0, 0)
        self.setLayout(self.main_gridLayout)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = OScanViewer(width=720, height=480)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
