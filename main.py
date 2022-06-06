from ModularConfigurator import ModularConfigurator

if __name__ == '__main__':
    ## Build a list of simulations using blocks from the filesystem
    ModularConfigurator.getBlocksFromFilesystem()

    imports = """
from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
           """
    classBeginning = """
class CLOBotInstructions():
    @staticmethod
    def run():
    """
    ## Write the script to a python file
    f = open("instructions.py", "w")
    f.write(imports + classBeginning + ModularConfigurator.scriptToOutput)
    f.close()

    # CLOBot.simulateAllModularBlocks()