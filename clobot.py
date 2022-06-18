from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
from instructions import CLOBotInstructions

class CLOBot():

    @staticmethod
    def testSimulate(object):
        # Blocks to Garments
        mdm = MarvelousDesignerAPI.MarvelousDesignerModule()
        ## Enable drapping
        mdm.SimulationOn(1)
        ## Load the modular configurator blocks
        mdm.LoadZmdrFileWithZblc("C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\\Polo.Dropped.zmdr", ["C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Body_Dropped.Regular.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Collar.ButtonDown.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Sleeves_Dropped.Long.zblc"])
        ## High-quality render of the image
        #mdm.ExportRenderingImage("I:\exportRenderImage.png")
        mdm.ExportZPac("Y:\polo-test-1.zpac")

        ## Load the modular configurator blocks
        mdm.LoadZmdrFileWithZblc("C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\\Polo.Dropped.zmdr", ["C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Body_Dropped.Regular.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Collar.ButtonDown.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Sleeves_Dropped.Short.zblc"])
        mdm.ExportZPac("Y:\polo-test-2.zpac")

        ## Load the modular configurator blocks
        mdm.LoadZmdrFileWithZblc("C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\\Polo.Dropped.zmdr", ["C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Body_Dropped.Regular.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Collar.ButtonDown.zblc", "C:\\Users\Public\Documents\CLO\Assets\\Blocks\Woman\Polos\Sleeves_Set-In.Long.zblc"])
        mdm.ExportZPac("Y:\polo-test-2.zpac")

        # Garments to Images & Projects
        # clear console window
        object.clear_console() 
        #initialize object module
        object.initialize()

        #Set importing options (unit) of string type
        object.set_import_scale_unit("mm")

        #Set exporting options (unit) of string type
        object.set_export_scale_unit("mm")
        
        #Set simulation property settings
        #Set Simulation property options(simulation quality) of integer type
        # qulity = 0 Complete
        # qulity = 1 Normal
        # qulity = 2 Custom
        object.set_simulation_quality(1)

        # Load the avatar
        object.set_avatar_file_path("C:\\Users\\Public\\Documents\\CLO\\Assets\\Avatar\\Avatar\\Female_V2\\Avatar (Modular)\\Modular_FV2_Feifei.avt")

        #next multi process
        object.set_garment_file_path("Y:\polo-test-1.zpac")
        object.sync_file_lists("animation")
        #next multi process
        object.set_garment_file_path("Y:\polo-test-2.zpac")
        object.sync_file_lists("animation")

        object.set_garment_file_path("Y:\polo-test-3.zpac")
        object.sync_file_lists("animation")

        object.set_save_folder_path("Y:\\", "pdf")
        # object.set_save_folder_path("Y:\\", "png")
        #set auto save option. True is save with Zprj File and Image File.
        object.set_auto_save(True)
        #call the "process" function (to autosave project file, change factor to ture)
        object.process()

    ## Simulate all the block combinations in the modular configurator
    @staticmethod
    def simulateAllModularBlocks():
        ModularConfigurator.getBlocksFromFilesystem()
        ModularConfigurator.iterateThroughBlockFolders(ModularConfigurator.blocks)
        print("Number of simulations:")
        print(ModularConfigurator.countOfSimulations)

        ## Run the imported instructions
