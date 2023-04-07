# Цей код демонструє використання п'яти режимів DES: ECB, CBC, CFB, OFB та CTR. 
# Для кожного режиму створені окремі функції шифрування та дешифрування, 
# які використовують бібліотеку pycryptodomex. Повідомлення шифрується та дешифрується 
# за допомогою різних режимів та результати виводяться на екран.

from Cryptodome.Cipher import DES
from Cryptodome.Util.Padding import pad, unpad
import base64
import os

def des_encrypt_ecb(key, plaintext):
    """Шифрує повідомлення за допомогою DES у режимі ECB"""
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode()

def des_decrypt_ecb(key, ciphertext):
    """Дешифрує шифртекст за допомогою DES у режимі ECB"""
    cipher = DES.new(key, DES.MODE_ECB)
    decoded_ciphertext = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(decoded_ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size)
    return plaintext.decode()

def des_encrypt_cbc(key, iv, plaintext):
    """Шифрує повідомлення за допомогою DES у режимі CBC"""
    cipher = DES.new(key, DES.MODE_CBC, iv)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(ciphertext).decode()

def des_decrypt_cbc(key, iv, ciphertext):
    """Дешифрує шифртекст за допомогою DES у режимі CBC"""
    cipher = DES.new(key, DES.MODE_CBC, iv)
    decoded_ciphertext = base64.b64decode(ciphertext)
    padded_plaintext = cipher.decrypt(decoded_ciphertext)
    plaintext = unpad(padded_plaintext, DES.block_size)
    return plaintext.decode()

def des_encrypt_cfb(key, iv, plaintext):
    """Шифрує повідомлення за допомогою DES у режимі CFB"""
    cipher = DES.new(key, DES.MODE_CFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def des_decrypt_cfb(key, iv, ciphertext):
    """Дешифрує шифртекст за допомогою DES у режимі CFB"""
    cipher = DES.new(key, DES.MODE_CFB, iv)
    decoded_ciphertext = base64.b64decode(ciphertext)
    plaintext = cipher.decrypt(decoded_ciphertext)
    return plaintext.decode()

def des_encrypt_ofb(key, iv, plaintext):
    """Шифрує повідомлення за допомогою DES у режимі OFB"""
    cipher = DES.new(key, DES.MODE_OFB, iv)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def des_decrypt_ofb(key, iv, ciphertext):
    """Дешифрує шифртекст за допомогою DES у режимі OFB"""
    cipher = DES.new(key, DES.MODE_OFB, iv)
    decoded_ciphertext = base64.b64decode(ciphertext)
    plaintext = cipher.decrypt(decoded_ciphertext)
    return plaintext.decode()

def des_encrypt_ctr(key, nonce, plaintext):
    """Шифрує повідомлення за допомогою DES у режимі CTR"""
    cipher = DES.new(key, DES.MODE_CTR, nonce=nonce)
    ciphertext = cipher.encrypt(plaintext.encode())
    return base64.b64encode(ciphertext).decode()

def des_decrypt_ctr(key, nonce, ciphertext):
    """Дешифрує шифртекст за допомогою DES у режимі CTR"""
    cipher = DES.new(key, DES.MODE_CTR, nonce=nonce)
    decoded_ciphertext = base64.b64decode(ciphertext)
    plaintext = cipher.decrypt(decoded_ciphertext)
    return plaintext.decode()

#key = b"my_secret_key"
key = os.urandom(8)
iv = os.urandom(8)
nonce = b"nonce"
plaintext = "Hello, world!"

print("ECB mode:")
encrypted_text = des_encrypt_ecb(key, plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = des_decrypt_ecb(key, encrypted_text)
print("Decrypted text:", decrypted_text)

print("CBC mode:")
encrypted_text = des_encrypt_cbc(key, iv, plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = des_decrypt_cbc(key, iv, encrypted_text)
print("Decrypted text:", decrypted_text)

print("CFB mode:")
encrypted_text = des_encrypt_cfb(key, iv, plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = des_decrypt_cfb(key, iv, encrypted_text)
print("Decrypted text:", decrypted_text)

print("OFB mode:")
encrypted_text = des_encrypt_ofb(key, iv, plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = des_decrypt_ofb(key, iv, encrypted_text)
print("Decrypted text:", decrypted_text)

print("CTR mode:")
encrypted_text = des_encrypt_ctr(key, nonce, plaintext)
print("Encrypted text:", encrypted_text)
decrypted_text = des_decrypt_ctr(key, nonce, encrypted_text)
print("Decrypted text:", decrypted_text)