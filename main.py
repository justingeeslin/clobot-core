import sys
from CLOModularBlocks import CLOModularBlocks

if __name__ == '__main__':

    ## Establish whether in debug mode
    isDebug = False
    gettrace = getattr(sys, 'gettrace', None)
    if gettrace():
        isDebug = True


    blockPath = "";
    ## Woman\\T-Shirts,Woman\\Trench Coats
    hasSufficentArguments = True;
    if len(sys.argv) > 1:
        blockPath = sys.argv[1]
    else:
        print("Please supply the path for the blocks. Ex: C:\\\\Users\Public\Documents\CLO\Assets\Blocks\\")
        hasSufficentArguments = False;

    outputPath = "";
    if len(sys.argv) > 2:
        outputPath = sys.argv[2]
    else:
        print("Please supply the output path i.e. where do you want to resutling Python script to go. . Ex: C:\\\\Users\Public\Documents\CLO\CLOBot\Scripts\\")
        hasSufficentArguments = False;

    if not hasSufficentArguments:
        exit(1)

    CLOModularBlocks.discoverBlockInformation(blockPath, outputPath)

    CLOModularBlocks.scriptFilePath = "/Users/Skyward/Documents/clo/CLOBot/test-case.py"
    CLOModularBlocks.writePythonScript()