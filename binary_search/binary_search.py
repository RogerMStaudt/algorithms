def search(list, guess):
    first = 0
    last = len(list) - 1
    

    while first <= last:
        middle = round(last / 2)

        if list[middle] > guess:
            last = middle
        elif list[middle] < guess:
            first = middle
        else:
            return middle
        
    return 'none'


my_list = [1, 5, 10, 15, 20, 25, 30, 35, 40]

print(search(my_list, 2))