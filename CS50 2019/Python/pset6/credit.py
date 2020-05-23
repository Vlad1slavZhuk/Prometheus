from cs50 import get_int

def main():
    while True:
        number = get_int("Number: ")
        if number > 0:
            break
        
    number1 = number
    length = len(str(number))
    sum1 = 0
    sum2 = 0
    while number > 0:
        sum1 += (number % 10)
        tmp = number // 10
        if (tmp % 10) * 2 > 9:
            a = ((tmp % 10) * 2) % 10
            b = ((tmp % 10) * 2) // 10
            sum2 += a + b
        else:
            sum2 += (tmp % 10) * 2
        
        number //= 100
    
    summa = sum1 + sum2
    
    if summa % 10 == 0:
        if (number1 >= 340000000000000 and number1 < 350000000000000) or (number1 >= 370000000000000 and number1 < 380000000000000):
            print("AMEX")
        elif number1 >= 5100000000000000 and number1 < 5600000000000000:
            print("MASTERCARD")
        elif (number1 >= 4000000000000 and number1 < 5000000000000) or (number1 >= 4000000000000000 and number1 < 5000000000000000):
            print("VISA")
        else:
            print("INVALID")
    else:
        print("INVALID")
    
if __name__ == "__main__":
    main()