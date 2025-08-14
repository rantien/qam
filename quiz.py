class Question:
    def __init__(self, string1, string2, tags):
        self.text = string1
        self.answer = string2
        self.tags = tags
    
    def __str__(self):
        return self.text

    def eval_answer(self, my_answer):
        return self.answer == my_answer 

class Quiz:
    def __init__(self, voc_list, order = True):
        self.over = False 
        self.points = 0
        self.length = min(5, len(voc_list))
        self.pos = 1
        if order:
            self.questions = [Question(voc.string1, voc.string2, voc.tags) for voc in voc_list[:self.length]]
        else:
            self.questions = [Question(voc.string2, voc.string1, voc.tags) for voc in voc_list[:self.length]] 
    
    def __str__(self):
        my_str = ''
        count = 1
        for question in self.questions:
            my_str += f'#{count}\n{question}\n**********\n'
            count += 1
        return my_str

    def score(self):
        return f'{self.points}/{self.length}'

    def position(self):
        return f'{self.pos}/{self.length}'

    def increment(self):
        if self.pos <= self.length:
            self.pos += 1
        if self.pos > self.length:
            self.over = True

    def current_question(self):
        return self.questions[self.pos-1]

    def answer_question(self, my_answer):
        if not self.over:
            if self.current_question().eval_answer(my_answer):
                self.points += 1
                self.increment()
                return True
            else:
                self.increment()
                return False
        else:
            self.increment()
            return False
