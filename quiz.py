class Question:
    def __init__(self, q, a, tags):
        self.q = q
        self.a = a
        self.tags = tags

    def eval_answer(self, my_answer):
        a = self.a.replace('’', "'")
        my_answer = my_answer.replace('’', "'")
        return a == my_answer 

class Quiz:
    def __init__(self, question_list, reverse = False):
        self.over = False 
        self.points = 0
        self.length = min(5, len(question_list))
        self.pos = 1
        if not reverse:
            self.questions = [Question(question.q, question.a, question.tags) for question in question_list[:self.length]]
        else:
            self.questions = [Question(question.a, question.q, question.tags) for question in question_list[:self.length]] 

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

    def current_prompt(self):
        return self.questions[self.pos-1].q

    def current_tags(self):
        return self.questions[self.pos-1].tags

    def current_answer(self):
        return self.questions[self.pos-1].a

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
            return False

    def run(self):
        while not self.over:
            print(f'\n({self.position()}): "{self.current_prompt()}"')
            print(f'({self.position()})  {self.current_tags()}')
            my_answer = input('\nYour answer: ')
            correct_answer = self.current_answer()
            if self.answer_question(my_answer):
                print('Good answer!')
            else:
                print(f'Wrong answer.\nCorrect answer: {correct_answer}')
        
        print(f"\nIt's over. Your score: {self.score()}.\n")
