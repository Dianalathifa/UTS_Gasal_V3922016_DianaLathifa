#!/usr/bin/env python
# coding: utf-8

# In[4]:


#V3922016_DIANA LATHIFA_UTS SKD Kombinasi Caesar Cipher dengan Vigenere Cipher

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = (ord(char) - ord('a') + shift) % 26
            char = chr(shifted + ord('a'))
            if is_upper:
                char = char.upper()
        result += char
    return result

def caesar_decrypt(ciphertext, shift):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = (ord(char) - ord('a') - shift) % 26
            char = chr(shifted + ord('a'))
            if is_upper:
                char = char.upper()
        result += char
    return result

def vigenere_encrypt(text, key):
    result = ""
    key_length = len(key)
    for i in range(len(text)):
        if text[i].isalpha():
            is_upper = text[i].isupper()
            text_char = text[i].lower()
            key_char = key[i % key_length].lower()
            shifted = (ord(text_char) - ord('a') + ord(key_char) - ord('a')) % 26
            encrypted_char = chr(shifted + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
        else:
            result += text[i]
    return result

def vigenere_decrypt(ciphertext, key):
    result = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            is_upper = ciphertext[i].isupper()
            text_char = ciphertext[i].lower()
            key_char = key[i % key_length].lower()
            shifted = (ord(text_char) - ord('a') - (ord(key_char) - ord('a')) + 26) % 26
            decrypted_char = chr(shifted + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            result += decrypted_char
        else:
            result += ciphertext[i]
    return result

# Teks yang akan dienkripsi
plaintext = "Success is not final, failure is not fatal, it is the courage to continue that counts"
# Kunci Vigenere Cipher berupa nama panggilan "lathif"
vigenere_key = "lathif"
# Shift untuk Caesar Cipher
caesar_shift = 3

# Enkripsi dengan Caesar Cipher
caesar_encrypted = caesar_encrypt(plaintext, caesar_shift)
print("Hasil Enkripsi dengan Caesar Cipher:")
print(caesar_encrypted)

# Deskripsi dengan Caesar Cipher
caesar_decrypted = caesar_decrypt(vigenere_decrypted, caesar_shift)
print("\nHasil Deskripsi dengan Caesar Cipher:")
print(caesar_decrypted)


# Enkripsi hasil Caesar Cipher dengan Vigenere Cipher
vigenere_encrypted = vigenere_encrypt(caesar_encrypted, vigenere_key)
print("\nHasil Enkripsi Vigenere dari hasil Caesar Cipher:")
print(vigenere_encrypted)

# Deskripsi Vigenere Cipher dengan kunci "lathif"
vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, vigenere_key)
print("\nHasil Deskripsi Vigenere Cipher:")
print(vigenere_decrypted)


# In[ ]:




