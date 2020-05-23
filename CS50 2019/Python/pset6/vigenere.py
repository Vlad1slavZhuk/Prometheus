from cs50 import get_string
from sys import argv, exit

if len(argv) != 2:
    print("Usage: python vigenere.py k")
    exit(1)

for ch in argv[1]:
    if not ch.isalpha():
        print("Usage: python vigenere.py k")
        exit(1)
        
k = argv[1]

p = get_string("plaintext:  ")

print("ciphertext: ", end="")

j = 0

for ch in p:
    if not ch.isalpha():
        print(ch, end="")
        continue
    
    ascii_ = 65 if ch.isupper() else 97
    pi = ord(ch) - ascii_
    kj = ord(k[j % len(k)].upper()) - 65
    ci = (pi + kj) % 26
    j += 1
    
    print(chr(ci + ascii_), end="")

print()
exit(0)