import customtkinter as ctk
from themes.themes import default_font, PADXY, savedTabListBoxFont
from gui.loginTab import sc
from gui.popUpUi import ShowLogins
from CTkListbox import CTkListbox

def savedTabWidgets(self, master):
    self.savedTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.savedTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.savedListBox = CTkListbox(master, height=400, width=500, font=savedTabListBoxFont, command=plotData)
    self.savedListBox.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    addDataList(self)

def addDataList(self):

    self.savedListBox.delete(0, 'end')
    data = sc.get().keys()
    for idx, title in enumerate(data, start=0):
        self.savedListBox.insert(str(idx), title)
    return 

def plotData(*args):
    data = sc.get()
    data=data[args[0]]
    print(data)
    ShowLogins().show(data=data)