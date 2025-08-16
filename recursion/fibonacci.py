def ask_question():
    number = int(input("Enter any number to find out its value in the Fibonacci sequence: "))

    if number < 0:
        print("Your number has to be positive.")

        ask_question()

    return fibonacci(number)

def fibonacci(num):
    first_term = 0
    second_term = 1
    third_term = first_term + second_term

    if second_term == (third_term - 1):
        return third_term
    
    return 

print(ask_question())