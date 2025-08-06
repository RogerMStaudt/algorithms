brazilian_names = [
    'Abel', 'Adriano', 'Agnaldo', 'Alberto', 'Alexandre', 'Alisson', 'Aloísio',
    'Anderson', 'André', 'Antônio', 'Bruno', 'Caio', 'Carlos', 'César',
    'Christian', 'Ciro', 'Cláudio', 'Cristiano', 'Daniel', 'Danilo', 'Davi',
    'Denis', 'Diego', 'Douglas', 'Eduardo', 'Elias', 'Emerson', 'Enrique',
    'Erick', 'Ernesto', 'Estevão', 'Ezequiel', 'Fabiano', 'Fábio', 'Felipe',
    'Ferdinando', 'Fernando', 'Francisco', 'Frederico', 'Gabriel', 'George',
    'Geraldo', 'Gilberto', 'Guilherme', 'Gustavo', 'Heitor', 'Henrique',
    'Herbert', 'Hugo', 'Ian', 'Igor', 'Isac', 'Ismael', 'Ivan', 'Jacinto',
    'Jair', 'James', 'Jeferson', 'João', 'Joaquim', 'Jorge', 'José',
    'Josué', 'Júlio', 'Kauan', 'Kauê', 'Leonardo', 'Leônidas', 'Lucas',
    'Luciano', 'Luís', 'Marcelo', 'Márcio', 'Marcos', 'Matheus', 'Maurício',
    'Mauro', 'Michel', 'Miguel', 'Murilo', 'Nathan', 'Nelson', 'Neymar',
    'Nícolas', 'Nilton', 'Norberto', 'Osvaldo', 'Pablo', 'Paulo', 'Pedro',
    'Rafael', 'Raimundo', 'Ramon', 'Raul', 'Renan', 'Ricardo', 'Roberto',
    'Robson', 'Rodrigo', 'Rogério', 'Ronald', 'Ronaldo', 'Rubens', 'Samuel',
    'Sandro', 'Saulo', 'Sérgio', 'Sidnei', 'Silas', 'Silvio', 'Thiago',
    'Tomás', 'Ubiratan', 'Valdemar', 'Valdir', 'Valmir', 'Vanderlei',
    'Vicente', 'Victor', 'Vinícius', 'Vitor', 'Wallace', 'Walter', 'Wellington',
    'Wendel', 'Wesley', 'Willian', 'Wilson'
]

def search_name(list, name):
    begin = 0
    end = len(list)

    while begin <= end:
        middle = round((begin + end) / 2)
    

        if name > list[middle]:
            begin = middle + 1
        elif name < list[middle]:
            end = middle - 1
        else:
            return middle
        
    return 'none'

print(search_name(brazilian_names, "Márcio"))