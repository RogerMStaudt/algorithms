number = int(input("Write a number and find its factorial: "))
result = 0

def factorial(number_factorial):
    next_number = number_factorial - 1

    if next_number != 1:
        result = number_factorial * next_number

    if next_number == 1:
        return result
    
    factorial(next_number)

print(f'The factorial of {number} is: {factorial(number)}')