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
    k = ord('a')
    ok = ord('A')
    m = ord('z') 
    om = ord('Z')
    for s in range(len(plaintext)):
        if  k <= ord(plaintext[s]) <= m:
            ciphertext += chr(((ord(plaintext[s]) - k + shift) % 26) + k)
        elif ok <= ord(plaintext[s]) <= om:
            ciphertext += chr(((ord(plaintext[s]) - ok + shift) % 26) + ok)
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
    k = ord('a')
    ok = ord('A')
    # m = ord('z') 
    om = ord('Z')
    for s in range(len(ciphertext)):
        if k <=  ord(ciphertext[s]) <= ord('z'):
             plaintext += chr(((ord(ciphertext[s]) - k - shift) % 26) + k)
        elif ok <= ord(ciphertext[s]) <= om:
            plaintext += chr(((ord(ciphertext[s]) - ok - shift) % 26) + ok)
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

    