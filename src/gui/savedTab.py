import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from themes.themes import default_font, PADXY, savedTabListBoxFont
from gui.loginTab import sc, showMessage
from gui.popUpUi import ShowLogins
from CTkListbox import CTkListbox

def savedTabWidgets(self, master):
    self.savedTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.savedTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.savedListBox = CTkListbox(master, height=350, width=500, font=savedTabListBoxFont, command=plotData)
    self.savedListBox.grid(row=0, column=0, padx=PADXY, pady=PADXY)
    
    self.deleteEntryFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.deleteEntryFrame.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.deleteEntryBtn = ctk.CTkButton(self.deleteEntryFrame, text='Delete', command=self.deleteEntry, font=default_font)
    self.deleteEntryBtn.grid(row=0, column=0, padx=PADXY, pady=PADXY)

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
    ShowLogins().show(data=data)

def deleteEntry(self):
    titleIdx = self.savedListBox.curselection()
    title = list(sc.get().keys())[titleIdx]

    choice = CTkMessagebox(self.savedTabFrame, message=f"Do you want to delete '{title}'\nYou can't restore it after deleted!!", icon='question', option_1='Yes', option_2='No')
    
    if choice.get() == 'Yes':        
        sc.delete(title=title)
        showMessage(self, msgtype='info', message=f"{title} deleted sucessfully")
        self.addDataList()
    else:
        return