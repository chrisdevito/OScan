import sys

DIR = "/X/tools/maya/user_python/cdevito/OScan"
sys.path.insert(0, DIR)

import OScan

try:
    reload(OScan.calculator)
except:
    pass

from OScan import ui
reload(ui)

try:
    reload(ui.mayaui)
except:
    pass

if __name__ == '__main__':

    app = ui.create()
    app.show()
