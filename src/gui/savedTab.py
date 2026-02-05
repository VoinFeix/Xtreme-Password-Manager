import customtkinter as ctk
from themes.themes import default_font, PADXY, savedTabListBoxFont
from CTkListbox import CTkListbox

def savedTabWidgets(self, master):
    self.savedTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.savedTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.savedListBox = CTkListbox(master, height=400, width=500, font=savedTabListBoxFont, command=testCmd)
    self.savedListBox.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    for i in range(20):
        self.savedListBox.insert(str(i), str(i))


def testCmd(*args, **kwargs):
    print('Commaned Executed')
    print(*args)
    print(*kwargs)