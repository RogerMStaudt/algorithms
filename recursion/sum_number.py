def ask_question():
    number = int(input("Digit a number positive: "))

    if number < 1:
        print("The number that you digit isn't a positive number.")

        ask_question()

    sum_numbers(number)

def sum_numbers(final_num):
    if final_num == 0:
        return 0
    
    return final_num + sum_numbers(final_num - 1)

print(ask_question())