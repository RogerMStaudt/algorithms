print("This program make a list with the numbers that you send, and make a sum with them. Write 'q' if to finish the list.")

list = []

while True:
    number = input("Write a number: ")
    
    if number == 'q':
        break
    
    list.append(int(number))

def account():
    account = ''

    for i in list:
        if account == '':
            account = str(i)
        else:
            if i < 0:
                account += f' + ({str(i)})'
            else:
                account += f' + {str(i)}'
    
    return account

def sum_list(number):
    if number == 0:
        return list[number]

    return list[number] + sum_list(number - 1)

result = str(sum_list(len(list) - 1))

print(account() + ' = ' + result)