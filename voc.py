import datetime

class VocUnit:
    def __init__(self, string1, string2, tags):
        self.string1 = string1
        self.string2 = string2
        self.tags = tags
        self.datetime = datetime.datetime.now()

    def __str__(self):
        return f'''{self.string1}
{self.string2}
{self.tags}
{self.datetime}'''


def is_string_ok(my_str):
    my_str = my_str.replace(' ', '')
    if my_str == '':
        return False
    else:
        return True

def input_voc_unit():
        string1 = ''
        string2 = ''
        while not is_string_ok(string1):
               string1 = input('Enter string1: ')
        while not is_string_ok(string2):
               string2 = input('Enter string2: ')
        tags = input("Enter tags (separated by ',': ")
        tags = [tag.strip() for tag in tags.split(',')]
        return VocUnit(string1, string2, tags)


if __name__ == '__main__':
    v = VocUnit('pies', 'chien', ['animaux', 'pl'])
    print(v)
