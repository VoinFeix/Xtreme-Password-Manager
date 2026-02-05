import customtkinter as ctk
from themes.themes import default_font, PADXY, available_themes

def settingsTabWidget(self, master):
    self.settingsTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.settingsTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)
    
    

    self.availThemes: list = [*list(available_themes.keys())]
    self.selectTheme_value = ctk.StringVar()

    self.selectThemeOptionMenuLabel = ctk.CTkLabel(self.settingsTabFrame, text='Theme:', font=default_font)
    self.selectThemeOptionMenuLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.selectThemeOptionMenu = ctk.CTkOptionMenu(self.settingsTabFrame,  font=default_font, command=self.setTheme_func, variable=self.selectTheme_value, values=self.availThemes)
    self.selectThemeOptionMenu.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.selectThemeOptionMenu.set(self.availThemes[0])


def setTheme_func(self, *args, **kwargs):
    theme = self.selectTheme_value.get()
    ctk.set_default_color_theme(available_themes[theme])
    print('Applied')