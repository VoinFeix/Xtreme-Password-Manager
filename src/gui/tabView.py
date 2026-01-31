import customtkinter as ctk
from themes.themes import default_font

class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add('Generate')
        self.add('Check')
        self.add('Saved')
        self.add('About')
        self.add('Settings')

        self.generateTabWidgets(self.tab('Generate'))
        self.checkTabWidgets(self.tab('Check'))
        self.savedTabWidgets(self.tab('Saved'))
        self.aboutTabWidgets(self.tab('About'))
        self.settingsTabWidgets(self.tab('Settings'))

    def generateTabWidgets(self, master):
        self.generateTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.generateTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.label0 = ctk.CTkLabel(self.generateTabFrame, text='-: Generate :-', font=default_font)
        self.label0.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

    def checkTabWidgets(self, master):
        self.checkTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
        self.checkTabFrame.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

        self.checkHeading = ctk.CTkLabel(self.checkTabFrame, text='Hello CheckTab', font=default_font)
        self.checkHeading.grid(row=0, column=0, padx=20, pady=20, sticky='ew')

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
