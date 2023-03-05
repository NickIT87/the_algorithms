class Cipher(object):
    def __init__(self, key:int, alpha:str='EN'):
        if alpha == 'EN':
            self.ABC = ' abcdefghijklmnopqrstuvwxyz'
        else:
            self.ABC = ' абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        
        if type(key) != int or key <= 0 or key >= len(self.ABC):
            raise ValueError('key must be Integer, greater than 0 and less than ABC length!')
        
        self.k:int = key
        self.n = len(self.ABC)

    def __str__(self) -> str:
        return "Dev: Prytula M.I. 124m-22-1"

class CAESAR(Cipher):
    def __init__(self, key: int, alpha: str = 'EN'):
        super().__init__(key, alpha)

    def enc(self, text:str) -> str:
        res = ''
        for x in text.lower():
            res += self.ABC[(self.ABC.index(x) + self.k) % self.n]
        return res

    def dec(self, text:str) -> str:
        res = ''
        for y in text.lower():
            res += self.ABC[(self.ABC.index(y) + self.n - (self.k % self.n)) % self.n]
        return res


class TRITEMIUS(Cipher):
    def __init__(self, key: int, alpha: str = 'EN'):
            super().__init__(key, alpha)

    def enc(self, text:str) -> str:
        ciphertext = ""
        key = self.k % len(self.ABC)
        for char in text.lower():
            if char in self.ABC:
                idx = (self.ABC.index(char) + key) % len(self.ABC)
                ciphertext += self.ABC[idx]
            else:
                ciphertext += char
        return ciphertext

    def dec(self, text:str) -> str:
        plaintext = ""
        key = self.k % len(self.ABC)
        for char in text.lower():
            if char in self.ABC:
                idx = (self.ABC.index(char) - key) % len(self.ABC)
                plaintext += self.ABC[idx]
            else:
                plaintext += char
        return plaintext