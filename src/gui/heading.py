import customtkinter as ctk
from themes.themes import heading_font

def headingWidget(self):
    self.headingFrame = ctk.CTkFrame(self.root, border_color='black', border_width=3)
    self.headingFrame.grid(row=0, column=0, padx=10, pady=10, sticky='EW')

    self.heading = ctk.CTkLabel(self.headingFrame, text='Xtreme Password Manager', font=heading_font)
    self.heading.pack(padx=5, pady=5)