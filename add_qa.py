from user import User
from qa import QA
from sys import argv
from get_user import get_user

if __name__ == '__main__':

    user = get_user()
 
    try:
        q = argv[1]
        a = argv[2]
    except:
        print('Add at least two parameters (Q and A).')
        exit()

    tags = []
    over = False
    counter = 3
    while not over:
        try:
            tags.append(argv[counter])
        except:
            over = True
        else:
            counter += 1

    qa = QA(q, a, tags)
    user.add_qa(qa)

