# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
from ModularConfigurator import ModularConfigurator

spacingBetweenModularConfiguratorFolders = 75

def exportToPNG():
    # Export / Open the Export prompt
    pyautogui.press('f10')
    # Type into the save box some file name. This might become an argument to this function
    pyautogui.write('garment')
    clickOSSave()

def clickOSSave():
    # TODO Detect where the OS Save is
    pyautogui.moveTo(1068, 529)
    # Add a delay
    # Click the Save button
    pyautogui.click()

# Press the green button in the gutter to run the script.
# TODO use grayscale matching and regions to make locateOnScreen() fast!
# ex pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400), grayscale=True)

if __name__ == '__main__':
    # Focus Clo window
    pyautogui.click(x=17, y=81)
    ModularConfigurator.open()
    ModularConfigurator.tryOnAllMensBlocks()

    # exportToPNG()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
