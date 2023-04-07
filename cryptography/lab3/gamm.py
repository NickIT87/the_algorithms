import secrets

def generate_key(length):
    """Генерує ключ заданої довжини"""
    key = ""
    for i in range(length):
        key += str(secrets.randbelow(2))
    return key

def encrypt(message, key):
    """Шифрує повідомлення за допомогою шифру гамування"""
    cipher = ""
    for i in range(len(message)):
        # Об'єднуємо кожен символ повідомлення з відповідним символом з ключа
        # за допомогою операції XOR та переводимо отриманий біт в символ ASCII
        cipher += chr(ord(message[i]) ^ ord(key[i % len(key)]))
    return cipher

def decrypt(cipher, key):
    """Дешифрує шифртекст за допомогою шифру гамування"""
    message = ""
    for i in range(len(cipher)):
        # Об'єднуємо кожен символ шифртексту з відповідним символом з ключа
        # за допомогою операції XOR та переводимо отриманий біт в символ ASCII
        message += chr(ord(cipher[i]) ^ ord(key[i % len(key)]))
    return message

# Приклад використання
message = "Hello, world!"
key = generate_key(len(message))
print("Повідомлення:", message)
print("Ключ:", key)
cipher = encrypt(message, key)
print("Шифртекст:", cipher)
decrypted_message = decrypt(cipher, key)
print("Дешифроване повідомлення:", decrypted_message)
