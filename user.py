from datetime import datetime
import csv
from os.path import isfile
from voc import VocUnit 
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

    def does_voc_exist(self, voc):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                voc_row = VocUnit(row[1], row[2])    
                if voc_row == voc:
                        return True
        return False

    def add_voc(self, voc):
        if self.does_voc_exist(voc):
            print(f'There is already such a record.')
            return False
        
        records = []
        if not voc.tags:
            records += [[datetime.now().strftime('%Y%m%d'), \
                         voc.string1, \
                         voc.string2, \
                         '',
                         '']]
        else:
            for tag in voc.tags:
                records += [[datetime.now().strftime('%Y%m%d'), \
                             voc.string1, \
                             voc.string2, \
                             tag,
                             voc.tags]]
        
        with open(self.filename, 'r', encoding = 'utf-8') as f:
                reader = csv.reader(f, delimiter = '|')
                for row in reader:
                    records.append([row[0], row[1], row[2], row[3], row[4]])

        with open(self.filename, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f, delimiter = '|')
                for r in records:
                    writer.writerow([r[0], r[1], r[2], r[3], r[4]])

    def display_voc(self, tags = []):
        voc_list = []
        with open(self.filename, 'r', encoding = 'utf-8') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                if tags:
                    if row[3] in tags:
                        voc_list.append(row)
                else:
                    voc_list.append(row)
        print(tabulate(voc_list, headers = ['date', '#1', '#2', 'tags']))

    def generate_voc_list(self, tags):
        voc_list = [] 
        with open(self.filename, 'r', encoding = 'utf-8') as f:
             reader = csv.reader(f, delimiter = '|')
             for row in reader:
                 voc_row = VocUnit(row[1], row[2], row[4])    
                 if row[3] in tags:
                    voc_list.append(voc_row)
        return voc_list
