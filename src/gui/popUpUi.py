import customtkinter as ctk
from themes.themes import default_font, PADXY, titles_font, showInfo_font, timerLabelColors, showTimer_font
from utils.copyPassword import copyPassword

class ShowLogins(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Saved Logins")
        self.geometry('650x600')
        self.resizable(False, False)

        self.label0 = ctk.CTkLabel(self, text='Saved Logins', font=titles_font)
        self.label0.pack(padx=PADXY, pady=PADXY)

        self.textbox = ctk.CTkTextbox(self, width=600, height=350, font=showInfo_font)
        self.textbox.pack(padx=PADXY, pady=PADXY)
        self.textbox.configure(state='disabled')

        self.timerLabel = ctk.CTkLabel(self, text='', font=showTimer_font)
        self.timerLabel.pack(padx=PADXY, pady=PADXY)

        self.copyBtn = ctk.CTkButton(self, text='Copy', command=self.copyPassword, font=default_font)
        self.copyBtn.pack(padx=PADXY, pady=PADXY)
        
        self.closeBtn = ctk.CTkButton(self, text='Close', command=self.closePopUp, font=default_font)
        self.closeBtn.pack(padx=PADXY, pady=PADXY)

        curSec = 60
        self.showtimer(curSec)
    
    def show(self, data: dict) -> None:
        self.title = data['Title']
        self.usernameOremail = data['UsernameOrEmail']
        self.password = data['Password']
        self.twoFASecretKey = data['2FASecretKey']
        self.website = data['Website']
        self.note = data['Note']
        self.isUsername = False if "@" in self.usernameOremail else True

        self.result = f"""
{"="*33}

Title:   {self.title}
{"Username: " if self.isUsername else "Email: "}  {self.usernameOremail if self.usernameOremail else 'N/A'}
Password:   {self.password if self.password else 'N/A'}
2FA Secret Key:   {self.twoFASecretKey if self.twoFASecretKey else 'N/A'}
Website:   {self.website if self.website else 'N/A'}
Note:   {self.note if self.note else 'N/A'}

{"="*33}
        
        """
        self.textbox.configure(state='normal')
        self.textbox.insert("0.0", self.result.strip())
        self.textbox.configure(state='disabled')

    def copyPassword(self) -> None:
        copyPassword(self, self.password)

    def closePopUp(self) -> None:
        self.destroy()

    def showtimer(self, curSec:int) -> None:
        if curSec == 0:
            self.closePopUp()
            return

        text_color = None
       
        if 20 <= curSec or curSec <= 40: text_color=timerLabelColors['Middle']
        if curSec > 40: text_color=timerLabelColors['High']
        if curSec <=10: text_color=timerLabelColors['Low']

        self.timerLabel.configure(text=f'Closing in {curSec} seconds.', text_color=text_color)
        self.after(1000, lambda : self.showtimer(curSec-1))

