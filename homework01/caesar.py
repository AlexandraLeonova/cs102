import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = "" 
    for s in range(len(plaintext)):
        if  ord('a') <= ord(plaintext[s]) <=  ord('z'):
            ciphertext += chr(((ord(plaintext[s]) - ord('a') + shift) % 26) + ord('a'))
        elif ord('A') <= ord(plaintext[s]) <= ord('Z'):
            ciphertext += chr(((ord(plaintext[s]) - ord('A') + shift) % 26) + ord('A'))
        else:
            ciphertext += plaintext[s]   
    return ciphertext

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for s in range(len(ciphertext)):
        if ord('a') <=  ord(ciphertext[s]) <= ord('z'):
             plaintext += chr(((ord(ciphertext[s]) - ord('a') - shift) % 26) + ord('a'))
        elif ord('A') <= ord(ciphertext[s]) <=  ord('Z'):
            plaintext += chr(((ord(ciphertext[s]) - ord('A') - shift) % 26) + ord('A')
        else: 
            plaintext += ciphertext[s]
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker("python", d)
    0
    >>> caesar_breaker("sbwkrq", d)
    3
    """
    best_shift = 0 
    sasha = ciphertext.split()
    for sash in sasha:
        for i in range(0,26):
            decr_word = decrypt_caesar(sash, i)
            if decr_word in dictionary:
                best_shift = i
    return best_shift
