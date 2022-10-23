# CLOBot
An automation robot for digital garment creation and simulation. 

## What CLOBot does
* CLOBot creates garments (lots!) by automatically putting together garment blocks.
* CLOBot uses the garment blocks created in the CLO Modular Configurator.
* CLOBot can also create simulations by placing all of those garments on a set of avatars.
* CLOBot creates a Python script to be run inside the CLO Python prompt ( Edit -> Python Script… ) . CLO’s Python API is only available on Windows for enterprise-esqe customers.

## Basics
From the Command Prompt, run the following:
```bash
clobot.exe C:\\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos C:\\Users\Public\Documents\CLO C:\\Users\Public\Documents\CLO\CLOBot\clobot.py
```

Once this process completes, you will see further instructions in the command prompt window detailing how to run CLOBot within the CLO, at CLO’s Python prompt using CLO’s Python API. 

The command line arguments are in this order:
1. The location or path on the filesystem where the blocks you want to use are located. Typically, `C:\\Users\Public\Documents\CLO\Assets\Blocks\Man\Polos`.
2. The location or path on the filesystem where the output should be saved. This might include garments, images of garments, 3D assets like OBJ files, etc. 
3. The location where you want to save the Python script CLOBot generates. Can be anywhere you like. For example: `C:\\Users\Public\Documents\CLO\clobot.py`

## Roadmap
* A UI on top of this command line tool.

## Building for Windows
This is how you build `clobot.exe` from this project written in Python. 

**This step must be done on a Windows PC.**

```commandline
pyinstaller --onefile main.py -n clobot.exe
```
