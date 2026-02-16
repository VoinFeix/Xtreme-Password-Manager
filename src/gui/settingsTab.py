import customtkinter as ctk
from themes.themes import DEFAULT_APPEARANCE_MODE, DEFAULT_THEME, default_font, PADXY, available_themes, DEFAULT_APPEARANCE_MODE_FILENAME, DEFAULT_THEME_FILENAME


def settingsTabWidget(self, master):
    self.settingsTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.settingsTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)
    
    self.appearanceModes: list = ["System", "Light", "Dark"]
    self.appearanceMode_value = ctk.StringVar()

    self.appearanceModeLabel = ctk.CTkLabel(self.settingsTabFrame, text='Appearance Mode:', font=default_font)
    self.appearanceModeLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.appearanceModeOptionMenu = ctk.CTkOptionMenu(self.settingsTabFrame, font=default_font, command=self.setAppearanceMode_func, variable=self.appearanceMode_value, values=self.appearanceModes)
    self.appearanceModeOptionMenu.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.appearanceModeOptionMenu.set(self.appearanceModes[self.appearanceModes.index(getAppearanceMode())])

    self.availThemes: list = [*list(available_themes.keys())]
    self.selectTheme_value = ctk.StringVar()

    self.selectThemeOptionMenuLabel = ctk.CTkLabel(self.settingsTabFrame, text='Theme:', font=default_font)
    self.selectThemeOptionMenuLabel.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.selectThemeOptionMenu = ctk.CTkOptionMenu(self.settingsTabFrame,  font=default_font, command=self.setTheme_func, variable=self.selectTheme_value, values=self.availThemes)
    self.selectThemeOptionMenu.grid(row=1, column=1, padx=PADXY, pady=PADXY)
    self.selectThemeOptionMenu.set(self.availThemes[self.availThemes.index(getTheme())])

    self.noteFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.noteFrame.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.label0 = ctk.CTkLabel(self.noteFrame, text='💡 Note:  Restart program to make changes. ', font=default_font)
    self.label0.grid(row=0, column=0, padx=PADXY, pady=PADXY)

def setAppearanceMode_func(self, *args) -> None:
    try:
        with open(DEFAULT_APPEARANCE_MODE_FILENAME, 'w', encoding='utf-8') as f:
            f.write(self.appearanceMode_value.get())
            
    except FileNotFoundError: return None

def setTheme_func(self, *args) -> None:
    try:
        with open(DEFAULT_THEME_FILENAME, 'w', encoding='utf-8') as f:
            f.write(self.selectTheme_value.get())
    except FileNotFoundError: return None

def getAppearanceMode() -> str:
    try:
        with open(DEFAULT_APPEARANCE_MODE_FILENAME, 'r', encoding='utf-8') as f:
            appearanceMode = f.read()
            if not appearanceMode:
                raise FileNotFoundError
            else:
                return appearanceMode
    except FileNotFoundError: return DEFAULT_APPEARANCE_MODE

def getTheme() -> str:
    try:
        with open(DEFAULT_THEME_FILENAME, 'r', encoding='utf-8') as f:
            theme = f.read()
            if not theme:
                raise FileNotFoundError
            else:
                return theme
    except FileNotFoundError: return DEFAULT_THEME