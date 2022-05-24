# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import pyautogui
import time
from ModularConfigurator import ModularConfigurator
from Clo import Clo
import beepy


spacingBetweenModularConfiguratorFolders = 75

pyautogui.FAILSAFE = True

def exportToPNG():
    # Export / Open the Export prompt
    pyautogui.press('f10')
    # Type into the save box some file name. This might become an argument to this function
    pyautogui.write('garment')
    clickOSSave()

def deleteGarment():
    # Focus the 3D garment window
    pyautogui.click(1023, 198)
    pyautogui.hotkey('command', 'a')
    pyautogui.press('delete')
    # to the Are you sure? prompt, click Yes
    time.sleep(3)
    pyautogui.click(767, 478)

# Press the green button in the gutter to run the script.
# TODO use grayscale matching and regions to make locateOnScreen() fast!
# ex pyautogui.locateOnScreen('someButton.png', region=(0,0, 300, 400), grayscale=True)

if __name__ == '__main__':
    try:
        print(Clo.getWindowSize())
        print('Please switch to CLO..')
        for i in range(5).__reversed__():
            print(i+1)
            time.sleep(1)

        # while Clo.isPrompting():


        while Clo.isLoading():
            # beepy.beep(sound="coin")
            print("loading..")


    except:
        beepy.beep(sound="error")

    # Focus Clo window
    # pyautogui.click(x=17, y=81)

    # deleteGarment()

    # ModularConfigurator.open()
    # ModularConfigurator.tryOnAllMensBlocks()
    # ModularConfigurator.iterateThroughGarmentBlocks()
    ModularConfigurator.getBlocksFromFilesystem()
    # print(ModularConfigurator.blocks)
    ModularConfigurator.iterateThroughBlockFolders(ModularConfigurator.blocks)
    # ModularConfigurator.exportToPNG()

    # print(ModularConfigurator.parseFolderConfig("/Users/Skyward/Documents/clo/Assets/Blocks/Man/Jackets/Jackets.conf"))


    # exportToPNG()

    # blockFolders = ["Man", "Woman"]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
