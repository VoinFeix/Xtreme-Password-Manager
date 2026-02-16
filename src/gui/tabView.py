import customtkinter as ctk
from themes.themes import default_font
from .generateTab import generateTabWidgets, passwordStrengthEvent
from .generateTab import charSliderEvent, advanchedOption_func, genPass_func, copyPass_func, clearStatus_func, passwordStrengthEvent
from .loginTab import loginTabWidgets, saveData, clearEntries, showMessage
from .settingsTab import settingsTabWidget, setTheme_func, setAppearanceMode_func
from .savedTab import savedTabWidgets, addDataList, deleteEntry
from .aboutTab import aboutTabWidgets
# from utils.keyBindings import generateTabBinding

class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add('Generate')
        self.add('Login')
        self.add('Saved')
        self.add('Settings')
        self.add('About')

        generateTabWidgets(self, master=self.tab('Generate'))
        loginTabWidgets(self, master=self.tab('Login'))
        savedTabWidgets(self, master=self.tab('Saved'))
        settingsTabWidget(self, master=self.tab('Settings'))
        aboutTabWidgets(self, master=self.tab('About'))        
        # generateTabBinding(self.tab('Generate'))
    

    def charSliderEvent(self, *args): charSliderEvent(self, *args)
    
    def genPass_func(self,): genPass_func(self)

    def advanchedOption_func(self): advanchedOption_func(self)

    def copyPass_func(self): copyPass_func(self)
    
    def clearStatus_func(self): clearStatus_func(self)
    
    def passwordStrengthEvent(self, *args): passwordStrengthEvent(self, *args)
    
    def setTheme_func(self, *args): setTheme_func(self, *args)

    def setAppearanceMode_func(self, *args): setAppearanceMode_func(self, *args)

    def saveData(self): saveData(self)

    def clearEntries(self): clearEntries(self)

    def showMessage(self): showMessage(self)

    def addDataList(self): addDataList(self)

    def deleteEntry(self): deleteEntry(self)


    # def savedTabWidgets(self, master):
    #     self.savedTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    #     self.savedTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    #     self.savedHeading = ctk.CTkLabel(self.savedTabFrame, text='Hello SavedTab', font=default_font)
    #     self.savedHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    # def aboutTabWidgets(self, master):
    #     self.aboutTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    #     self.aboutTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    #     self.aboutHeading = ctk.CTkLabel(self.aboutTabFrame, text='Hello AboutTab', font=default_font)
    #     self.aboutHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    # def settingsTabWidgets(self, master):
    #     self.settingsTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    #     self.settingsTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    #     self.settingsHeading = ctk.CTkLabel(self.settingsTabFrame, text='Hello SettingsTab', font=default_font)
    #     self.settingsHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')
