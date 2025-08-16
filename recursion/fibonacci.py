def ask_question():
    number = int(input("Enter any number to find out its value in the Fibonacci sequence: "))

    if number < 0:
        print("Your number has to be positive.")

        ask_question()

    return fibonacci(number)

def fibonacci(num):
    first_term = num - 2
    second_term = num - 1
    third_term = num

    if first_term == 0:
        return 1
    
    return third_term + fibonacci(first_term + second_term)

print(ask_question())