import shiboken
from .ui import UI
from PySide import QtGui
import maya.cmds as cmds
import maya.OpenMaya as OpenMaya
import maya.OpenMayaUI as OpenMayaUI


def get_maya_window():
    '''
    Gets maya's main window.
    '''
    ptr = long(OpenMayaUI.MQtUtil.mainWindow())
    return shiboken.wrapInstance(ptr, QtGui.QWidget)


def create():
    '''
    Creates the UI.
    '''
    return maya_UI()


class maya_UI(UI):
    '''
    Maya UI.
    '''
    def __init__(self, parent=get_maya_window()):
        '''
        Initializer.
        '''
        super(maya_UI, self).__init__(parent)
