import pyperclip

def copyPassword(self, randPass:str) -> None:
    try:
        pyperclip.copy(text=randPass)
    except Exception as e:
        print(f'Error Copying the Password\n{e}')
