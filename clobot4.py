
from PythonQt import QtCore, QtGui, MarvelousDesignerAPI
from PythonQt.MarvelousDesignerAPI import *
import MarvelousDesigner
from MarvelousDesigner import *
import time
           
class CLOBot():

    @staticmethod
    def go(object):
        CLOBot.createGarmentsFromBlocks()
        CLOBot.createProjectsAndImagesFromGarments(object)

    @staticmethod
    def createGarmentsFromBlocks(object):

        mdm = MarvelousDesignerModule()
        
        # Load the garments
        mdm.LoadZmdrFileWithZblc("G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\BishopSleeves\\Shirt.Basic.zmdr", [
            "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\BishopSleeves\\Body_Front.zblc", 
            "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\BishopSleeves\\Cuffs.zblc", 
            "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\BishopSleeves\\Sleeves.zblc", 
            "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\BishopSleeves\\Body_Back.zblc"
        ])

        # Create the Garment file
        mdm.ExportZPac('G:\\My Drive\\CLOBot Creations\\CustomBlocks-BishopSleeves.zpac')

        # mdm.LoadZmdrFileWithZblc("G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\dolman\\T-Shirt.Basic.zmdr", [
        #     "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\dolman\\Sleeves.zblc", 
        #     "G:\\Shared drives\\Wearable Technology Lab\\Projects\\Smart Wardrobe\\J. CloBot\\CustomBlocks\\3DResetBlocksBlocks\\Sweaters\\dolman\\Body.zblc"
        # ])
        # mdm.ExportZPac('G:\\My Drive\\CLOBot Creations\\CustomBlocks-Dolman.zpac')

    @staticmethod
    def garmentsToProjects(object):
        ## From the garments (zpac) to Projects per avatar (unsimulated, and un-reset)

        garments = [
            "CustomBlocks-BishopSleeves.zpac"
        ]

        avatars = [
            "Test651\ID_651.avt"
        ]

        for avatar in avatars:
            for garment in garments:

                #initialize object module
                object.initialize()

                #Set importing options (unit) of string type
                object.set_import_scale_unit("mm")

                #Set exporting options (unit) of string type
                object.set_export_scale_unit("mm")

                # Load the avatar
                object.set_avatar_file_path("C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\\" + avatar)

                #next multi process
                object.set_garment_file_path('G:\\My Drive\\CLOBot Creations\\' + garment)
                object.sync_file_lists("animation")

                ##set a save path for these projects, unsimulated, and unreset
                filename = garment + "_" + avatar
                object.set_save_folder_path('G:\\My Drive\\CLOBot Creations\\NonReset\\', "zprj")
                # object.set_save_file_path('G:\\My Drive\\CLOBot Creations\\NonReset\\' + filename + '.zprj')

                #set auto save option. True is save with Zprj File and Image File.
                object.set_auto_save(True)
                #call the "process" function (to autosave project file, change factor to ture)
                object.process()

    @staticmethod
    def createResetGarmentsFromResetProjects(object):
        # Garments to Images & Projects
        mdm = MarvelousDesignerModule()    

        ## Insert Reset projects
        projects = [
            # "CustomBlocks-BishopSleeves-ID_651.zprj",
            "CustomBlocks-BishopSleeves (10).zprj"
        ]

        for project in projects:

            mdm.ImportZprj("G:\My Drive\CLOBot Creations\\" + project, False)
        
            mdm.ExportZPac("G:\My Drive\CLOBot Creations\\Garment1 Unsimulated ID_651.zpac")

    @staticmethod
    def createSimulationsFromResetGarments(object):

        garments = [
            "Garment1 Unsimulated ID_651.zpac"
        ]

        avatars = [
            "Test651\ID_651.avt"
        ]

        for avatar in avatars:
            for garment in garments:
                #initialize object module
                object.initialize()

                #Set importing options (unit) of string type
                object.set_import_scale_unit("mm")

                #Set exporting options (unit) of string type
                object.set_export_scale_unit("mm")

                #Set simulation option.
                # 1 Complete
                # 0 Normal
                # 2 Custom
                simulation_quality = 0
                object.set_simulation_options(0, simulation_quality, 10000) 

                # Load the avatar
                object.set_avatar_file_path("C:\Users\Public\Documents\CLO\Assets\Avatar\Avatar\\" + avatar)

                #next multi process
                object.set_garment_file_path('G:\\My Drive\\CLOBot Creations\\' + garment)
                object.sync_file_lists("animation")
            
                object.set_save_folder_path('G:\\My Drive\\CLOBot Creations\\', "obj")

                #set auto save option. True is save with Zprj File and Image File.
                object.set_auto_save(True)
                #call the "process" function (to autosave project file, change factor to ture)
                object.process()            
    