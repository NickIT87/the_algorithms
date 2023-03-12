def vigenere_cipher(message, key, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key *= len(message) // len(key) + 1
    result = ""
    for i in range(len(message)):
        if message[i].lower() not in alphabet:
            result += message[i]
        else:
            key_letter = key[i]
            if mode == "decrypt":
                key_letter = alphabet[(26 - alphabet.index(key_letter.lower())) % 26]
            message_letter = message[i]
            shift = alphabet.index(key_letter.lower())
            if message_letter.isupper():
                result += alphabet[(alphabet.index(message_letter.lower()) + shift) % 26].upper()
            else:
                result += alphabet[(alphabet.index(message_letter.lower()) + shift) % 26]
    return result


message = "This is a secret message."
key = "secret"
encrypted_message = vigenere_cipher(message, key, "encrypt")
decrypted_message = vigenere_cipher(encrypted_message, key, "decrypt")
print(encrypted_message)
print(decrypted_message)


def vigenere_enc(message, key):
    # Повторюємо ключове слово декілька разів, щоб отримати ключ довжиною, що не менше за довжину повідомлення
    key = key * (len(message) // len(key) + 1)

    # Шифруємо повідомлення за допомогою шифру Віженера
    encrypted_message = ""
    for i in range(len(message)):
        char = message[i]
        key_char = key[i]
        # Застосовуємо операцію шифрування Цезаря до кожного символу повідомлення з відповідним символом ключа
        encrypted_char = chr((ord(char) + ord(key_char)) % 256)
        encrypted_message += encrypted_char

    return encrypted_message


def vigenere_dec(encrypted_message, key):
    # Повторюємо ключове слово декілька разів, щоб отримати ключ довжиною, що не менше за довжину зашифрованого повідомлення
    key = key * (len(encrypted_message) // len(key) + 1)

    # Розшифровуємо повідомлення за допомогою шифру Віженера
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        char = encrypted_message[i]
        key_char = key[i]
        # Застосовуємо операцію дешифрування Цезаря до кожного символу зашифрованого повідомлення з відповідним символом ключа
        decrypted_char = chr((ord(char) - ord(key_char)) % 256)
        decrypted_message += decrypted_char

    return decrypted_message


message = "This is a secret message."
key = "secret"
enc_message = vigenere_enc(message, key)
a = list(enc_message)
dec_message = vigenere_dec(enc_message, key)
print(enc_message)
print(dec_message)