from datetime import datetime
import csv
from os.path import isfile
from voc import VocUnit 
from tabulate import tabulate

class User:
    def __init__(self, my_str):
        self.name = my_str
        self.filename = f'data/{self.name}.csv'
        if isfile(self.filename):
            with open(self.filename, 'w'):
                pass

    def get_voc_size(self):
        with open(self.filename, 'r') as f:
            return len(f.readlines())

    def does_voc_unit_exist(self, voc_unit):
        with open(self.filename, 'r') as f:
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                    if row[1] == voc_unit.string1 and row[2] == voc_unit.string2:
                        return True
        return False

    def display_voc(self):
        with open(self.filename, 'r') as f:                                            
            reader = csv.reader(f, delimiter = '|')
            for row in reader:
                print(row)

    def add_voc_unit(self, voc_unit):
        v = voc_unit        
        if self.does_voc_unit_exist(v.string1):
            print(f'There is already such a record.')
            return False
        
        if not v.tags:
            record = [datetime.now(i).strftime('%Y%m%d'), \
                      v.string1, \
                      v.string2, \
                      '']
        else:
            record = []
            for tag in v.tags:
                record += [datetime.now().strftime('%Y%m%d'), \
                           v.string1, \
                           v.string2, \
                           tag]
        
        with open(self.filename, 'w', encoding = 'utf-8') as f:
                writer = csv.writer(f, delimiter = '|')
                for e in record:
                    writer.writerow(e)

