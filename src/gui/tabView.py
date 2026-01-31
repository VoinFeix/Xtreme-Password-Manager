import customtkinter as ctk
from themes.themes import default_font
from .generateTab import generateTabWidgets
from .generateTab import charSliderEvent, advanchedOption_func, genPass_func, copyPass_func, clearCopyStatus_func
# from utils.keyBindings import generateTabBinding

class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add('Generate')
        self.add('Login')
        self.add('Saved')
        self.add('About')
        self.add('Settings')

        generateTabWidgets(self, master=self.tab('Generate'))
        self.loginTabWidgets(self.tab('Login'))
        self.savedTabWidgets(self.tab('Saved'))
        self.aboutTabWidgets(self.tab('About'))
        self.settingsTabWidgets(self.tab('Settings'))
        
        # generateTabBinding(self.tab('Generate'))

    def charSliderEvent(self, *args):
        charSliderEvent(self, *args)
    
    def genPass_func(self,):
        genPass_func(self)

    def advanchedOption_func(self):
        advanchedOption_func(self)

    def copyPass_func(self):
        copyPass_func(self)
    
    def clearCopyStatus_func(self):
        clearCopyStatus_func(self)


    def loginTabWidgets(self, master):
        self.loginTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.loginTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.loginHeading = ctk.CTkLabel(self.loginTabFrame, text='Hello LoginTab', font=default_font)
        self.loginHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    def savedTabWidgets(self, master):
        self.savedTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.savedTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.savedHeading = ctk.CTkLabel(self.savedTabFrame, text='Hello SavedTab', font=default_font)
        self.savedHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    def aboutTabWidgets(self, master):
        self.aboutTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.aboutTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.aboutHeading = ctk.CTkLabel(self.aboutTabFrame, text='Hello AboutTab', font=default_font)
        self.aboutHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    def settingsTabWidgets(self, master):
        self.settingsTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.settingsTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.settingsHeading = ctk.CTkLabel(self.settingsTabFrame, text='Hello SettingsTab', font=default_font)
        self.settingsHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
