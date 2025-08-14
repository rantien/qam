from user import User
from quiz import Quiz
from get_user import get_user

def display_qa(tags = []):
    user = get_user()
    user.display_qa(tags = tags)

if __name__ == '__main__':
    print('\nAll records\n')
    display_qa()
    
    print('\nTag "pl"\n')
    display_qa(tags = ['pl'])

    print('\nTags "de" "animal"\n')
    display_qa(tags = ['de', 'animal'])
