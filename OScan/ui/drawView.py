import os
import sys
from PySide import QtGui, QtCore
DIR = os.path.dirname(__file__)


class OScanViewer(QtGui.QWidget):
    '''
    Creates the overscan viewer.
    '''
    def __init__(self, width=720, height=480):
        super(OScanViewer, self).__init__()

        self.oScanX = 1.2
        self.oScanY = 1.2

        self.width = width
        self.height = height

        self.oWidth = int(self.width * self.oScanX)
        self.oHeight = int(self.height * self.oScanY)

        self.centerX = int((self.oWidth - self.width)/2.0)
        self.centerY = int((self.oHeight - self.height)/2.0)

        self.imgPath = os.path.join(DIR, "images/ponyo.jpeg")

        self.initUI()

    def initUI(self):
        '''
        Initilizes the ui.
        '''
        #Center the window.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Resize.
        self.resize(self.oWidth, self.oHeight)
        self.setWindowTitle('OScan Viewer')
        self.show()

    def paintEvent(self, event):
        '''
        Paint event to draw overscan.
        @param event - QPainter drawing event.
        Returns None.
        '''
        qPaint = QtGui.QPainter()
        qPaint.begin(self)
        self.drawBrushes(qPaint)
        qPaint.end()

    def drawBrushes(self, qPaint):
        '''
        Draws the rectangles.
        @param qPaint - QPainter draw.
        Returns None.
        '''
        oscan_Brush = QtGui.QBrush(QtCore.Qt.Dense6Pattern)
        oscan_Brush.setColor(QtGui.QColor(0, 0, 0, 255))
        qPaint.setBrush(oscan_Brush)
        qPaint.setPen(QtCore.Qt.SolidLine)
        qPaint.drawRect(
            0, 0,
            self.oWidth, self.oHeight)

        res_Brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
        res_Brush.setColor(QtGui.QColor(255, 255, 255, 255))
        # res_Brush.setTextureImage(self.image)
        qPaint.setBrush(res_Brush)
        qPaint.drawRect(self.centerX, self.centerY, self.width, self.height)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = OScanViewer(width=720, height=480)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
