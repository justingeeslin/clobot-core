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
        print(r"Please supply the path for the CLO blocks. ex. C:\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos")
        hasSufficentArguments = False;

    avatarPath = "";
    if len(sys.argv) > 2:
        avatarPath = sys.argv[2]
    else:
        print(r"Please supply the path for the CLO avatars. ex. C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\Female_V2")
        hasSufficentArguments = False;

    outputPath = "";
    if len(sys.argv) > 3:
        outputPath = sys.argv[3]
    else:
        print(r"Please supply where the files created should go. ex. C:\Users\Public\Documents\CLO\clobot")
        hasSufficentArguments = False;

    scriptFilePath = "";
    if len(sys.argv) > 4:
        scriptFilePath = sys.argv[4]
    else:
        print(r"Please supply where resulting Python script should go. ex. C:\Users\Public\Documents\CLO\clobot\testcase.py")
        hasSufficentArguments = False;

    if not hasSufficentArguments:
        sys.exit(1)


    CLOModularBlocks.discoverBlockInformation(blockPath, avatarPath, outputPath)

    CLOModularBlocks.scriptFilePath = scriptFilePath
    CLOModularBlocks.writePythonScript()