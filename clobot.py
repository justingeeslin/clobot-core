from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *

class CLOBot():

    @staticmethod
    def testSimulate():
        mdm = MarvelousDesignerModule()
        mdm.SimulationOn(1)
        mdm.LoadZmdrFileWithZblc("C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Polo.Set-In.zmdr", ["C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Collar.ButtonDown.zblc", "C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Body_Set-In.Regular.zblc"])
        mdm.ExportRenderingImage("I:\exportRenderImage.png")