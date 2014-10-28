#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore


class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.width = 720
        self.height = 480

        self.initUI()

    def initUI(self):

        #Center the window.
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        #Resize.
        self.resize(self.width, self.height)
        self.setWindowTitle('OScan Viewer')
        self.show()

    def paintEvent(self, e):

        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()

    def drawBrushes(self, qp):

        brush = QtGui.QBrush(QtCore.Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.setPen(QtCore.Qt.SolidLine)
        qp.drawRect(0, 0, self.width, self.height)

        brush.setStyle(QtCore.Qt.SolidPattern)
        brush.setColor(QtGui.QColor(255, 255, 255, 255))
        qp.setBrush(brush)
        centerX = int(self.width/2.0)/2.0
        centerY = int(self.height/2.0)/2.0

        qp.drawRect(centerX, centerY, self.width/2, self.height/2)


def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
