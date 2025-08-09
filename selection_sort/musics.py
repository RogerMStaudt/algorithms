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
    list_sorted = [{'view': ''}]
    last_view = 0

    for music_position in range(0, len(list)):
        music_view = list[music_position]['view']
        title = list[music_position]['title']

        if music_position == 0 or last_view < music_view:
            list_sorted.append(create_dict_music(title, music_view))
        elif last_view > music_view:
            for i in reversed(list_sorted):
                if i == len(list_sorted):
                    continue
                elif music_view > list_sorted[i]['view']:
                    list_sorted.insert(music_view, i + 1)

        last_view = music_view

print(selection_sort(playlist))

# loop em cima da playlist

    # Se for o primeiro loop, insere na nova lista o valor

    # Caso contrário, se o valor anterior for menor do que o valor atual
    #   Apenas insere na nova lista o valor

    # Caso contrário, se o valor anterior for maior do que o valor atual
    #   Guardar valor atual
    #
    #   Fazer um loop na lista nova, do cara atual até o inicio da nova lista

    #       Se for o primeiro loop

    #           Guarda o valor

    #           Continua o loop
    #           
    #       Se o valor atual for menor que o valor guardado

    #           Adiciona o valor guardado no indice depois do valor atual






    
#def selection_sort(list):
#    list_sorted = []
#    last_view = {'view': ''}
#
#    for music_position in range(0, len(list)):
#        number_views = list[music_position]['view']
#        title = list[music_position]['title']
#
#        if music_position == 0:
#            list_sorted.append(create_dict_music(title, number_views))
#            last_view = create_dict_music(title, number_views)
#
#            continue
#        elif number_views > last_view['view']:
#            list_sorted.append(create_dict_music(title, number_views))
#
#        elif number_views < last_view['view']:
#            for i in reversed(list_sorted):
#                if i == len(list_sorted):
#                    last_value = list_sorted[i]['view']
#
#                    continue
#                elif list_sorted[i]['view'] < last_value:
#                    list_sorted.append(create_dict_music(title, list_sorted[i]['view']))
#
#                last_value = list_sorted[i]['view']
#            # fazer um loop verificando até que o valor que vier seja menor que o número, adiciona na frente
#
#        last_view = create_dict_music(title, number_views)
#
#    return list_sorted