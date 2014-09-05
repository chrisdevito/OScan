import sys
sys.path.insert(0, "/X/tools/python/users/python2.6/cdevito/OScan")
from OScan import ui
reload(ui)
from PySide import QtGui


if __name__ == '__main__':
    qtapp = QtGui.QApplication(sys.argv)
    app = ui.UI()
    app.show()
    sys.exit(qtapp.exec_())
