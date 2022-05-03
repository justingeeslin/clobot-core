import unittest
import pyautogui
from ModularConfigurator import ModularConfigurator

class TestingModularConfigurator(unittest.TestCase):
    def test_open(self):
        ModularConfigurator.open()
        isConfiguratorOpen = True

        try:
            box = pyautogui.locateOnScreen('screenshotsForDetection/panel_modConfig.png')
        except:
            isConfiguratorOpen = False

        self.assertEqual(isConfiguratorOpen, True)

    def test_isAtTop(self):
        self.assertEqual(ModularConfigurator.isAtTopLevel(), True)

if __name__ == '__main__':
    unittest.main()
