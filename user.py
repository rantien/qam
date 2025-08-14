from datetime import datetime
import csv
from os.path import isfile
from voc import VocUnit 

class Question:
    def __init__(self, string1, string2):
        self.text = string1
        self.answer = string2
    
    def __str__(self):
        return f'Q: {self.text}\nA: {self.answer}'

class Quiz:
    def __init__(self, voc_list, order = True):
        if order:
            self.questions = [Question(voc.string1, voc.string2) for voc in voc_list]
        else:
            self.questions = [Question(voc.string2, voc.string1) for voc in voc_list] 
    
    def __str__(self):
        my_str = ''
        count = 1
        for question in self.questions:
            my_str += f'#{count}\n{question}\n**********\n'
            count += 1
        return my_str

class User:
    def __init__(self, my_str):
        self.name = my_str
        self.filename = f'data/{self.name}.csv'
        if not isfile(self.filename):
            with open(self.filename, 'w'):
                pass

    def __len__(self):
        with open(self.filename, 'r') as f:
            return len(f.readlines())

    def does_voc_unit_exist(self, voc_unit):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                voc_row = VocUnit(row[1], row[2])    
                if voc_row == voc_unit:
                        return True
        return False

    def add_voc_unit(self, voc_unit):
        v = voc_unit        
        if self.does_voc_unit_exist(v):
            print(f'There is already such a record.')
            return False
        
        records = []
        if not v.tags:
            records += [[datetime.now().strftime('%Y%m%d'), \
                         v.string1, \
                         v.string2, \
                         '']]
        else:
            for tag in v.tags:
                records += [[datetime.now().strftime('%Y%m%d'), \
                             v.string1, \
                             v.string2, \
                             tag]]
        
        with open(self.filename, 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f, delimiter = '|')
                for row in reader:
                    records.append([row[0], row[1], row[2], row[3]])

        with open(self.filename, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f, delimiter = '|')
                for r in records:
                    writer.writerow([r[0], r[1], r[2], r[3]])

    def display_voc(self):
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                print(row)

    def generate_voc_list(self, tags):
        voc_list = [] 
        with open(self.filename, 'r', encoding = 'utf-8') as f:
             reader = csv.reader(f, delimiter = '|')
             for row in reader:
                 voc_row = VocUnit(row[1], row[2])    
                 if row[3] in tags and not voc_row in voc_list:
                    voc_list.append(voc_row)
        return voc_list
 
