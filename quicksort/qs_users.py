users = [
    {'name': 'Felipe', 'age': 25},
    {'name': 'Arthur', 'age': 32},
    {'name': 'Maggie', 'age': 12},
    {'name': 'Joseph', 'age': 65},
    {'name': 'Brice', 'age': 98},
    {'name': 'Sam', 'age': 23},
    {'name': 'Bruno', 'age': 100}
]

def quicksort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[round((len(list) - 1) / 2)]
        smaller_than_pivot = []
        greater_than_pivot = []

        for i in list:
            if i['name'] < pivot['name']:
                smaller_than_pivot.append(i)
            elif i['name'] > pivot['name']:
                greater_than_pivot.append(i)

        return quicksort(smaller_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
print(quicksort(users))