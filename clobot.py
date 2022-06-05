from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
from ModularConfigurator import ModularConfigurator

class CLOBot():

    @staticmethod
    def testSimulate():
        mdm = MarvelousDesignerModule()
        ## Enable drapping
        mdm.SimulationOn(1)
        ## Load the modular configurator blocks
        mdm.LoadZmdrFileWithZblc("C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Polo.Set-In.zmdr", ["C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Collar.ButtonDown.zblc", "C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Body_Set-In.Regular.zblc"])
        ## High-quality render of the image
        mdm.ExportRenderingImage("I:\exportRenderImage.png")

    @staticmethod
    def simulateAllModularBlocks():
        ModularConfigurator.getBlocksFromFilesystem()
        ModularConfigurator.iterateThroughBlockFolders(ModularConfigurator.blocks)
        print("Number of simulations:")
        print(ModularConfigurator.countOfSimulations)
