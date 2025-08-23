from datetime import datetime
import csv
from os.path import isfile
from qa import QA 
from tabulate import tabulate

# '"['a', 'b', 'c']" => ['a', 'b', 'c']

def transform_str_into_list(my_str):
    return [element.strip()[1:-1] for element in my_str[1:-1].split(',')]


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
                qa_row = QA(row[1], row[2], transform_str_into_list(row[4]))    
                if qa_row == qa:
                        return True
        return False

    def get_tags(self, tags = None):
        if tags is None:
            tags = []
        
        all_tags = []
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                list_row = transform_str_into_list(row[4])
                if tags == []:
                    all_tags += list_row
                elif set(tags).intersection(list_row) == set(tags):
                    all_tags += list_row

        all_tags = list(set(all_tags))
        all_tags.sort()
        return all_tags


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

        print(f'{self.filename} updated.')

    def generate_qa_list(self, tags = None):
        if tags is None:
            tags = []

        qa_list = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f, delimiter = '|')
            list_dummies = []
            for row in reader:
                dummy_str = f'{row[0]}|{row[1]}|{row[2]}|{row[4]}'
                if not dummy_str in list_dummies:
                    if tags:
                        if row[3] in tags:
                            qa_list.append([row[0], row[1], row[2], row[4]])
                    else:
                        qa_list.append([row[0], row[1], row[2], row[4]])
                    list_dummies.append(dummy_str) 
        return qa_list

    def display_qa_list(self, tags = None):
        if tags is None:
            tags = []

        qa_list = self.generate_qa_list(tags)
        
        print('\n' + tabulate(qa_list, headers = ['date', 'q', 'a', 'tags']) + '\n')


# extracts the current user

user_filename = 'user'

def get_user():
    with open(user_filename, 'r', encoding = 'utf-8') as f:
        name = f.read().replace('\n','')

    return User(name)
