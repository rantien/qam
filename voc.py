import datetime

class VocUnit:
    def __init__(self, string1, string2, tags):
        self.string1 = string1
        self.string2 = string2
        self.tags = tags
        self.datetime = datetime.datetime.now()

    def __str__(self):
        return f'''string1  : {self.string1}
string2  : {self.string2}
tags     : {self.tags}
datetime : {self.datetime}'''

    def __eq__(self, other):
        return self.string1 == other.string1 and self.string2 == other.string2

    def reverse(self):
        self.string1, self.string2 = self.string2, self.string1

def is_string_ok(my_str):
    return not my_str.replace(' ', '') == ''

def input_voc_unit():
        string1 = ''
        string2 = ''
        while not is_string_ok(string1):
               string1 = input('Enter string1: ')
        while not is_string_ok(string2):
               string2 = input('Enter string2: ')
        tags = input("Enter tags (separated by ','): ")
        tags = [tag.strip() for tag in tags.split(',')]
        return VocUnit(string1, string2, tags)


if __name__ == '__main__':
    v1 = VocUnit('pies', 'chien', ['animaux', 'pl'])
    print(v1)
    v1.reverse()
    print(v1)
    v2 = VocUnit('kot', 'chat', ['animaux', 'pl'])
    print(v1)
    print(v1 == v2)
    v3 = VocUnit('pies', 'chien', ['animals', 'pl'])
    print(v1 == v3)
