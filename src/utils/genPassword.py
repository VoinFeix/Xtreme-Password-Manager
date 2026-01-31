import secrets
import string

# print(string.__all__)
# print('a',string.ascii_letters)
# print('b',string.ascii_lowercase)
# print('c',string.ascii_uppercase)
# print('d',string.capwords)
# print('e',string.digits)
# print('f',string.hexdigits)
# print('g',string.octdigits)
# print('h',string.printable)
# print('i',string.punctuation)
# print('j',string.whitespace)
# print('k',string.Formatter)
# print('l',string.Template)

# print(''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(64)))

def genPassword(self, length: int, specialChars=None, captialLetters=None, includeNumbers=None) -> str:
    words = string.ascii_lowercase
    special = string.punctuation if specialChars else ''
    capital = string.ascii_uppercase if captialLetters else ''
    numbers = string.digits if includeNumbers else ''

    rand = words + special + capital + numbers
    result = ''.join(secrets.choice(rand) for _ in range(length))
    return result
