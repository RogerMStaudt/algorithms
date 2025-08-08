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

def create_dict_music(title, view):
    return {"title": title, "view": view}

def selection_sort(list):
    list_sorted = []
    last_view = None
    
    for music in list:
        number_views = music['view']
        
        if last_view is None:
            list_sorted.append(create_dict_music(music['title'], music['view']))

            continue
        elif number_views < last_view:
            list_sorted

    return list_sorted



print(selection_sort(playlist))