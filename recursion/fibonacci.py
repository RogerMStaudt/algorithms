def ask_question():
    number = int(input("Enter any number to find out its value in the Fibonacci sequence: "))

    if number < 0:
        print("Your number has to be positive.")

        ask_question()

    return fibonacci(number)


def fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    
    return (fibonacci(num - 1) + fibonacci(num - 2))

print(ask_question())