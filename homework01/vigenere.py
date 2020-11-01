def encrypt_vigenere(plaintext: str , keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""
    for s in range(len(plaintext)):
        t = s % len(keyword)
        if ord('A') <= ord(keyword[t]) <= ord('Z'):
            shift = ord(keyword[t]) - ord('A')
        elif ord('a') <= ord(keyword[t]) <= ord('z'):
            shift = ord(keyword[t]) - ord('a')
        else: 
            continue

        if ord('A') <= ord(plaintext[s]) <= ord('Z'):
            if 65 <= ord(keyword[t]) <= 90:
                shift = ord(keyword[t]) - 65
            elif 97 <= ord(keyword[t]) <= 122:
                shift = ord(keyword[t]) - 97
            else: 
                continue

            if ord('Z') - ord(plaintext[s]) < shift:
                ciphertext += chr(ord('A') - 1 + (shift - ord('Z') + ord(plaintext[s])))
            else:
                ciphertext += chr(ord(plaintext[s]) + shift)

        elif ord('a') <= ord(plaintext[s]) <= ord('z'):
            if 65 <= ord(keyword[t]) <= 90:
                shift = ord(keyword[t]) - 65
            elif 97 <= ord(keyword[t]) <= 122:
                shift = ord(keyword[t]) - 97
            else: 
                continue
            if ord('z')  - ord(plaintext[s]) < shift:
                ciphertext += chr(ord('a') - 1 + (shift - ord('z') + ord(plaintext[s])))
            else:
                ciphertext += chr(ord(plaintext[s]) + shift)
        else:
            ciphertext += plaintext[s]
    return ciphertext

def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for s in range(len(ciphertext)):
        t = s % len(keyword)
        if ord('A') <= ord(keyword[t]) <= ord('Z'):
            shift = ord(keyword[t]) - ord('A')
        elif ord('a') <= ord(keyword[t]) - ord('z'):
            shift = ord(keyword[t]) - ord('a')
        else:
            continue
        if ord('A') <= ord(ciphertext[s]) <= ord('Z'):
            if ord(ciphertext[s]) - shift < ord('A'):
                plaintext += chr(ord('Z') + 1 - (shift - (ord(ciphertext[s]) - ord('A'))))
            else:
                plaintext += chr(ord(ciphertext[s]) - shift)
        elif ord('a')<=ord(ciphertext[s])<=ord('z'):
            if ord(ciphertext[s]) - shift < ord('a'):
                plaintext += chr(ord('z') + 1 - (shift - (ord(ciphertext[s]) - ord('a'))))
            else:
                 plaintext += chr(ord(ciphertext[s]) - shift)
        else:
            plaintext += ciphertext[s]
    return plaintext
