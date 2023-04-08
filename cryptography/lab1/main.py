class CAESAR(object):
    def __init__(self, key:int, alpha:str='EN'):
        if alpha == 'EN':
            self.ABC = ' abcdefghijklmnopqrstuvwxyz'
        else:
            self.ABC = ' абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
        
        if key <= 0 or key >= len(self.ABC):
            raise ValueError('key must be greater than 0 and less than ABC length')
        
        self.__k:int = key
        self.n = len(self.ABC)

    def enc(self, text:str) -> str:
        res = ''
        for x in text.lower():
            res += self.ABC[(self.ABC.index(x) + self.__k) % self.n]
        return res

    def dec(self, text:str) -> str:
        res = ''
        for y in text.lower():
            res += self.ABC[(self.ABC.index(y) + self.n - (self.__k % self.n)) % self.n]
        return res

    def __str__(self) -> str:
        return "Dev: Prytula M.I. 124m-22-1"


def main():
    cipher = CAESAR(key=3, alpha="EN")
    print(cipher.enc("abc"))
    print(cipher.dec(cipher.enc("abc")))
    print(cipher)


if __name__ == "__main__":
    main()