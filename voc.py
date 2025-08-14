from datetime import datetime
from tabulate import tabulate

class VocUnit:
    def __init__(self, string1, string2, tags = []):
        self.string1 = string1
        self.string2 = string2
        self.tags = tags
        self.date = datetime.now().strftime('%Y%m%d')

    def __str__(self):
        return f'''string1: {self.string1}
string2: {self.string2}
tags   : {self.tags}
date   : {self.date}
'''

    def display(self):
        headers = ['date', 'string1', 'string2', 'tags']
        content = [[self.date, self.string1, self.string2, self.tags]]
        print(tabulate(content, headers))

    def __eq__(self, other):
        print(other.tags.sort())
        print(self.tags.sort())
        return self.string1 == other.string1 and self.string2 == other.string2 and self.tags.sort() == other.tags.sort()

    def reverse(self):
        self.string1, self.string2 = self.string2, self.string1


if __name__ == '__main__':
    v1 = VocUnit('pies', 'chien', ['animaux', 'pl'])
    v3 = VocUnit('pies', 'chien', ['animals', 'pl'])
    print(v1 == v3)
    print(v1)
    v1.display()
