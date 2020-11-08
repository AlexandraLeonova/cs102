def encrypt_vigenere(plaintext: str, keyword: str) -> str:
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
        if ord("A") <= ord(keyword[t]) <= ord("Z"):
            shift = ord(keyword[t]) - ord("A")
        elif ord("a") <= ord(keyword[t]) <= ord("z"):
            shift = ord(keyword[t]) - ord("a")
        else:
            continue
        if ord("A") <= ord(plaintext[s]) <= ord("Z"):
            if ord("Z") - ord(plaintext[s]) < shift:
                ciphertext += chr(ord("A") - 1 + (shift - ord("Z") + ord(plaintext[s])))
            else:
                ciphertext += chr(ord(plaintext[s]) + shift)

        elif ord("a") <= ord(plaintext[s]) <= ord("z"):
            if ord("z") - ord(plaintext[s]) < shift:
                ciphertext += chr(ord("a") - 1 + (shift - ord("z") + ord(plaintext[s])))
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
        if "a" <= ciphertext[s] <= "z":
            plaintext += chr(ord("a") + ((ord(ciphertext[s]) + 7) % 26 - shift) % 26)
        elif "A" <= ciphertext[s] <= "Z":
            shift = (ord(keyword[s % len(keyword)]) + 13) % 26 
            plaintext += chr(ord("A") + ((ord(ciphertext[s]) + 13) % 26 - shift) % 26)
        else:
            plaintext += ciphertext[s]
    return plaintext
