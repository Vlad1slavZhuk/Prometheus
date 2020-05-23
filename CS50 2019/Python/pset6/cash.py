from cs50 import get_float
from math import floor

while True:
    f = get_float("Change owed: ")
    fl = floor(f * 100)
    if f > 0:
        break
    

quarters = fl // 25
dimes = (fl % 25) // 10
nickels = ((fl % 25) % 10) // 5
pennies = ((fl % 25) % 10) % 5

count = quarters + dimes + nickels + pennies

print(f"{count}")