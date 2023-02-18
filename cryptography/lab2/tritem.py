# Функція для шифрування тексту за допомогою шифру Тритеміуса
def trithemius_cipher_encrypt(plaintext, key_word):
    encrypted_text = ''
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Знаходимо позицію ключового слова в алфавіті та додаємо до неї позицію поточної літери у тексті
            shift = ord(key_word[key_index].lower()) - 97 + ord(char.lower()) - 97
            
            # Якщо позиція перевищує кількість літер в алфавіті, то знову починаємо з початку алфавіту
            if shift >= 26:
                shift -= 26
            
            # Додаємо зашифровану літеру до вихідного тексту
            encrypted_text += chr(shift + 97).upper() if char.isupper() else chr(shift + 97)
            
            # Збільшуємо індекс ключового слова
            key_index = (key_index + 1) % len(key_word)
        else:
            encrypted_text += char
    
    return encrypted_text

# Функція для дешифрування тексту за допомогою шифру Тритеміуса
def trithemius_cipher_decrypt(ciphertext, key_word):
    decrypted_text = ''
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Знаходимо позицію ключового слова в алфавіті та віднімаємо від неї позицію зашифрованої літери у тексті
            shift = ord(key_word[key_index].lower()) - 97 - (ord(char.lower()) - 97)
            
            # Якщо позиція менша за 0, то знову починаємо з кінця алфавіту
            if shift < 0:
                shift += 26
            
            # Додаємо розшифровану лі
