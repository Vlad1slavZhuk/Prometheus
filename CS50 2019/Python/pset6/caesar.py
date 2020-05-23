from cs50 import get_string
from sys import argv, exit

if len(argv) != 2:
    print("Usage: python caesar.py k")
    exit(1)

k = int(argv[1])
text = get_string("plaintext:  ")
print("ciphertext: ", end="")

for ch in text:
    if not ch.isalpha():
        print(ch, end="")
        continue
    
    ascii_ = 65 if ch.isupper() else 97
    pi = ord(ch) - ascii_
    ci = (pi + k) % 26
    
    print(chr(ci + ascii_), end="")

print()