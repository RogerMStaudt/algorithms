print("This program make a list with the numbers that you send, and make a sum with them. Write 'q' if to finish the list.")

list = []

while True:
    number = input("Write a number: ")
    
    if number == 'quit':
        break
    
    list.append(number)
