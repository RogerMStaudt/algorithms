print("This program order a list with the numbers that you send. Write 'q' if to finish the list.")

list_numbers = []

while True:
    number = input("Write a number: ")
    
    if number == 'q':
        break
    
    list_numbers.append(int(number))

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        smaller_than_pivot = [i for i in list[1:] if i <= pivot]
        greater_than_pivot = [i for i in list[1:] if i > pivot]

        return quicksort(smaller_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
print(quicksort(list_numbers))

