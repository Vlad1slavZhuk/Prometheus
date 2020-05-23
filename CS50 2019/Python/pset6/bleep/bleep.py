from cs50 import get_string
from sys import argv

def main():
    if len(argv) == 2:
        f = open(argv[1], "r")
    else:
        print("Usage: python bleep.py dictionary")
    
    content = f.read()
    text = get_string("What message would you like to censor?\n")
    words = text.split(" ")
    
    for word in words:
        if word.lower() in content:
            print("*" * len(word), end=" ")
        else:
            print(word, end=" ")
    
    print()
    
if __name__ == "__main__":
    main()
