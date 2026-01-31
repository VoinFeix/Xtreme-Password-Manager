import customtkinter as ctk
from .tabView import TabView

def tabsWidget(self):
    self.tabsFrame = ctk.CTkFrame(master=self, border_color='black', border_width=3)
    self.tabsFrame.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

    self.tabView = TabView(master=self.tabsFrame, width=550, height=500)
    self.tabView.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

