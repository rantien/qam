from user import User

user_filename = 'user'

def get_user():
    with open(user_filename, 'r', encoding = 'utf-8') as f:
        name = f.read().replace('\n','')

    return User(name)
