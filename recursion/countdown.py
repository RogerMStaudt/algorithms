def ask_question():
    number = int(input("Digit a positive number: "))

    if number < 0:
        print("Your number has to be positive.")

        ask_question()

    countdown(number)

def countdown(num):
    if num < 0:
        return
    
    print(num)

    countdown(num - 1)

ask_question()