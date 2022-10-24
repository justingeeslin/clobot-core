
class Clo:

    # @staticmethod
    # def open():
    #     os.system("""osascript -e 'tell app "TextEdit" to open'""")

    # Minimize the vision detection by storing coordinates. Assumes some elements won't move during Clobot's running.
    # Taken at a 1440 x 900 resolution
    cachedCoordinates = {
        # Not sure why these have to be multiplied by to. Retina displays?

        # OS Level elements
        'osSaveAsInput': [819*2, 155*2],
        'osSaveButton': [1051*2, 526*2],

        # Clo UI elements
        'snapshotSaveButton' : [909*2, 544*2],
        # Possibly a general dialog affirmative location
        'proceedButton' : [664, 478]
    }
