import time
import unittest
import pyautogui
from Clo import Clo

class TestingClo(unittest.TestCase):

    # # To run this test, snapshot from Clo's 3d window. When the OS prompt appears, run this
    # def test_OSSaveAsInput(self):
    #     Clo.focusOSSaveAsInput()
    #
    #     self.assertNotEqual(Clo.cachedCoordinates['osSaveAsInput'], None)
    #
    # def test_clickOSSave(self):
    #     Clo.clickOSSave()
    #
    #     self.assertNotEqual(Clo.cachedCoordinates['osSaveButton'], None)
    #
    # # Testing the Clicking of Clo's Save button
    # def test_clickSave(self):
    #     Clo.clickSave()
    #
    #     self.assertNotEqual(Clo.cachedCoordinates['snapshotSaveButton'], None)

    def test_snapshot3DWindow(self):
        Clo.snapshot3DWindow()

if __name__ == '__main__':
    print('Please switch to CLO..')
    for i in range(5).__reversed__():
        print(i + 1)
        time.sleep(1)
    unittest.main()
