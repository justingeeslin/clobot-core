import os
from itertools import product
import pathlib
from pathlib import Path
import sys

class CLOModularBlocks:
    
    blockFilepath = r"C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos"
    blockConfigFilePath = ""
    exportFilepath = r"C:\Users\Public\Documents\CLO\clobot"

    # The path and file name of the generated python script
    scriptFilePath = r"C:\Users\Public\Documents\CLO\clobot\testcase.py"

    garmentCreationScriptToOutput = """
        mdm = MarvelousDesignerModule()
        ## Enable drapping
        mdm.SimulationOn(1)
            """

    ## A simulation script that can be run inside of CLO - Creates Projects and images from garments
    projectCreationScriptToOutput = """"""

    def __init__(self):
        self.data = []

    @staticmethod
    def discoverBlockInformation(blockFilePath, exportFilePath):
        CLOModularBlocks.blockFilepath = blockFilePath
        CLOModularBlocks.exportFilepath = exportFilePath
        ## Get block information from the config file, such as how many blocks are in each category.
        import configparser
        config = configparser.ConfigParser()

        ## Discover the config file
        files = os.listdir(CLOModularBlocks.blockFilepath)
        sortedFiles = sorted(files)
        for file in sortedFiles:
            # Show progress..
            print('.')
            filePath = os.path.join(CLOModularBlocks.blockFilepath, file)
            # If it is a file
            if os.path.isfile(filePath):
                ## Is it a config file (.conf)
                if ".conf" in filePath:
                    CLOModularBlocks.blockConfigFilePath = filePath
                    config.read(CLOModularBlocks.blockConfigFilePath)

        ## The garment subtypes (Double & Single)
        try:
            garmentSubTypes = config['Activate_Configurator_Info']['None\Activate_List'].split(', ')
        except KeyError:
            print('Could not find block information within this folder. Is there a configuration file (.conf) in this folder?')
            sys.exit(-1)

        for garmentSubType in garmentSubTypes:
            ## Categories within the subType, Body Collar sleeves
            blockCategories = []

            ## Lists of all blocks to make simulations of
            listOfBlockListsToSimulate = []

            for key in config['Block_List_For_Modular']:
                # if "jacket.double" is in "none\jacket.double\body_back\activate_list"
                if garmentSubType.lower() in key:
                    blocks = config['Block_List_For_Modular'][key]
                    blocksList = blocks.split(", ")
                    listOfBlockListsToSimulate.append(blocksList)

            listOfBlockListsToSimulate
            blockCombos = list(product(*listOfBlockListsToSimulate))
            x = 3
            for blockCombo in blockCombos:

                renderImageFilename = ""
                renderImageFilename = renderImageFilename.replace(CLOModularBlocks.blockFilepath, '')
                renderImageFilename = renderImageFilename + '__' + '--'.join(blockCombo)
                # Remove slashes
                renderImageFilename = renderImageFilename.replace("\\", '')
                renderImageFilename = garmentSubType + '__' + renderImageFilename
                # Remove the file extensions from the individual block names
                renderImageFilename = renderImageFilename.replace(".zblc", '')
                # Remove dots since these are not allowed in folder names
                renderImageFilename = renderImageFilename.replace(".", '_')


                ## Build the simulation commands
                # print('Adding to scriptOutput')
                # print(blockCombo)

                ## Prepend the block path to the blocks
                blockComboAndPath = []
                for block in blockCombo:
                    blockComboAndPath.append(CLOModularBlocks.blockFilepath + "\\" + block)

                CLOModularBlocks.garmentCreationScriptToOutput += """
        # Load the garments
        mdm.LoadZmdrFileWithZblc(r\"""" + "" + CLOModularBlocks.blockFilepath + "\\" + garmentSubType + """.zmdr", [r\"""" + '", r"'.join(
            blockComboAndPath) + """\"])
                    """

                CLOModularBlocks.garmentCreationScriptToOutput += """
        # Create the Garment file
        mdm.ExportZPac(r'""" + CLOModularBlocks.exportFilepath + "\\" + renderImageFilename + """.zpac')
                           """

                CLOModularBlocks.projectCreationScriptToOutput += """
        #next multi process
        object.set_garment_file_path(r'""" + CLOModularBlocks.exportFilepath + "\\" + renderImageFilename + """.zpac')
        object.sync_file_lists("animation")
                        """

    @staticmethod
    def writePythonScript():
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
""" + CLOModularBlocks.garmentCreationScriptToOutput + """

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
        object.set_avatar_file_path(r"C:\\Users\\Public\\Documents\\CLO\\Assets\\Avatar\\Avatar\\Female_V2\\Avatar (Modular)\\Modular_FV2_Feifei.avt")
        object.set_avatar_file_path(r"C:\\Users\\Public\\Documents\\CLO\\Assets\\Avatar\\Avatar\\Female_V1\\FV1_Emma.avt")
        object.set_avatar_file_path(r"C:\\Users\\Public\\Documents\\CLO\\Assets\\Avatar\\Avatar\\Female_V2\\FV2_Feifei.avt")

""" + CLOModularBlocks.projectCreationScriptToOutput + """

        object.set_save_folder_path(r'""" + CLOModularBlocks.exportFilepath + """', "obj")

        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(True)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()
    """

        scriptToExport = imports + classScript

        # pathlib.Path(CLOModularBlocks.scriptFilePath).mkdir(parents=True, exist_ok=True)

        with open(CLOModularBlocks.scriptFilePath, "w") as f:
            f.write(scriptToExport)
            print("CLO Python Script created successfully!")
            print("From the CLO Python Script prompt, copy and paste the following, one line at a time:")
            # Add the CLOBot to the path
            print("sys.path.append(r\"" + os.path.dirname(CLOModularBlocks.scriptFilePath) + "\")")
            # Import CLOBot
            filename = Path(CLOModularBlocks.scriptFilePath).stem
            print("from " + filename + " import CLOBot")
            # Run the script
            print("CLOBot.go(mdsa)")

        f.close()