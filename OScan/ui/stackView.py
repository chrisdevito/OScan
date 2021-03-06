import os
import sys
from PySide import QtGui, QtCore
DIR = os.path.dirname(__file__)


class OScanViewer(QtGui.QDialog):
    '''
    Creates the overscan viewer.
    '''
    def __init__(
            self, parent=None, width=720, height=480, oScanX=1.1, oScanY=1.1):

        super(OScanViewer, self).__init__(parent)

        self.aspectRatio = float(width)/float(height)

        windowWidth = 475

        sWidth = windowWidth
        sHeight = round(windowWidth/self.aspectRatio)

        self.oScanX = oScanX
        self.oScanY = oScanY

        self.width = sWidth
        self.height = sHeight

        self.oWidth = round(self.width * self.oScanX)
        self.oHeight = round(self.height * self.oScanY)

        self.imgPath = os.path.join(DIR, "images/ponyo.jpeg")

        #Resize.
        self.setWindowTitle('OScan Viewer')
        self.setFixedSize(self.oWidth, self.oHeight)

        self.setStyleSheet("QWidget{"
                           "background-color: rgb(0, 0, 0);"
                           "color: rgb(200, 200, 200);}")

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
        self.main_gridLayout.setContentsMargins(0, 0, 0, 0)

        #Build border.
        self.oScan_Border = QtGui.QWidget()
        self.oScan_Border.setAutoFillBackground(True)
        self.oScan_Border.setFixedWidth(self.oWidth)
        self.oScan_Border.setFixedHeight(self.oHeight)
        palette = self.oScan_Border.palette()
        palette.setColor(self.oScan_Border.backgroundRole(), QtCore.Qt.black)
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

        print(self.size())
        print(self.oScan_Border.size())
        print(self.res_Lbl.size())


def main():
    app = QtGui.QApplication(sys.argv)
    ex = OScanViewer(width=720, height=480, oScanX=1.1, oScanY=1.1)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
