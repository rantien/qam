from user import User
from quiz import Quiz
from get_user import get_user

def display_qa():
    user = get_user()
    user.display_qa()

if __name__ == '__main__':
    display_qa()
