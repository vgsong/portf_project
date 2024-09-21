from datetime import datetime
from dotenv import load_dotenv
from win32com.client import Dispatch

import csv
import os
import time

class ReportSender:
    def __init__(self):
        load_dotenv()
        self.today_timestamp = datetime.today()
        self.weekday_today = self.today_timestamp.weekday()
        self.mdir = os.getenv('MDIR')
        self.csv_dir = os.path.join(self.mdir,'_csv', self.__class__.__name__.lower())
        self.csv_files = [x for x in os.listdir(self.csv_dir) if os.path.isfile(os.path.join(self.csv_dir,x))]
        self.contact_list = self.get_contact_list()

        self.att_dir = os.path.join(self.csv_dir, 'attachments')

        # index: ['TITLE', 'CALLBACK']
        self.menu_mapp = {
            1: ['SEND REPORTS', self.start_sendreport],
            0: ['QUIT', exit],
            }
        # index: ['GROUPNAME','FILENAME',[WEEKDAY]]
        self.contact_mapp = {
            1: ['A','proj_a_distr.csv',[0,1,2,3,4]],
            2: ['B','proj_b_distr.csv',[0,2,4]],
            3: ['C','proj_c_report.csv',[2]],
            }  


    def get_contact_list(self):
        with open(os.path.join(self.csv_dir, self.csv_files[0]), 'r', encoding='utf-8-sig') as cf:
            data = csv.reader(cf)
            _, *result = [x for x in data]  # Excludes header on [0] index
            return result

    def start_sendreport(self):
        return
        # for i, v in self.contact_mapp.items():
        #     if self.weekday_today in v[2]:


def main():
    pj = ReportSender()
    result = []
    for x in pj.contact_list:
        if 'A' in x[1] and x[2] == 'TO':
            result.append(x)
    print(result)

if __name__ == '__main__':
    main()
