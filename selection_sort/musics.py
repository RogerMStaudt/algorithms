playlist = [
    {"title": "Nothing Else Matters", "view": 523},
    {"title": "Chop Suey!", "view": 389},
    {"title": "Everlong", "view": 712},
    {"title": "Bohemian Rhapsody", "view": 438},
    {"title": "Comfortably Numb", "view": 658},
    {"title": "Smells Like Teen Spirit", "view": 912},
    {"title": "Highway to Hell", "view": 271},
    {"title": "Enter Sandman", "view": 834}
]

def search_minor(list):
    minor = list[0]['view']
    index_minor = 0
    
    for i in range(1, len(list)):
        if minor < list[i]['view']:
            minor = list[i]['view']
            index_minor = i

    return index_minor

def selection_sort(list):
    sorted_list = []

    for i in range(len(list)):
        minor = search_minor(list)
        sorted_list.append(list.pop(minor))
    
    return sorted_list

print(selection_sort(playlist))