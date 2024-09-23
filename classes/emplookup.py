from dotenv import load_dotenv

import csv
import os


class EmpLookup:
    def __init__(self):
        load_dotenv()
        self.mdir = os.getenv('MDIR')
        self.csv_dir = os.path.join(self.mdir, 'csv', self.__class__.__name__.lower())
        self.csvfiles = os.listdir(os.path.join(self.csv_dir))
        self.emplist = self.get_emplist()


    def get_emplist(self):
        with open(os.path.join(self.csv_dir, self.csvfiles[0]), 
                  'r', encoding='utf-8-sig') as cf:
            data = csv.reader(cf)
            return [row for row in data]

    def start_lookup(self):
        headers, *details = self.emplist
        while True:
            user_input = input('Search by first or last name\n').lower()
            if user_input == 'q':
                exit()
            else:
                search_result = [row for row in details if user_input in row[1].lower() or user_input in row[2].lower()]
                break
        
        for emp in search_result:
            empinfo = {
                    'empid' : str(emp[0]),
                    'first' : str(emp[1]),
                    'last' : str(emp[2]),
                    'email' : str(emp[3]),
                    'gender' : str(emp[4]),
                    'department' : str(emp[5]),
                    'title' : str(emp[6]),
                    'salary' : str(emp[7]),
                    'hiredate' : str(emp[8]),
                    }

            print('--------------------------')
            for k, v in empinfo.items():
                print('{}: {}'.format(k, v))        
            print('--------------------------\n')


def main():
    a = EmpLookup()
    a.start_lookup()

if __name__ == '__main__':
    main()

