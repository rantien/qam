class Question:
    def __init__(self, q, a, tags):
        self.q = q
        self.a = a
        self.tags = tags
    
    def __str__(self):
        return self.q

    def eval_answer(self, my_a):
        return self.a == my_a 

class Quiz:
    def __init__(self, qa_list, order = True):
        self.over = False 
        self.points = 0
        self.length = min(5, len(qa_list))
        self.pos = 1
        if order:
            self.questions = [Question(qa.q, qa.a, qa.tags) for qa in qa_list[:self.length]]
        else:
            self.questions = [Question(qa.a, qa.q, qa.tags) for qa in qa_list[:self.length]] 
    
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
