# from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
# from PythonQt.MarvelousDesignerAPI import *
# import MarvelousDesigner
# from MarvelousDesigner import *
import time
from itertools import product

from Clo import Clo

class ModularConfigurator:

    ## A list of zblocks to add to the avatar
    zBlocksToSimulate = []

    activeGarment = ""

    currentZMDRFile = ""

    countOfSimulations = 0

    isHighQualityRender = True

    # Might Vary
    ## Might get the position of the modular configurator panel then move from there.
    blockFolderStartingPoint = [275, 192]
    ## Distance between block folders
    distanceBetweenBlocks = 75

    # In the case of Jackets, Double, Single, etc
    garmentSubTypeStartingPoint = [325, 388]

    garmentTypeFoldersToInclude = [0]

    ## A master list of all blocks
    blocks = {}

    ## Distance bewteen the actual garment peices (fronts, backs, sleeves, etc.)
    distanceBetweenGarmentVertical = 119

    ## Is the Modular Configurator at the top most level. Folders are positioned differently when it is.
    isAtTopLevel = True

    ## Are there active blocks on the configurator. Is CLO going to prompt when I switch from Double to Single
    areBlocksActive = False

    ## Don't snapshot until a full outfit has been made
    madeFullOutfit = False

    ## Wait for things, but keep up with how long you're waiting
    sleepCounter = 0

    ## Break from waiting for something if it takes too long, more than this number
    maxTimeToSleep = 10

    ## List of Folders, stack kept during traversal
    folders = []

    ## Windows
    blockFilepath = "C:\\\\Users\Public\Documents\CLO\Assets\Blocks\\"
    ## Mac
    # blockFilepath = "/Volumes/[C] WinDev2204Eval/Users/Public/Documents/CLO/Assets/Blocks/"
    # blockFilepath = "/Users/Skyward/Documents/clo/Assets/"

    # exportFilepath = "Y:\\\\"

    # Citrix
    # exportFilepath = "I:\\\\CLOBot Creations\\\\"

    # VM
    exportFilepath = "C:\\\\Users\Public\Documents\CLO\CLOBot Creations\\\\"

    # Mac
    # exportFilepath = "~/CLOBot Creations/"

    # exportFilepath = "V:\\\\"
    ## A simulation script that can be run inside of CLO - Creates Garments zpac files
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
    def log(msg):
        ## Replace later when you have a way of showing notifications to the user.
        print(msg)

    @staticmethod
    def iterateThroughGarmentSubtypeBlocks():
        # In the case of Jackets, Double, Single, etc
        garmentSubTypeStartingPoint = [325, 388]

        garmentTypeFoldersToInclude = [0]

        # Double, Single Jacket subtype
        for k in garmentTypeFoldersToInclude:
            ModularConfigurator.log("Move to a garment subtype...")
            # pyautogui.moveTo(
            #     garmentSubTypeStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * k,
            #     garmentSubTypeStartingPoint[1]
            # )
            # pyautogui.doubleClick()

            # Start to go back up -- out of subtype
            ## Double Click on the .. folder
            time.sleep(3)
            # pyautogui.moveTo(ModularConfigurator.blockFolderStartingPoint)
            # pyautogui.doubleClick()

    @staticmethod
    def makeBlockTree(garmentTypesAndBlockCategories):
        print(garmentTypesAndBlockCategories)

        ModularConfigurator.zBlocksToSimulate

        # for row in garmentTypesAndBlockCategories:
        #     garmentRowName = list(row.keys())[0]
        #     rowBlocks = row[garmentRowName]
        #     for block in rowBlocks:
        #
        #     x = 3

    ## Individual action for the recursive process
    @staticmethod
    def iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex, colIndex):
        garmentRow = garmentTypesAndBlockCategories[rowIndex]
        garmentRowName = list(garmentRow.keys())[0]

        try:
            blockName = garmentRow[garmentRowName][colIndex]
        except IndexError:
            # ModularConfigurator.log("No block at " + colIndex + " for " + garmentRowName);
            return
        blocks = garmentRow[garmentRowName]

        ModularConfigurator.log("Exploring " + garmentRowName + ", " + blockName)


        # Double click on Double, Single, etc.
        ModularConfigurator.log("Loading garment piece...")


        ## Make the block combinations
        listOfBlockLists = []
        for row in garmentTypesAndBlockCategories:
            garmentRowName = list(row.keys())[0]
            rowBlocks = row[garmentRowName]

            rowBlocksNamed = []
            for block in rowBlocks:
                ## Append "Collar" or the type of block it is to the front
                rowBlocksNamed.append(garmentRowName + "." + block)

            listOfBlockLists.append(rowBlocksNamed)


        ## A list of block sets to simulate
        listOfBlockSets = list(product(*listOfBlockLists))
        x=3
        for blockSet in listOfBlockSets:
            ModularConfigurator.log('Rendering..')
            ModularConfigurator.log(blockSet)

            ## File path


            ## Create a filename from the block set combined with the garment name
            renderImageFilename = ModularConfigurator.activeGarment + '_' + '-'.join(blockSet)

            ModularConfigurator.zBlocksToSimulate = []

            for block in blockSet:
                blockFilename = block + ".zblc"
                ModularConfigurator.zBlocksToSimulate.append(blockFilepath + blockFilename)

            ModularConfigurator.scriptToOutput += """
        # Load the garments
        mdm.LoadZmdrFileWithZblc(\"""" + ModularConfigurator.blockFilepath + ModularConfigurator.currentZMDRFile + """\", [\"""" + '", "'.join(ModularConfigurator.zBlocksToSimulate) + """\"])
            """
            x=3
            if ModularConfigurator.isHighQualityRender:
                ModularConfigurator.scriptToOutput += """
        # Call for the high quality render
        mdm.ExportRenderingImage('I:\\""" + renderImageFilename + """.png')
                """
            else:
                ModularConfigurator.scriptToOutput += """
        # 3dsnapshot
        mdm.ExportSnapshot3D('I:\\""" + renderImageFilename + """.png')
                   """


            ModularConfigurator.countOfSimulations = ModularConfigurator.countOfSimulations + 1

        # try:
        #     ModularConfigurator.zBlocksToSimulate[rowIndex] = blockFileName
        # except IndexError:
        #     ModularConfigurator.zBlocksToSimulate.append(blockFileName)
        #
        # if len(garmentTypesAndBlockCategories) <= rowIndex + 1:
        #     ModularConfigurator.madeFullOutfit = True

        # if ModularConfigurator.madeFullOutfit:
        #     ModularConfigurator.zBlocksToSimulate
        #     ModularConfigurator.log('Rendering..')
        #     ModularConfigurator.log(ModularConfigurator.zBlocksToSimulate)
        #
        #     ## Load the garments
        #     # mdm.LoadZmdrFileWithZblc(ModularConfigurator.currentZMDRFile, ModularConfigurator.zBlocksToSimulate)
        #     ## Call for the high quality render
        #     # mdm.ExportRenderingImage("I:\exportRenderImage.png")
        #     #Clo.snapshot3DWindow("" + garmentRowName + "-" + blockName + "-" + str(colIndex) + "-" + str(rowIndex) )
        # else:
        #     ModularConfigurator.log('Skipping snapshot for now, still making an entire outfit.')

        # i = 0
        # for rows in garmentTypesAndBlockCategories:
        #     ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex + 1, colIndex)
        #     i = i + 1
        #
        # # if rowIndex+1 < len(garmentTypesAndBlockCategories):
        # #     ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex+1, colIndex)
        # #
        # # if colIndex + 1 < len(garmentTypesAndBlockCategories[rowIndex][garmentRowName]):
        # #     ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex,
        # #                                                           colIndex+1)
        #
        # ModularConfigurator.madeFullOutfit = False

    @staticmethod
    def iterateThroughGarmentBlocks(garmentTypesAndBlockCategories):
        ModularConfigurator.log("Iterating through the garment blocks...")

        ## Don't render anything until a full outfit is made
        madeFullOutfit = False

        ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, 0, 0);

        ModularConfigurator.log("Complete for this modular type...")
    @staticmethod
    def sortGarmentsLikeClo(garment):
        garmentName = list(garment.keys())[0]
        listOfGarmentTypes = [
            'collar',
            'body_front',
            'body_back',
            'body',
            'sleeves',
            'cuffs'
        ]
        return listOfGarmentTypes.index(garmentName)

    ## Build simulations right from here
    @staticmethod
    def parseFolderConfig(configFilePath):
        import configparser
        config = configparser.ConfigParser()
        config.read(configFilePath)

        ## The garment subtypes (Double & Single)
        garmentSubTypes = config['Activate_Configurator_Info']['None\Activate_List'].split(', ')

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
            x=3
            for blockCombo in blockCombos:

                renderImageFilename = '-'.join(ModularConfigurator.folders)
                renderImageFilename = renderImageFilename.replace(ModularConfigurator.blockFilepath, '')
                renderImageFilename = renderImageFilename + '__' + '--'.join(blockCombo)
                # Remove slashes
                renderImageFilename = renderImageFilename.replace("\\", '')
                renderImageFilename = garmentSubType + '__' + renderImageFilename
                # Remove the file extensions from the individaul block names
                renderImageFilename = renderImageFilename.replace(".zblc", '')
                # Remove dots since these are not allowed in folder names
                renderImageFilename = renderImageFilename.replace(".", '_')

                ##
                blockPath = ModularConfigurator.folders
                # if len(blockPath) > 1:
                #     ## Remove the path from C: to the blocks
                # del blockPath[0]

                ## Build the simulation commands
                print('Adding to scriptOutput')
                print(blockCombo)

                ## Prepend the block path to the blocks
                blockComboAndPath = []
                for block in blockCombo:
                    blockComboAndPath.append(ModularConfigurator.blockFilepath + block)

                ModularConfigurator.garmentCreationScriptToOutput += """
        # Load the garments
        mdm.LoadZmdrFileWithZblc(\"""" + "" + ModularConfigurator.blockFilepath + '\\' + garmentSubType + """.zmdr", [\"""" + '", "'.join(
    blockComboAndPath) + """\"])"""

                ModularConfigurator.garmentCreationScriptToOutput += """
        # Create the Garment file
        mdm.ExportZPac('""" + ModularConfigurator.exportFilepath +  renderImageFilename + """.zpac')
                   """

                ModularConfigurator.projectCreationScriptToOutput += """
        #next multi process
        object.set_garment_file_path('""" + ModularConfigurator.exportFilepath + renderImageFilename + """.zpac')
        object.sync_file_lists("animation")
                """



    ## The individual folder process of working with the filesystem
    @staticmethod
    def exploreBlockFolder(folderPath):
        # Things to do for each folder
        directoriesInPath = folderPath.split('/')
        currentFolderName = directoriesInPath[-1]
        ModularConfigurator.folders
        ModularConfigurator.folders.append(currentFolderName + "\\")
        x=3
        # Special Folders to omit
        foldersToOmit = "Assets/Blocks/Folded Shirt"

        #
        listOfDirectories = {}

        # Iterate over the other files and folders
        import os
        your_path = folderPath
        files = os.listdir(your_path)
        sortedFiles = sorted(files)
        for file in sortedFiles:
            subfolders = {}
            filePath = os.path.join(your_path, file)
            # If it is a directory
            if os.path.isfile(filePath):
                ## Is it a config file (.conf)
                if ".conf" in filePath:
                    ## Get block information fron the config file, such as how many blocks are in each category.
                    ModularConfigurator.parseFolderConfig(filePath)

            else:
                folderPath = filePath

                directories = folderPath.split("/")
                ## Last folder in the path is the current folder
                nameOfFolder = directories[-1]

                if (foldersToOmit in folderPath):
                    # Do nothing
                    x = 3
                else:
                    # If this is not an omitted folder, explore it
                    ModularConfigurator.exploreBlockFolder(folderPath)

                listOfDirectories[nameOfFolder] = subfolders

        if len(ModularConfigurator.folders) > 0:
            ModularConfigurator.folders.pop()
        return listOfDirectories

    ## extract information about the blocks from the filesystem, before we interact with the CLO UI
    @staticmethod
    def getBlocksFromFilesystem(blockPath):
        ModularConfigurator.folders = []

        ## Save this in the master list of blocks
        ModularConfigurator.exploreBlockFolder(blockPath)

        # for blockPath in blockPaths:
        #
        #     blockPath
        #
        #     ## When passing directories in the parameter, be sure these get added to the list of folders. As if you traversed as far.
        #     directories = blockPath.split('//')
        #     directories.pop()
        #     ModularConfigurator.folders = directories
        #     x=3
        #     ModularConfigurator.exploreBlockFolder(blockPath)

    # Iterate through all the garment folders
    @staticmethod
    def iterateThroughBlockFolders(startingFolder):
        # ModularConfigurator.log("Now inside to the " + startingFolder + " folder...")
        # Loop over Blocks (Folded shirts, Men, women)

        if ModularConfigurator.isAtTopLevel:
            i = 0
        else:
            ## Don't start with the .. / Up folder.
            i = 1

        k = 0
        for folderName in startingFolder:
            # If the "subfolder" has a dot, it isn't a folder; its garment type (single, double, etc)
            if "." in folderName:
                # Begin to iterate over these garments and their blocks
                print("Iterating over garment " + folderName)
                ModularConfigurator.activeGarment = folderName

                ## Set the ZMDR file
                ModularConfigurator.currentZMDRFile = folderName + ".zmdr"

                ModularConfigurator.iterateThroughGarmentBlocks(startingFolder[folderName])

            else:
                ModularConfigurator.log("Moving to the " + folderName + " folder...")

                ModularConfigurator.iterateThroughBlockFolders(startingFolder[folderName])

                # Go back up

            i += 1