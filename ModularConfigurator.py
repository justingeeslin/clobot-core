import pyautogui
import time

from Clo import Clo

class ModularConfigurator:
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

    def __init__(self):
        self.data = []

    @staticmethod
    def log(msg):
        ## Replace later when you have a way of showing notifications to the user.
        print(msg)

    #
    @staticmethod
    def open():
        pyautogui.moveTo(14, 259)
        pyautogui.click()

    @staticmethod
    def isAtTopLevel():

        box = pyautogui.locateOnScreen('screenshotsForDetection/blocks-breadcrumb.png')

        if box == None:
            isAtTopLevel = True
        else:
            isAtTopLevel = False

        return isAtTopLevel

    # Move to the blocks tab
    @staticmethod
    def moveToBlocks():
        pyautogui.moveTo(blockFolderStartingPoint)

    @staticmethod
    def iterateThroughGarmentSubtypeBlocks():
        # In the case of Jackets, Double, Single, etc
        garmentSubTypeStartingPoint = [325, 388]

        garmentTypeFoldersToInclude = [0]

        # Double, Single Jacket subtype
        for k in garmentTypeFoldersToInclude:
            ModularConfigurator.log("Move to a garment subtype...")
            pyautogui.moveTo(
                garmentSubTypeStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * k,
                garmentSubTypeStartingPoint[1]
            )
            pyautogui.doubleClick()

            # Start to go back up -- out of subtype
            ## Double Click on the .. folder
            time.sleep(3)
            pyautogui.moveTo(ModularConfigurator.blockFolderStartingPoint)
            pyautogui.doubleClick()

    @staticmethod
    def exportToPNG(filename):
        time.sleep(3)
        pyautogui.hotkey('command', 'shift', '3')
        time.sleep(3)
        # # Export / Open the Export prompt
        # pyautogui.press('f10')
        # time.sleep(10)
        #
        # # Focus the Save File dialog input
        # pyautogui.click(x=700, y=155)
        #
        # # Type into the save box some file name. This might become an argument to this function
        # pyautogui.write(filename)
        # ModularConfigurator.clickOSSave()

    @staticmethod
    def clickOSSave():
        # TODO Detect where the OS Save is
        # saveButtonBox = pyautogui.locateOnScreen('screenshotsForDetection/button-save-macOS.png')
        pyautogui.moveTo(1068, 529)

        # Click the Save button
        pyautogui.click()
        time.sleep(10)
        # Click the final CLO save dialog
        pyautogui.click(x=898, y=541)
        time.sleep(10)

        # if (saveButtonBox == None):
        #     # What should I do here?
        #     return
        # else:
        #     pyautogui.moveTo(saveButtonBox)
        #     # Click the Save button
        #     pyautogui.click()
        #     time.sleep(1)
        #     # Click the final CLO save dialog
        #     pyautogui.click(x=898, y=541)
        #     time.sleep(3)

    ## Individual action for the recursive process
    @staticmethod
    def iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex, colIndex):
        garmentRow = garmentTypesAndBlockCategories[rowIndex]
        garmentRowName = list(garmentRow.keys())[0]

        try:
            blockName = garmentRow[garmentRowName][colIndex]
        except IndexError:
            ModularConfigurator.log("No block at " + colIndex + " for " + garmentRowName);
            return

        ModularConfigurator.log("Exploring " + garmentRowName + ", " + blockName)

        garmentStartingPoint = [320, 484]

        # Distance bewteen the actual garment peices (fronts, backs, sleeves, etc.)
        distanceBetweenGarmentHoriz = 70
        distanceBetweenGarmentVertical = 120

        ModularConfigurator.log("Moving to the garment piece...")
        pyautogui.moveTo(
            garmentStartingPoint[0] + distanceBetweenGarmentHoriz * colIndex,
            garmentStartingPoint[1] + distanceBetweenGarmentVertical * rowIndex
        )
        # Double click on Double, Single, etc.
        ModularConfigurator.log("Loading garment piece...")
        pyautogui.doubleClick()
        # Wait for it to load - TODO replace with an isLoading to see if this makes it faster.
        time.sleep(3)
        ModularConfigurator.log('Taking a screenshot..')

        if len(garmentTypesAndBlockCategories) > rowIndex+1:
            ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex+1, colIndex)

        if len(garmentTypesAndBlockCategories[rowIndex][garmentRowName]) > colIndex + 1:
            ModularConfigurator.iterateThroughGarmentBlockRow(garmentTypesAndBlockCategories, rowIndex, colIndex + 1)

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

                # Click the garment type (Single or double)
                pyautogui.moveTo(
                    ModularConfigurator.garmentSubTypeStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * k,
                    ModularConfigurator.garmentSubTypeStartingPoint[1]
                )
                pyautogui.doubleClick()
                # Advanced to the next garment type
                k += 1

                if ModularConfigurator.areBlocksActive:
                    while not Clo.isLoading():
                        ModularConfigurator.log("Sleeping while you load the loading..")
                        time.sleep(1)

                    while Clo.isLoading():
                        ModularConfigurator.log("Sleeping while you load the prompt..")
                        time.sleep(1)

                    ## Check to see if CLO is prompting
                    ModularConfigurator.log("Is CLO prompting? ")
                    if Clo.isPrompting():
                        ModularConfigurator.log("Clicking OK in the prompt")
                        Clo.clickOK()

                        ## Wait while clo loads comperable blocks
                        while Clo.isLoading():
                            ModularConfigurator.log("Sleeping while you load comperable blocks..")
                            time.sleep(1)

                ModularConfigurator.log("thank u next")
                ModularConfigurator.iterateThroughGarmentBlocks(startingFolder[folderName])
                ModularConfigurator.areBlocksActive = True

            else:
                ModularConfigurator.log("Moving to the " + folderName + " folder...")
                pyautogui.moveTo(
                    ModularConfigurator.blockFolderStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * i,
                    ModularConfigurator.blockFolderStartingPoint[1]
                )
                time.sleep(3)
                ## Double click on Folder
                ModularConfigurator.log("Open the folder...")
                pyautogui.doubleClick()
                ModularConfigurator.isAtTopLevel = False
                ## When switching folders, CLO will not try to prompt to replace from comperable blocks
                ModularConfigurator.areBlocksActive = False
                time.sleep(3)

                ModularConfigurator.iterateThroughBlockFolders(startingFolder[folderName])

                # Go back up
                ## Double Click on the .. folder
                time.sleep(3)
                pyautogui.moveTo(ModularConfigurator.blockFolderStartingPoint)
                pyautogui.doubleClick()

            # ## Double click on Garment Type folder (Jackets Polos, Shirts)
            # pyautogui.doubleClick()
            # time.sleep(3)

            # if len(ModularConfigurator.blocks[folderName]) == 0:
            #     continue

            # for subfolder in startingFolder[folderName]:
            #     # If the "subfolder" has a dot, it isn't a folder its garment type (single, double, etc)
            #     if "." in subfolder:
            #         # Begin to iterate over these garments and their blocks
            #         print("Iterating over garment " + subfolder)
            #     else:
            #         print("Has Subfolder " + subfolder)
            #         print(startingFolder[folderName][subfolder])
            #         ModularConfigurator.iterateThroughBlockFolders(startingFolder[folderName][subfolder])

            i += 1