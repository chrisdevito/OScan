import os
import sys

DIR = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, DIR)

import OScan

try:
    reload(OScan.Calculator)
except:
    pass

from OScan import ui
reload(ui)

from PySide import QtGui

if __name__ == '__main__':

    #Shell test.
    qtapp = QtGui.QApplication(sys.argv)
    app = ui.UI()
    app.show()
    sys.exit(qtapp.exec_())
