import unittest
from CLOModularBlocks import CLOModularBlocks
import pathlib as pl

class TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class MyTestCase(TestCaseBase):
    def test_discoverBlockInformation(self):
        blockFilePath = r"C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos"
        exportFilePath = r"C:\Users\Public\Documents\CLO\clobot"
        CLOModularBlocks.discoverBlockInformation(blockFilePath, exportFilePath)

        ## Expect that the config file was discovered correctly
        self.assertEqual(CLOModularBlocks.blockConfigFilePath, r"C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos\Polos.conf")

        ## Expect that the file paths from ZMDR are correct
        self.assertIn(blockFilePath + r"\Polo.Dropped.zmdr", CLOModularBlocks.garmentCreationScriptToOutput)

    def test_writePythonScript(self):
        blockFilePath = r"C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos"
        exportFilePath = r"C:\Users\Public\Documents\CLO\clobot"
        CLOModularBlocks.discoverBlockInformation(blockFilePath, exportFilePath)

        CLOModularBlocks.scriptFilePath = r"C:\Users\Public\Documents\CLO\clobot\testcase.py"
        CLOModularBlocks.writePythonScript()

        path = pl.Path(CLOModularBlocks.scriptFilePath)
        self.assertIsFile(path)


if __name__ == '__main__':
    unittest.main()
