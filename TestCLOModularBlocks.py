import unittest
from CLOModularBlocks import CLOModularBlocks
import pathlib as pl

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class MyTestCase(TestCaseBase):
    def test_discoverBlockInformation(self):
        blockFilePath = "/Users/Skyward/Documents/clo/Assets/Blocks/Man/Polos/"
        exportFilePath = "/Users/Skyward/Documents/clo/CLOBot/"
        CLOModularBlocks.discoverBlockInformation(blockFilePath, exportFilePath)

        ## Expect that the config file was discovered correctly
        self.assertEqual(CLOModularBlocks.blockConfigFilePath, "/Users/Skyward/Documents/clo/Assets/Blocks/Man/Polos/Polos.conf")

        ## Expect that the file paths from ZMDR are correct
        self.assertIn(blockFilePath + "Polo.Dropped.zmdr", CLOModularBlocks.garmentCreationScriptToOutput)

    def test_writePythonScript(self):
        blockFilePath = "/Users/Skyward/Documents/clo/Assets/Blocks/Man/Polos/"
        exportFilePath = "/Users/Skyward/Documents/clo/CLOBot/"
        CLOModularBlocks.discoverBlockInformation(blockFilePath, exportFilePath)

        CLOModularBlocks.scriptFilePath = "/Users/Skyward/Documents/clo/CLOBot/test-case.py"
        CLOModularBlocks.writePythonScript()

        path = pl.Path(CLOModularBlocks.scriptFilePath)
        self.assertIsFile(path)


if __name__ == '__main__':
    unittest.main()
