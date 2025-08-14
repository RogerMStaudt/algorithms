def ask_question():
    number = int(input("Digit a number positive: "))

    if number < 1:
        print("The number that you digit isn't a positive number.")

        sum_numbers(number)

def sum_numbers(final_num):

    return num + sum_numbers(num + 1)