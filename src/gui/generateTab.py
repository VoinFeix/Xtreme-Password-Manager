import customtkinter as ctk
from themes.themes import default_font
from utils.genPassword import genPassword
from utils.copyPassword import copyPassword
# from utils.keyBindings import generateTabBinding
PADXY = 12


def generateTabWidgets(self, master):
    self.generateTabFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.generateTabFrame.grid(row=0, column=0, padx=PADXY, pady=PADXY, sticky='ew')

    # self.generateTabFrame.columnconfigure(0, weight=1)
    # self.generateTabFrame.rowconfigure(0, weight=1)
    


    # ctk.CTkLabel(self.generateTabFrame, text='').grid(row=0, column=1, padx=50, pady=PADXY)
    # ctk.CTkLabel(self.generateTabFrame, text='').grid(row=0, column=2, padx=50, pady=PADXY)
    # ctk.CTkLabel(self.generateTabFrame, text='').grid(row=0, column=3, padx=50, pady=PADXY)
    # ctk.CTkLabel(self.generateTabFrame, text='').grid(row=0, column=4, padx=50, pady=PADXY)
    self.minCharNum = 4
    self.maxCharNum = 64
    self.currentCharValue = None
    # self.numOfSteps = 1

    self.charSliderLabel = ctk.CTkLabel(self.generateTabFrame, text=f'{self.minCharNum} Characters            ', font=default_font)
    self.charSliderLabel.grid(row=0, column=0, padx=PADXY, pady=PADXY)

    self.charSlider = ctk.CTkSlider(self.generateTabFrame, from_=self.minCharNum, to=self.maxCharNum, command=self.charSliderEvent)
    self.charSlider.grid(row=0, column=1, padx=PADXY, pady=PADXY)
    self.charSlider.set(0)

    self.specialChars_check_value = ctk.BooleanVar()
    self.specialCharsCheckBox = ctk.CTkCheckBox(self.generateTabFrame, text='Special characters (!&%)', variable=self.specialChars_check_value, command=None, font=default_font)
    self.specialCharsCheckBox.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.advanchedOptions_check_value = ctk.BooleanVar()
    self.advanchedOptionCheckBox = ctk.CTkCheckBox(self.generateTabFrame, text='Advanched options        ', variable=self.advanchedOptions_check_value, command=self.advanchedOption_func, font=default_font)
    self.advanchedOptionCheckBox.grid(row=2, column=0, padx=PADXY, pady=PADXY)
    
    # self.passwordResult = ctk.CTkLabel(self.generateTabFrame, text='Result:', font=default_font)
    # self.passwordResult.grid(row=5, column=0, padx=PADXY, pady=PADXY)
    
    
    self.resultPassFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.resultPassFrame.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.passwordResultTextBox = ctk.CTkTextbox(self.resultPassFrame, width=450, height=50, font=default_font)
    self.passwordResultTextBox.grid(row=0, column=0, padx=PADXY, pady=PADXY)
    self.passwordResultTextBox.configure(state='disabled')

    self.copyStatusLabel = ctk.CTkLabel(self.resultPassFrame, text='', font=default_font)
    self.copyStatusLabel.grid(row=1, column=0, padx=PADXY, pady=PADXY)
    
    

    self.genBtnsFrame = ctk.CTkFrame(master, border_color='black', border_width=3)
    self.genBtnsFrame.grid(row=2, column=0, padx=PADXY, pady=PADXY)

    self.generateBtn = ctk.CTkButton(self.genBtnsFrame, text='Generate', command=self.genPass_func, font=default_font)
    self.generateBtn.grid(row=1, column=0, padx=PADXY, pady=PADXY)

    self.copyBtn = ctk.CTkButton(self.genBtnsFrame, text='Copy', command=self.copyPass_func, font=default_font)
    self.copyBtn.grid(row=1, column=1, padx=PADXY, pady=PADXY)

    # generateTabBinding(self.tab('Generate'))
    


def testSliderEvent(event):
    print(f"Slider Value: {event}")

def charSliderEvent(self, event):
    # testSliderEvent(event)

    currentCharValue = int(self.charSlider.get())
    charSliderLabelText = f'{currentCharValue} Characters'
    self.charSliderLabel.configure(text=charSliderLabelText)

def advanchedOption_func(self):
    try:
        if not self.advanchedOptions_check_value.get():
            self.capitalLettersCheckBox.destroy()
            self.includeNumbersCheckBox.destroy()
            return
    except Exception as e:
        print(f'Error On AdvanchedOption_func\n{e}')
    
    self.capitalLetters_check_value = ctk.BooleanVar()
    self.capitalLettersCheckBox = ctk.CTkCheckBox(self.generateTabFrame, text='Capital letters (A-Z)       ', variable=self.capitalLetters_check_value, command=None, font=default_font)
    self.capitalLettersCheckBox.grid(row=3, column=0, padx=PADXY, pady=PADXY)

    self.includeNumbers_check_value = ctk.BooleanVar()
    self.includeNumbersCheckBox = ctk.CTkCheckBox(self.generateTabFrame, text='Include numbers (0-9)   ', variable=self.includeNumbers_check_value, command=None, font=default_font)
    self.includeNumbersCheckBox.grid(row=4, column=0, padx=PADXY, pady=PADXY)

def genPass_func(self):
    length = 0
    specialChars = None
    captialLetters = None
    includeNumbers = None
    
    length = int(self.charSlider.get())
    specialChars = True if self.specialChars_check_value.get() else False
    try:
        captialLetters = True if self.capitalLetters_check_value.get() else False
        includeNumbers = True if self.includeNumbers_check_value.get() else False
    except Exception as e:
        print(f'Error on genPass_func\n{e}')
        captialLetters = False
        includeNumbers = False

    
    randomPassword: str = genPassword(self, length=length, specialChars=specialChars, captialLetters=captialLetters, includeNumbers=includeNumbers)
    self.passwordResultTextBox.configure(state='normal')
    self.passwordResultTextBox.delete('0.0', 'end')
    # output = f'Result: {randomPassword}'
    self.passwordResultTextBox.insert('end', randomPassword)
    self.passwordResultTextBox.configure(state='disabled')

def clearCopyStatus_func(self):
    self.copyStatusLabel.configure(text='')

def copyPass_func(self):
    randomPass = self.passwordResultTextBox.get('0.0', 'end') if self.passwordResultTextBox.get('0.0', 'end') else ''
    copyPassword(self, randomPass)
    self.copyStatusLabel.configure(text='Status: Password Copied!!')
    self.after(5000, self.clearCopyStatus_func)

