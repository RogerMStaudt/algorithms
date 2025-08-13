number = int(input("Write a number and find its factorial: "))
result = 0

def factorial(factorial_number, next_num=-1):
    if next_num == -1:
        next_number = factorial_number - 1
    else:
        next_number = next_num - 1

    result = factorial_number * next_number

    if next_number == 1:
        return result
    
    factorial(result, next_number)

    return result

value = factorial(number)

print('The factorial of ' + str(number) + ' is: ' + str(value))