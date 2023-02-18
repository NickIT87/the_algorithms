def tritemius_cipher(plaintext, key):
    """
    Encrypts plaintext using the Tritemius cipher with the given key.
    The key is an integer indicating the shift value for the first letter of the alphabet.
    """
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key % len(alphabet)  # make sure key is within range of alphabet size
    for char in plaintext.lower():
        if char in alphabet:
            idx = (alphabet.index(char) + key) % len(alphabet)
            ciphertext += alphabet[idx]
        else:
            ciphertext += char
    return ciphertext

def tritemius_decipher(ciphertext, key):
    """
    Decrypts ciphertext using the Tritemius cipher with the given key.
    The key is an integer indicating the shift value for the first letter of the alphabet.
    """
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key = key % len(alphabet)  # make sure key is within range of alphabet size
    for char in ciphertext.lower():
        if char in alphabet:
            idx = (alphabet.index(char) - key) % len(alphabet)
            plaintext += alphabet[idx]
        else:
            plaintext += char
    return plaintext


plaintext = "the quick brown fox jumps over the lazy dog"
key = 3
ciphertext = tritemius_cipher(plaintext, key)
print(ciphertext)
# prints "wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj"

decrypted_text = tritemius_decipher(ciphertext, key)
print(decrypted_text)
# prints "the quick brown fox jumps over the lazy dog"
