import sys
import os
try:
    filepath = os.path.abspath('src/')
    # print(f"FilePath: {filepath}")
    sys.path.append(filepath)
except Exception as e:
    print('Error Importing Modules')
    print(str(e))
    sys.exit(1)
else:
    pass
    # sys.exit(1)

import customtkinter as ctk
from themes.themes import DEFAULT_APPEARANCE_MODE, DEFAULT_THEME, default_font, heading_font
from utils.keyBindings import keyBinds
from gui.heading import headingWidget

WINDOW_NAME = 'Xtreme Password Manager'
HEIGHT = 650
WIDTH = 450
GEOMETRY = f"{HEIGHT}x{WIDTH}"


class XPM:
    def __init__(self, root):
        self.root = root
        self.root.title(WINDOW_NAME)
        self.root.geometry(GEOMETRY)
        ctk.set_appearance_mode(DEFAULT_APPEARANCE_MODE)
        ctk.set_default_color_theme(DEFAULT_THEME)
        self.root.columnconfigure(0, weight=1)

        headingWidget(self)    


        
        keyBinds(self)



if __name__ == '__main__':
    root = ctk.CTk()
    app = XPM(root)
    root.mainloop()