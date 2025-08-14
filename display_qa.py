from user import User
from quiz import Quiz
from get_user import get_user

def display_qa_list(tags = []):
    user = get_user()
    user.display_qa_list(tags = tags)

if __name__ == '__main__':
    print('\nAll records\n')
    display_qa_list()
    
    print('\nTag: "pl"\n')
    display_qa_list(tags = ['pl'])

    print('\nTags: "de", "animal"\n')
    display_qa_list(tags = ['de', 'animal'])
