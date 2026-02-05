import customtkinter as ctk
from themes.themes import default_font, PADXY, titles_font

def loginTabWidgets(self, master):
    self.loginTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.loginTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.titleLabel = ctk.CTkLabel(self.loginTabFrame, text='Title:     ', font=titles_font)
    self.titleLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.titleEntry = ctk.CTkEntry(self.loginTabFrame, width=380, height=40, font=default_font, placeholder_text='Untitled')
    self.titleEntry.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.titleEntry.bind("<KeyRelease>", lambda _: otherEntriesOnClick(self))
    # self.titleEntry.insert('end', 'Untitled')


    self.detailsFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.detailsFrame.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.usernameOrEmailLabel = ctk.CTkLabel(self.detailsFrame, text='Username or email:', font=default_font)
    self.usernameOrEmailLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.usernameOrEmailEntry = ctk.CTkEntry(self.detailsFrame, width=315, height=30, font=default_font, placeholder_text='Add username or email address')
    self.usernameOrEmailEntry.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.usernameOrEmailEntry.bind("<KeyRelease>", lambda _: otherEntriesOnClick(self))

    self.passwordLabel = ctk.CTkLabel(self.detailsFrame, text='Password:         ', font=default_font)
    self.passwordLabel.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.passwordEntry = ctk.CTkEntry(self.detailsFrame, width=315, height=30, font=default_font, show=None, placeholder_text='Add password',)
    self.passwordEntry.grid(row=1, column=1, padx=PADXY, pady=PADXY)
    self.passwordEntry.bind("<KeyRelease>", lambda _: showPassword(self))

    self.twoFASecretKeyLabel = ctk.CTkLabel(self.detailsFrame, text='2FA secret key:   ', font=default_font)
    self.twoFASecretKeyLabel.grid(row=2, column=0, padx=PADXY, pady=PADXY)

    self.twoFASecretKeyEntry = ctk.CTkEntry(self.detailsFrame, width=315, height=30, font=default_font, placeholder_text='Add 2FA secret key')
    self.twoFASecretKeyEntry.grid(row=2, column=1, padx=PADXY, pady=PADXY)
    self.twoFASecretKeyEntry.bind("<KeyRelease>", lambda _: otherEntriesOnClick(self))



    self.websiteFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.websiteFrame.grid(row=2, column=0, padx=PADXY, pady=PADXY)

    self.websiteLabel = ctk.CTkLabel(self.websiteFrame, text='Website:                ', font=default_font,)
    self.websiteLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.websiteEntry = ctk.CTkEntry(self.websiteFrame, width=315, height=30, font=default_font, placeholder_text='https://')
    self.websiteEntry.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.websiteEntry.bind("<KeyRelease>", lambda _: otherEntriesOnClick(self))



    self.noteFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.noteFrame.grid(row=3, column=0, padx=PADXY, pady=PADXY)

    self.noteLabel = ctk.CTkLabel(self.noteFrame, text='Note:                     ', font=default_font)
    self.noteLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.noteEntry = ctk.CTkEntry(self.noteFrame, width=315, height=40, font=default_font, placeholder_text='Add note')
    self.noteEntry.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.noteEntry.bind("<KeyRelease>", lambda _: otherEntriesOnClick(self))


    self.createButton = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.createButton.grid(row=4, column=0, padx=PADXY, pady=PADXY)

    self.createButton = ctk.CTkButton(self.createButton, text='Create', command=None, font=default_font)
    self.createButton.grid(row=0, column=0, padx=PADXY, pady=PADXY)

def hidePassword(self):
    self.passwordEntry.configure(show='*')

def showPassword(self):
    self.passwordEntry.configure(show='')

def otherEntriesOnClick(self):
    hidePassword(self)
