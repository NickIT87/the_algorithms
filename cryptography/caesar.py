EN = ' abcdefghijklmnopqrstuvwxyz'
UA = ' абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'

# y = (x + k) mod n
# x = (y + n - (k mod n)) mod n

# x - символ відкритого тексту, 
# y - символ шифрованого тексту, 
# n - потужність алфавіту, 
# k - ключ.

def caesar(text:str, k:int, ABC:str, dec:int=0) -> str:
    res: str = ""
    text = text.lower()
    k = abs(k)
    n = len(ABC)

    if dec:
        for y in text:
            res += ABC[(ABC.index(y) + n - (k % n)) % n]
    else:
        for x in text:
            res += ABC[(ABC.index(x) + k) % n]

    return res

key = 12 #int(input())
user_text = "abc" #input().strip()

print(caesar(user_text, key, EN))
print(caesar(caesar(user_text, key, EN), key, EN, 1))


# res = ''
# for c in user_text:
#     res += EN[(EN.index(c) + key) % len(EN)]
# print('Result: "' + res + '"')

# dcp = ''
# for i in res:
#     dcp += EN[(EN.index(i) + len(EN) - (key % len(EN))) % len(EN)]

# print(dcp)