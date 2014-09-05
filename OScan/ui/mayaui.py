from PySide import QtGui
from .ui import UI


def get_maya_window():
    '''Gets maya's main window.'''

    import shiboken
    import maya.OpenMayaUI as mui

    ptr = long(mui.MQtUtil.mainWindow())
    return shiboken.wrapInstance(ptr, QtGui.QWidget)


def create():
    '''
    Creates the UI.
    '''
    maya_window = get_maya_window()
    return UI(parent=maya_window)
