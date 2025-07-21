from voc import VocUnit


class Question:
    def __init__(self, string1, string2):
        self.text = string1
        self.answer = string2
    
    def __str__(self):
        return f'Q: {self.text}\nA: {self.answer}'


class Quiz:
    def __init__(self, list_voc, order = True):
        if order:
            self.questions = [Question(voc.string1, voc.string2) for voc in list_voc]
        else:
            self.questions = [Question(voc.string2, voc.string1) for voc in list_voc] 
    
    def __str__(self):
        my_str = ''
        count = 1
        for question in self.questions:
            my_str += f'#{count}\n{question}\n**********\n'
            count += 1
        return my_str


if __name__ == '__main__':
    v1 = VocUnit('pies', 'chien', ['animaux', 'pl'])
    v2 = VocUnit('kot', 'chat', ['animaux', 'pl'])
    v3 = VocUnit('ptak', 'oiseau', ['animaux', 'pl'])
    v4 = VocUnit('lis', 'renard', ['animaux', 'pl'])
    v5 = VocUnit('wilk', 'loup', ['animaux', 'pl'])

    list_voc = [v1, v2, v3, v4, v5]

    my_quiz = Quiz(list_voc, order = True)
    print(my_quiz)
    my_quiz = Quiz(list_voc, order = False)
    print(my_quiz)
