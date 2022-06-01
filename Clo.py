import pyautogui
import time
import os

class Clo:

    # @staticmethod
    # def open():
    #     os.system("""osascript -e 'tell app "TextEdit" to open'""")

    @staticmethod
    def getWindowSize():
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
        except:            x = 3

        if box != None:
            isPrompting = True
        else:
            isPrompting = False

        return isPrompting

    @staticmethod
    def clickOSSave():
        # Detect where the OS Save is
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/button-save-macOS.png')
        except:
            x = 3

        if box != None:
            buttonPoint = pyautogui.center(box)
            buttonX, buttonY = buttonPoint
            pyautogui.click(buttonX / 2, buttonY / 2)

            # Click the final CLO save dialog
            Clo.clickOK()
            time.sleep(10)
        else:
            print("Couldn't find OS save..")
            print(box)

    @staticmethod
    def focusOSSaveAsInput():
        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/input-saveas-macOS.png')
        except:
            x = 3

        if box != None:
            buttonPoint = pyautogui.center(box)
            buttonX, buttonY = buttonPoint
            ## Adding pixels here to go to the right of the label
            pyautogui.click( (buttonX / 2) + 60, buttonY / 2)
        else:
            print("Couldn't find OS save as input..")
            print(box)

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

        buttonPoint = pyautogui.center(box)
        buttonX, buttonY = buttonPoint

        if box != None:
            pyautogui.click(buttonX / 2, buttonY / 2)