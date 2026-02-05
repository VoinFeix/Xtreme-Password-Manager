import customtkinter as ctk
from themes.themes import default_font, PADXY

def aboutTabWidgets(self, master):
    self.aboutTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.aboutTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)
