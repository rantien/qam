from qa import QA
from quiz import Quiz, Question
from sys import argv
from get_user import get_user
from random import shuffle

def add_qa(user):
    try:                                                  
        q = argv[2]
        a = argv[3]
    except:
        print('Add at least two parameters (Q and A).')
        exit()
    
    tags = argv[4:]

    qa = QA(q, a, tags)
    user.add_qa(qa)

def add_qa_from_xlsx(user):
    pass

def display_qa_list(user):
    tags = argv[2:]

    user.display_qa_list(tags = tags)

def generate_quiz(user):
    tags = argv[2:]

    qa_list = user.generate_qa_list(tags = tags)
    shuffle(qa_list)
    question_list = [Question(qa[1], qa[2], qa[3]) for qa in qa_list]

    quiz = Quiz(question_list)
    quiz.run()

def display_tags(user):
    pass

def remove(user):
    pass

def switch_user():
    pass


if __name__ == '__main__':
    
    user = get_user()
    
    try:
        match argv[1]:
            case '-a':
                add_qa(user)
            case '-ax':
                add_qa_from_xlsx(user)            
            case '-d':
                display_qa_list(user)
            case '-q':
                generate_quiz(user)
            case '-t':
                display_tags(user)
            case '-rm':
                remove(user)
            case '-su':
                switch_user()
            case _:
                print('The first parameter is not appropriate.')

    except:
        print('Missing parameters.')
        exit()
