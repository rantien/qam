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

    # return the lowest available ID (integer > 0)

    def get_free_ID(self):
        list_existing_id = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f, delimiter = '|')
                for row in reader:
                    list_existing_id.append(row[0])
        if list_existing_id == []:
            return 1
        else:
            list_existing_id = [int(my_id) for my_id in list_existing_id]
            list_potential_id = list(range(1, max([int(my_id) for my_id in list_existing_id]) + 2))
            for my_id in list_potential_id:
                if not my_id in list_existing_id:
                    return my_id

    # check if the QA already exists in the user file

    def does_qa_exist(self, qa):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                qa_row = QA(row[2], row[3], transform_str_into_list(row[4]))    
                if qa_row == qa:
                        return True
        return False

    # add a QA to the user file

    def add_qa(self, qa):
        if self.does_qa_exist(qa):
            print(f'There is already such a record.')
            return False
        
        records = [[self.get_free_ID(), \
                    datetime.now().strftime('%Y%m%d'), \
                    qa.q, \
                    qa.a, \
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

    # remove the QA with a given id

    def remove_id(self, list_id = None):
        if list_id is None:
            return False

        records = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f, delimiter = '|')
                for row in reader:
                    if not row[0] in list_id: 
                        records.append([row[0], row[1], row[2], row[3], row[4]])
                    else:
                        print(f'Record #{row[0]} deleted.')

        with open(self.filename, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f, delimiter = '|')
                for r in records:
                    writer.writerow([r[0], r[1], r[2], r[3], r[4]])
    
        return True

    # get the number of QA of the user

    def __len__(self):
        with open(self.filename, 'r') as f:
            return len(f.readlines())

    # get all the tags of the user. 
    # if 'tags' != None, lists all the tags related to 'tags'

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

    # generate a list of all QA (related to the tags entered, if any)

    def generate_qa_list(self, tags = None):
        if tags is None:
            tags = []
        else:
            tags.sort()

        qa_list = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                if tags:
                    if set(tags).issubset(transform_str_into_list(row[4])):         
                        qa_list.append([row[0], row[1], row[2], row[3], row[4]])
                else:
                    qa_list.append([row[0], row[1], row[2], row[3], row[4]])
        return qa_list

    # display the list of all QA (related to the tags entered, if any)

    def display_qa_list(self, tags = None):
        if tags is None:
            tags = []

        qa_list = self.generate_qa_list(tags)
        
        print('\n' + tabulate(qa_list, headers = ['id', 'date', 'q', 'a', 'tags']) + '\n')


# extracts the current user

user_filename = 'user'

def get_user():
    with open(user_filename, 'r', encoding = 'utf-8') as f:
        name = f.read().replace('\n','')

    return User(name)
