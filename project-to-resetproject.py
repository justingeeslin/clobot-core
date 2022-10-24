import pyautogui
import time
import os
import subprocess, sys

if __name__ == '__main__':

    inputdir = "/Users/Skyward/PycharmProjects/clobot/Test Projects/"
    files = os.listdir(inputdir)
    for filename in files:
        if filename.__contains__("zprj"):
            print("--- " + filename + "---");
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, inputdir + filename])
            time.sleep(5)

            ## For the occasional prompt to either open the file or load it into the current project.
            print("Pressing enter");
            pyautogui.press('enter')

            time.sleep(10)

            ## Send the keyboard shortcut for 3D reset (R)
            print("3D Resetting");
            pyautogui.press('r');
            pyautogui.press('r');

            time.sleep(3)

            ## Save the project
            print("Saving");
            pyautogui.hotkey("command", "s")
            ### For Windoows
            pyautogui.hotkey("ctrl", "s")

            ## Repeat
            time.sleep(10)
        # break