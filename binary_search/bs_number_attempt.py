number_item_list = int(input("Enter the number of items in the list: "))

def number_attempts():
    attempts = 0
    number = int(number_item_list)
    
    while True:
        number = number / 2

        attempts += 1
        
        if number <= 1:
            return attempts

print(number_attempts())