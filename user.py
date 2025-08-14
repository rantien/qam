from datetime import datetime
import csv
from os.path import isfile
from qa import QA 
from tabulate import tabulate

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

    def does_qa_exist(self, qa):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                qa_row = QA(row[1], row[2], row[4])    
                if qa_row == qa:
                        return True
        return False

    def add_qa(self, qa):
        if self.does_qa_exist(qa):
            print(f'There is already such a record.')
            return False
        
        records = []
        if not qa.tags:
            records += [[datetime.now().strftime('%Y%m%d'), \
                         qa.q, \
                         qa.a, \
                         '',
                         '']]
        else:
            for tag in qa.tags:
                records += [[datetime.now().strftime('%Y%m%d'), \
                             qa.q, \
                             qa.a, \
                             tag,
                             qa.tags]]
        
        with open(self.filename, 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f, delimiter = '|')
                for row in reader:
                    records.append([row[0], row[1], row[2], row[3], row[4]])

        with open(self.filename, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f, delimiter = '|')
                for r in records:
                    writer.writerow([r[0], r[1], r[2], r[3], r[4]])

    def display_qa(self, tags = []):
        qa_list = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                if tags:
                    if row[3] in tags:
                        qa_list.append([row[0], row[1], row[2], row[4]])
                else:
                    qa_list.append([row[0], row[1], row[2], row[4]])
        print(tabulate(qa_list, headers = ['date', 'q', 'a', 'tags']))

    def generate_qa_list(self, tags):
        qa_list = [] 
        with open(self.filename, 'r', encoding = 'utf-8') as f:
             reader = csv.reader(f, delimiter = '|')
             for row in reader:
                 qa_row = QA(row[1], row[2], row[4])    
                 if row[3] in tags:
                    qa_list.append(qa_row)
        return qa_list
