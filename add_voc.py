from user import User
from voc import VocUnit
from sys import argv
from get_user import get_user

if __name__ == '__main__':

    user = get_user()
 
    try:
        string1 = argv[1]
        string2 = argv[2]
    except:
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

    voc = VocUnit(string1, string2, tags)
    user.add_voc(voc)

