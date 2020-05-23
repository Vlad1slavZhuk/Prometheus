from cs50 import get_int

while True:
    s = get_int("Height: ")
    if(s > 0 and s < 9):
        break
    
for i in range(s):
    for j in range(s - i - 1):
        print(" ", end="")
    for n in range(i + 1):
        print("#", end="")
    print()