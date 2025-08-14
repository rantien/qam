from user import User

user_filename = 'user'

if __name__ == '__main__':
    with open(user_filename, 'r', encoding = 'utf-8') as f:
        name = f.read().replace('\n','')

    user = User(name)
    print(f'Affichage du vocabulaire de {name}') 
    user.display_voc()
    
    print(f'\nAffichage du vocabulaire de {name}, tag "pl"') 
    voc_list = user.generate_voc_list(['pl'])
    for voc in voc_list:
        print(voc)

    print(f'\nAffichage du vocabulaire de {name}, tags "pl", "animal"') 
    voc_list = user.generate_voc_list(['pl', 'animal'])
    for voc in voc_list:
        print(voc)

    print(f'\nAffichage du vocabulaire de {name}, tags ""') 
    voc_list = user.generate_voc_list([])
    for voc in voc_list:
        print(voc)
