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

def by_search(list):
    first_number = 0
    last_number = 0

    middle = round(len(list) / 2)

    if list[middle] == number:
        return middle
    elif list[middle] > number:
        first_number = middle + 1
    else:
        last_number = middle - 1

    if len(list) < 2:
        return 'None'
    
    return by_search(list[first_number:last_number])

print(sorted_list)
print(by_search(sorted_list))