import customtkinter as ctk
from themes.themes import default_font, PADXY, titles_font

def aboutTabWidgets(self, master):
    self.aboutTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.aboutTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    about: str = f"""{"="*22}

XPM: Xtreme Password Manager
- It is a lightweight, free, open source password manager for linux based systems.
- It is user friendly, ease to use and good looking.
- All logins are saved encrypted.
- Offline Usage Support.
- Feel free to use it.

Source -> https://github.com/VoinFeix/Xtreme-Password-Manager/

'Privacy is a human right, And everyone should care about it'   - A Wise Man

Made with pure ❤️.
{"="*22}
    """

    self.textBox = ctk.CTkTextbox(self.aboutTabFrame, width=500, height=400, font=titles_font)
    self.textBox.grid(row=0, column=0, padx=PADXY, pady=PADXY)
    self.textBox.insert('0.0', about)
    self.textBox.configure(state='disabled')
