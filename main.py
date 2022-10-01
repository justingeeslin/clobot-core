import sys
from ModularConfigurator import ModularConfigurator

if __name__ == '__main__':

    ## Establish whether in debug mode
    isDebug = False
    gettrace = getattr(sys, 'gettrace', None)
    if gettrace():
        isDebug = True


    blockPath = "";
    ## Woman\\T-Shirts,Woman\\Trench Coats
    hasSufficentArguments = True;
    if len(sys.argv) > 1:
        blockPath = sys.argv[1]
    else:
        print("Please supply the path for the blocks. Ex: C:\\\\Users\Public\Documents\CLO\Assets\Blocks\\")
        hasSufficentArguments = False;

    outputPath = "";
    if len(sys.argv) > 2:
        outputPath = sys.argv[2]
    else:
        print("Please supply the output path i.e. where do you want to resutling Python script to go. . Ex: C:\\\\Users\Public\Documents\CLO\CLOBot\Scripts\\")
        hasSufficentArguments = False;

    if not hasSufficentArguments:
        exit(1)

    ModularConfigurator.blockFilepath = blockPath;
    ModularConfigurator.exportFilepath = outputPath;
    ## Build a list of simulations using blocks from the filesystem
    ModularConfigurator.getBlocksFromFilesystem(blockPath)

    imports = """
from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
           """
    classScript = """
class CLOBot():

    @staticmethod
    def go(object):
        CLOBot.createGarmentsFromBlocks()
        CLOBot.createProjectsAndImagesFromGarments(object)

    @staticmethod
    def createGarmentsFromBlocks():
""" + ModularConfigurator.garmentCreationScriptToOutput + """

    @staticmethod
    def createProjectsAndImagesFromGarments(object):
        # Garments to Images & Projects
        
        # clear console window
        object.clear_console() 
        #initialize object module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")
        
        #Set simulation property settings
        #Set Simulation property options(simulation quality) of integer type
        # qulity = 0 Complete
        # qulity = 1 Normal
        # qulity = 2 Custom
        object.set_simulation_quality(1)
        
        # Attempting to take the later frames of the simulation
        object.set_simulation_options(0, 0, 10000)
        
        # Load the avatar
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\CLO\\Assets\\Avatar\\Avatar\\Female_V2\\Avatar (Modular)\\Modular_FV2_Feifei.avt")

""" + ModularConfigurator.projectCreationScriptToOutput + """

        object.set_save_folder_path('""" + ModularConfigurator.exportFilepath + """', "obj")
        
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(True)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()
    """
    ## Write the script to a python file
    if isDebug:
        f = open("clobot3.py", "w")
    else:
        f = open("C:\\Users\Public\Documents\CLO\Assets\clobot3.py", "w")
    f.write(imports + classScript)
    f.close()

    # CLOBot.simulateAllModularBlocks()