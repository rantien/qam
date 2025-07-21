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


if __name__ == '__main__':
    v = VocUnit('pies', 'chien', ['animaux', 'pl'])
    print(v)
