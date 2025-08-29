list_numbers = [5,1,74,3,643,43,6,2]

number = int(input("Write a number to search it on the list: "))

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        smaller_than_pivot = [i for i in list[1:] if i <= pivot]
        greater_than_pivot = [i for i in list[1:] if i > pivot]

        return quicksort(smaller_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_list = quicksort(list_numbers)

def by_search(list, num, first_position, last_position):
    middle = round((last_position + first_position) / 2)

    if last_position >= first_position:
        if list[middle] == num:
            return middle
        elif list[middle] > num:
            return by_search(list, number, first_position, middle - 1)
        else:
            return by_search(list, number, middle + 1, last_position)
    else:
        return 'None'

print(by_search(sorted_list, number, 0, len(sorted_list) - 1))
