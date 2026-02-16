
# XPM: Xtreme Password Manager
XPM: Xtreme Password Manager is a lightweight, secured, encrypted, and easy to use password manager build for linux based systems.

---

## Features
- Generate fully random passwords up to 64 characters.
- Create a login and save your details securely.
- Access saved logins with a easy UI.
- User can delete unused login very easily with one button.
- Switch between themes easily with one click.
- Supports multiple themes
- Light weight setup and easy on cpu.
- Overall ui is easy to use and begineer friendly.
- Fully offline mode.
- Your data never leaves your computer.


## Project Structure
```
XPM/
│
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
│
├── ScreenShots/                # Contains all the screenshots of the project
│
└── src/
   ├── core/
   │   └── main.py              # Main file that launches the project 
   │
   ├── gui/
   │   ├── aboutTab.py          # Gui elements for About Tab
   │   ├── generateTab          # Gui elements for Generate Tab
   │   ├── heading.py           # Gui elements for the headings
   │   ├── loginTab.py          # Gui elements for Login Tab
   │   ├── popUpUi.py           # Gui elements for Pop Up
   │   ├── savedTab.py          # Gui elements for Saved Tab
   │   ├── settingsTab.py       # Gui elements for Settings Tab
   │   └── tabView.py           # Main Tab View
   │
   ├── themes/
   │   ├── themes.py            # All Neccesary variables and information
   │   └── *.json               # All json themes files       
   │
   └── utils/
      ├── copyPassword.py       # Function for Copying Password
      ├── saveCreds.py          # Contains the code for storing user credentials securely
      ├── genPassword.py        # Function for generating the random password
      └── keyBindings.py        # Function containing all keybinds for the program
      

```

## ScreenShots and Demo
- All Screenshots below have the default theme, but user can change it to their favourite theme.

1. Generate Password Tab

<img alt="generate_password" src="/ScreenShots/genPass.png" />

2. Create Login Tab
<img alt="login_password" src="/ScreenShots/loginPass.png" />

3. Saved Logins
<img alt="saved_logins" src="/ScreenShots/savedLogins.png" />

4. Settings Tab
<img alt="settings" src="/ScreenShots/settings.png" />

5. About Tab
<img alt="about" src="/ScreenShots/about.png" />

### Demo
[![Watch the video](/Demos/xpm.mp4)]


## Requirements
- Python 3.8+
- Some Pip Packages

## Installation
1. AppImage
    - Under Development :)

2. Source Code
    - Clone The Repository
    ```bash
    git clone https://github.com/VoinFeix/Xtreme-Password-Manager.git
    cd Xtreme-Password-Manager
    ```

    - Create An Virtual Env (Recommended)
    ```bash
    python3 -m venv venv/
    source venv/bin/activate
    ```

    - Install The Requirements
    ```bash
    pip install -r requirements.txt
    ```

    - Run The Application
    ```bash
    python3 src/core/main.py
    ```

---

## Licence
Check out LICENCE file for more information

---


**-** **Made with ❤️**



