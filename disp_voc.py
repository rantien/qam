from user import User

user_filename = 'user'

if __name__ == '__main__':
    with open(user_filename, 'r', encoding = 'utf-8') as f:
        nname = f.read().replace('\n','')

    user = User(name)
    v = input_voc_unit()
    if user.does_voc_unit_exist(v):
        print(f'{name} already memorized this vocabulary unit.')
    else:
        user.add_voc_unit(v)
