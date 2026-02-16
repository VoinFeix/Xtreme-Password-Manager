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
from themes.themes import DEFAULT_APPEARANCE_MODE, DEFAULT_THEME, default_font, heading_font, DEFAULT_APPEARANCE_MODE_FILENAME, DEFAULT_THEME_FILENAME, available_themes
from utils.keyBindings import keyBinds
from gui.heading import headingWidget
from gui.tabs import tabsWidget


def getThemes():
    try:
        with open(DEFAULT_THEME_FILENAME, 'r', encoding='utf-8') as f:
            theme = f.read()
            if not theme:
                THEME = DEFAULT_THEME
            else:
                THEME = theme
    except FileNotFoundError:
        THEME = DEFAULT_THEME

    try:
        with open(DEFAULT_APPEARANCE_MODE_FILENAME, 'r', encoding='utf-8') as f:
            appearanceMode = f.read()
            if not appearanceMode:
                APPEARANCE_MODE = DEFAULT_APPEARANCE_MODE
            else:
                APPEARANCE_MODE = appearanceMode
    except FileNotFoundError:
        APPEARANCE_MODE = DEFAULT_APPEARANCE_MODE

    return THEME, APPEARANCE_MODE
THEME, APPEARANCE_MODE = getThemes()

WINDOW_NAME = 'Xtreme Password Manager'
HEIGHT = 612
WIDTH = 625
GEOMETRY = f"{HEIGHT}x{WIDTH}"
RESIZEABLE_WIDTH = False
RESIZEABLE_HEIGHT = False


class XPM(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title(WINDOW_NAME)
        self.geometry(GEOMETRY)
        self.resizable(RESIZEABLE_WIDTH, RESIZEABLE_HEIGHT)
        ctk.set_appearance_mode(APPEARANCE_MODE)
        ctk.set_default_color_theme(available_themes[THEME])
        
        # self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        headingWidget(self)

        tabsWidget(self)

        keyBinds(self)1



if __name__ == '__main__':
    # root = ctk.CTk()
    app = XPM()
    app.mainloop()
    # root.mainloop()
