import typing as tp

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
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
    plaintext = ""
    k = ord('a')
    ok = ord('A')
    m = ord('z') 
    om = ord('Z')
    for s in range(len(ciphertext)):
        if k <=  ord(ciphertext[s]) <= m:
             plaintext += chr(((ord(ciphertext[s]) - k - shift) % 26) + k)
        elif ok <= ord(ciphertext[s]) <= om:
            plaintext += chr(((ord(ciphertext[s]) - ok - shift) % 26) + ok)
        else:
            plaintext += ciphertext[s]
    return plaintext

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0 
    sasha = ciphertext.split()
    for sash in sasha:
        for i in range(0,26):
            decr_word = decrypt_caesar(sash, i)
            if decr_word in dictionary:
                best_shift = i
    return best_shift