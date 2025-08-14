from datetime import datetime
from tabulate import tabulate

class QA:
    def __init__(self, q, a, tags = None):
        if tags is None:
            tags = []
        tags.sort()
        self.q = q
        self.a = a
        self.tags = tags
        self.date = datetime.now().strftime('%Y%m%d')

    def __str__(self):
        return f'''q: {self.q}
a: {self.a}
tags   : {self.tags}
date   : {self.date}'''

    def display(self):
        headers = ['date', 'q', 'a', 'tags']
        content = [[self.date, self.q, self.a, self.tags]]
        print(tabulate(content, headers))

    def __eq__(self, other):
        return self.q == other.q and self.a == other.a and self.tags == other.tags

    def reverse(self):
        self.q, self.a = self.a, self.q


if __name__ == '__main__':
    v1 = QA('pies', 'chien', ['animaux', 'pl'])
    v3 = QA('pies', 'chien', ['animals', 'pl'])
    
    print(v1)

    print(v1 == v3)
    v1.display()
