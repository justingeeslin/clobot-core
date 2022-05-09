import pyautogui
import time

class ModularConfigurator:
    # Might Vary
    ## Might get the position of the modular configurator panel then move from there.
    blockFolderStartingPoint = [275, 192]
    ## Distance between block folders
    distanceBetweenBlocks = 75

    ## Distance bewteen the actual garment peices (fronts, backs, sleeves, etc.)
    distanceBetweenGarmentVertical = 119

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

    # Iterate through all the blocks
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
    def iterateThroughGarmentBlocks():
        ModularConfigurator.log("Iterating through the garment blocks...")
        garmentStartingPoint = [320, 484]

        ## Distance bewteen the actual garment peices (fronts, backs, sleeves, etc.)
        distanceBetweenGarmentHoriz = 70
        distanceBetweenGarmentVertical = 120

        ## Don't render anything until a full outfit is made
        madeFullOutfit = False

        # Garment columns (variants)
        for i in [0,1,2]:

            # pieces (front, back, sleeve)
            garmentsRowsToInclude = [0, 1, 2]
            for j in garmentsRowsToInclude:
                ModularConfigurator.log("Moving to the garment piece...")
                pyautogui.moveTo(
                    garmentStartingPoint[0] + distanceBetweenGarmentHoriz * i,
                    garmentStartingPoint[1] + distanceBetweenGarmentVertical * j
                )
                # Double click on Double, Single, etc.
                ModularConfigurator.log("Loading garment piece...")
                pyautogui.doubleClick()
                # Wait for it to load
                time.sleep(3)

                if (madeFullOutfit):
                    filename = "garment" + str(i) + "-" + str(j)
                    ModularConfigurator.exportToPNG(filename)

            # Full outfit is made,
            if (madeFullOutfit == False):
                madeFullOutfit = True
                filename = "garment" + str(i) + "-" + str(j)
                ModularConfigurator.exportToPNG(filename)
        ModularConfigurator.log("Complete for this modular type...")

    # Iterate through all the garment folders
    @staticmethod
    def tryOnAllMensBlocks():
        # Omit folded shirts
        blockFoldersToInclude = [1]
        # Loop over Blocks (Folded shirts, Men, women)
        for i in blockFoldersToInclude:
            pyautogui.moveTo(
                ModularConfigurator.blockFolderStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * i,
                ModularConfigurator.blockFolderStartingPoint[1]
            )
            ## Double click on Folder
            pyautogui.doubleClick()
            ## Double click on Garment Type folder (Jackets Polos, Shirts)
            pyautogui.doubleClick()

            garmentTypeFoldersToInclude = [1]
            for j in garmentTypeFoldersToInclude:
                pyautogui.moveTo(
                    ModularConfigurator.blockFolderStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * j,
                    ModularConfigurator.blockFolderStartingPoint[1]
                )

                # In the case of Jackets, Double, Single, etc
                garmentSubTypeStartingPoint = [325, 388]

                garmentTypeFoldersToInclude = [0]

                # Double, Single Jacket subtype
                for k in garmentTypeFoldersToInclude:
                    pyautogui.moveTo(
                        garmentSubTypeStartingPoint[0] + ModularConfigurator.distanceBetweenBlocks * k,
                        garmentSubTypeStartingPoint[1]
                    )
                    pyautogui.doubleClick()

                    # Start to go back up -- out of subtype
                    ## Double Click on the .. folder
                    pyautogui.moveTo(ModularConfigurator.blockFolderStartingPoint)
                    pyautogui.doubleClick()

                # Start to go back up -- out of garment type
                ## Double Click on the .. folder
                pyautogui.moveTo(ModularConfigurator.blockFolderStartingPoint)
                pyautogui.doubleClick()