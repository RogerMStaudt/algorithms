number = print("This program calculates the exponent of a number.")

number = int(input("Give me the number: "))
exponent = int(input("Give me the exponent: "))

def expo(num, exp):
    if exp == 1:
        return num
    elif exp == 0:
        return 1
    
    return num * expo(num, exp - 1)

print(expo(number, exponent))