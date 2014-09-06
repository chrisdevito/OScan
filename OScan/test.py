import os
import sys

#Danica is cool.
DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, DIR)

from OScan import ui
reload(ui)
from PySide import QtGui


if __name__ == '__main__':
    qtapp = QtGui.QApplication(sys.argv)
    app = ui.UI()
    app.show()
    sys.exit(qtapp.exec_())
