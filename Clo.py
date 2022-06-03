import pyautogui
import time
import os
import shutil

class Clo:

    # @staticmethod
    # def open():
    #     os.system("""osascript -e 'tell app "TextEdit" to open'""")

    # Minimize the vision detection by storing coordinates. Assumes some elements won't move during Clobot's running.
    # Taken at a 1440 x 900 resolution
    cachedCoordinates = {
        # Not sure why these have to be multiplied by to. Retina displays?

        # OS Level elements
        'osSaveAsInput': [819*2, 155*2],
        'osSaveButton': [1051*2, 526*2],

        # Clo UI elements
        'snapshotSaveButton' : [909*2, 544*2],
        # Possibly a general dialog affirmative location
        'proceedButton' : [664, 478]
    }

    freeGB = 0

    @staticmethod
    def pre():
        ## Determine the screen resolution
        currentResolution = Clo.getWindowSize()

        ## Determine a scaling factor
        xScale = currentResolution[0] / 1440
        yScale = currentResolution[1] / 900

        ## Update the coordinate list
        for coordName in Clo.cachedCoordinates:
            x,y = Clo.cachedCoordinates[coordName]
            x = x * xScale
            y = y * yScale
            Clo.cachedCoordinates[coordName] = [x,y]

        ## Determine disk space - useful for determining if some prompts regarding low disk space will appear
        total, used, free = shutil.disk_usage("/")
        Clo.freeGB = free // (2 ** 30)

    @staticmethod
    def getWindowSize():
        ## TODO Add logic here to detect the window size not just the screen res. You might CV the little refersh button in the lower right corner

        return pyautogui.size()

    @staticmethod
    def isLoading():
        # TODO Consider updates for the mid poiont of the screen.
        coordsOfLoadingBox = [863*2, 411*2]
        cloGray = (75, 75, 76)
        ## You could say get color and do some math since its a gradient
        cloBlue = (0, 182, 255)

        return pyautogui.pixelMatchesColor(coordsOfLoadingBox[0], coordsOfLoadingBox[1], cloGray) | pyautogui.pixelMatchesColor(coordsOfLoadingBox[0], coordsOfLoadingBox[1], cloBlue, tolerance= 10)

    @staticmethod
    def isPrompting():
        # Is there a cancel button?
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/clo_button_cancel.png')
        except:
            x = 3

        if box != None:
            isPrompting = True
        else:
            isPrompting = False

        return isPrompting

    @staticmethod
    def snapshot3DWindow(filename = None):
        import random
        # # Export / Open the Export prompt
        pyautogui.press('f10')

        ## Issue a click to the Warning dialog, aboout file size. As I understand it CLO will prompt if you have less than 10GB free
        print("Free GB:")
        print(Clo.freeGB)
        if Clo.freeGB < 10:

            while not Clo.isPrompting():
                print("Sleeping while we wait for the disk space prompt..")
                pyautogui.sleep(1)
            # Click Proceed
            print("I see the disk space prompt.. clicking Proceed.")
            pyautogui.click(Clo.cachedCoordinates['proceedButton'][0], Clo.cachedCoordinates['proceedButton'][1])

        pyautogui.sleep(10)

        ## Focus the save as input field - MacOS save box
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        # pyautogui.press('tab')
        Clo.focusOSSaveAsInput()

        number = '0123456789483034769032842035732459074983'
        if filename is None:
            filename = "test-" + random.choice(number)

        # # Type into the save box some file name. Ensure its almost never the same.
        pyautogui.write(filename + random.choice(number) + random.choice(number) + random.choice(number))
        Clo.clickOSSave()

        time.sleep(10)

        # Handle the CLO export prompt
        Clo.clickSave()

    @staticmethod
    def _detectOSSave():
        # Detect where the OS Save is
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/button-save-macOS.png')
        except:
            x = 3
            print("Couldn't detect OS save..")
            print(box)
        return box

    @staticmethod
    def clickOSSave():
        if Clo.cachedCoordinates['osSaveButton'] is not None:
            box = Clo.cachedCoordinates['osSaveButton']
        else:
            box = Clo._detectOSSave()
            # Save so you don't have to use computer vision repeatedly.
            Clo.cachedCoordinates['osSaveButton'] = pyautogui.center(box)

        if Clo.cachedCoordinates['osSaveButton'] is not None:
            buttonX, buttonY = Clo.cachedCoordinates['osSaveButton']
            pyautogui.click(buttonX / 2, buttonY / 2)

        else:
            print("Couldn't find OS save, detected or cached..")
            print(box)

    @staticmethod
    def focusOSSaveAsInput():
        if Clo.cachedCoordinates['osSaveAsInput'] is None:
            try:
                print("Trying to locate on screen save as field..")
                pyautogui.screenshot('test.png')
                box = pyautogui.locateOnScreen('screenshotsForDetection/input-saveas-macOS.png')
                Clo.cachedCoordinates['osSaveAsInput'] = pyautogui.center(box)
            except:
                x = 3

        if Clo.cachedCoordinates['osSaveAsInput'] is not None:
            buttonPoint = Clo.cachedCoordinates['osSaveAsInput']
            buttonX, buttonY = buttonPoint
            ## Adding pixels here to go to the right of the label
            pyautogui.click( (buttonX / 2) + 60, buttonY / 2)
        else:
            print("Couldn't find OS save as input..")
            print(Clo.cachedCoordinates['osSaveAsInput'])

    @staticmethod
    def clickCancel():
        # Is there a cancel button?
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/clo_button_cancel.png')
        except:
            x = 3

        buttonPoint = pyautogui.center(box)
        buttonX, buttonY = buttonPoint
        if box != None:
            pyautogui.click(buttonX/2, buttonY/2)

    @staticmethod
    def clickOK():
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/clo_button_ok.png')
        except:
            x = 3

        if box != None:
            buttonPoint = pyautogui.center(box)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX / 2, buttonY / 2)

    # This function is written to be a Snapshot Save, but could/should be generalized to be a click Save function.
    @staticmethod
    def clickSave():
        if Clo.cachedCoordinates['snapshotSaveButton'] is None:
            try:
                print("Trying to locate on screen CLO Save button..")
                pyautogui.screenshot('test.png')
                box = pyautogui.locateOnScreen('screenshotsForDetection/clo_button_save.png')
                Clo.cachedCoordinates['osSaveAsInput'] = pyautogui.center(box)
            except:
                x = 3

        if Clo.cachedCoordinates['snapshotSaveButton'] is not None:
            buttonPoint = Clo.cachedCoordinates['snapshotSaveButton']
            buttonX, buttonY = buttonPoint
            ## Adding pixels here to go to the right of the label
            pyautogui.click( (buttonX / 2), buttonY / 2)
        else:
            print("Couldn't find OS CLO Save button..")
            print(Clo.cachedCoordinates['snapshotSaveButton'])
