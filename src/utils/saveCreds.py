import json
from cryptography.fernet import Fernet
import getpass

class SaveCredentials:
    def __init__(self, file_path, key):
        self.file_path = file_path
        self.cipher = Fernet(key)
        self.data: dict = self._load()

    def _load(self) -> dict:
        try:
            with open(self.file_path, 'rb') as f:
                encrypted = f.read()
                decrypted = self.cipher.decrypt(encrypted)
                return json.loads(decrypted)
        except FileNotFoundError: return {}

    def _save(self) -> None:
        encrypted = self.cipher.encrypt(json.dumps(self.data).encode())
        try:
            with open(self.file_path, 'wb') as f:
                f.write(encrypted)
        except FileNotFoundError: return None

    def add(self, data:dict) -> None:
        self.data[data['Title']] = data
        self._save()

    def get(self) -> dict: return self.data

    def delete(self, title) -> None:
        try:
            self.data.pop(title)
            self._save()
        except KeyError: return None

def addData(title=None, usernameOremail=None, password=None, twoFASecretKey=None, website=None, note=None) -> dict:
    data = {
        'Title': title,
        'UsernameOrEmail': usernameOremail,
        'Password': password,
        '2FASecretKey': twoFASecretKey,
        'Website': website,
        'Note': note,
    }
    return data

def init():
    user = getpass.getuser()
    key_file_dir = f'/home/{user}/.config/XPM/Configs/Default/'
    filepath_dir = f'/home/{user}/.config/XPM/Configs/Default/'
    key_filename = f'/home/{user}/.config/XPM/Configs/Default/.key.key'
    filepath = f'/home/{user}/.config/XPM/Configs/Default/.creds.enc'
    import os
    try:
        if not os.path.isfile(key_filename):
            os.makedirs(key_file_dir, exist_ok=True)
            passkey = Fernet.generate_key()
            with open(key_filename, 'wb') as f:
                f.write(passkey)

        with open(key_filename, 'rb') as f:
            key = f.read()
        
        return filepath, key
    except Exception as e: print('Error at init function in saveCreds: ', str(e))



# filepath, key = init()
# sc = SaveCredentials(filepath, key)

# # print(sc.get().keys())

# print(sc.get()['One Fake One'])