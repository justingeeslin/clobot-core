import pyautogui

class ModularConfigurator:
    # Might Vary
    ## Might get the position of the modular configurator panel then move from there.
    blockFolderStartingPoint = [275, 192]
    distanceBetweenBlocks = 75

    #
    @staticmethod
    def open():
        pyautogui.moveTo(14, 259)
        pyautogui.click()

    @staticmethod
    def isAtTopLevel():
        isAtTopLevel = False

        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/blocks-breadcrumb.png')
        except:
            # If you fail to see the breadcrumb you are at the top level
            isAtTopLevel = True

        return isAtTopLevel

    # Move to the blocks tab
    @staticmethod
    def moveToBlocks():
        pyautogui.moveTo(blockFolderStartingPoint)

    # Iterate through all the blocks
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