from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
import time
from itertools import product

from Clo import Clo

class ModularConfigurator:

    ## A list of zblocks to add to the avatar
    zBlocksToSimulate = []

    activeGarment = ""

    currentZMDRFile = ""

    countOfSimulations = 0

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

        ## Add this Zblock to the list of blocks to simulate
        blockFileName = garmentRowName + "-" + blockName + '.zblc'

        ## Make the block combinations
        listOfBlockLists = []
        for row in garmentTypesAndBlockCategories:
            garmentRowName = list(row.keys())[0]
            rowBlocks = row[garmentRowName]
            listOfBlockLists.append(rowBlocks)

        ## A list of block sets to simulate
        listOfBlockSets = list(product(*listOfBlockLists))

        for blockSet in listOfBlockSets:
            ModularConfigurator.log('Rendering..')
            ModularConfigurator.log(blockSet)

            ## Create a filename from the block set combined with the garment name
            filename = ModularConfigurator.activeGarment + '_' + '-'.join(blockSet)
            x=3

            
            mdm = MarvelousDesignerModule()
            ## Enable drapping
            mdm.SimulationOn(1)
            # Load the garments
            mdm.LoadZmdrFileWithZblc(ModularConfigurator.currentZMDRFile, ModularConfigurator.zBlocksToSimulate)
            # Call for the high quality render
            mdm.ExportRenderingImage("I:\\" + filename + ".png")

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

    @staticmethod
    def parseFolderConfig(configFilePath):
        import configparser
        config = configparser.ConfigParser()
        config.read(configFilePath)

        ## The garment subtypes (Double & Single)
        garmentSubTypes = config['Activate_Configurator_Info']['None\Activate_List'].lower().split(', ')

        ## Make a master data structure, nested tree-like structure of garment types and their block categories.
        garmentTypesAndBlockCategories = {}

        for garmentSubType in garmentSubTypes:
            ## Number of blocks for the garment subtype
            blockCategories = []
            for key in config['Activate_Configurator_Info']:
                # if "jacket.double" is in "none\jacket.double\body_back\activate_list"
                if (garmentSubType in key):
                    ## Extract only the block category name (body back, body front, sleeves)
                    blockCategory = key.replace("none", "")
                    blockCategory = blockCategory.replace(garmentSubType, "")
                    blockCategory = blockCategory.replace("activate_list", "")
                    blockCategory = blockCategory.replace("\\", "")

                    blocksString = config['Activate_Configurator_Info'][key]
                    blocksString = blocksString.replace('.zblc', '')

                    blocks = blocksString.split(", ")

                    # Prettyify the block names
                    i = 0
                    for block in blocks:
                        try:
                            blocks[i] = block.split('.')[1]
                        except IndexError:
                            x = 3
                        i += 1

                    blocksInCategory = {}

                    blocksInCategory[blockCategory] = blocks

                    blockCategory = blocksInCategory

                    blockCategories.append(blockCategory)
                    blockCategories = sorted(blockCategories, key=ModularConfigurator.sortGarmentsLikeClo)
            garmentTypesAndBlockCategories[garmentSubType] = blockCategories

        return garmentTypesAndBlockCategories

    ## The individual folder process of working with the filesystem
    @staticmethod
    def exploreBlockFolder(folderPath):
        # Things to do for each folder
        directoriesInPath = folderPath.split('/')
        currentFolderName = directoriesInPath[-1]

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
                    listOfDirectories = ModularConfigurator.parseFolderConfig(filePath)

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
                    subfolders = ModularConfigurator.exploreBlockFolder(folderPath)

                listOfDirectories[nameOfFolder] = subfolders

        return listOfDirectories

    ## extract information about the blocks from the filesystem, before we interact with the CLO UI
    @staticmethod
    def getBlocksFromFilesystem():
        # Modular configurator stores the blocks on the filesystem. Reading from the filesystem has advantages
        # ... to reading from the screen via OCR.
        pathToBlocks = '/Users/Skyward/Documents/clo/Assets/Blocks'
        ## Save this in the master list of blocks
        ModularConfigurator.blocks = ModularConfigurator.exploreBlockFolder(pathToBlocks)

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