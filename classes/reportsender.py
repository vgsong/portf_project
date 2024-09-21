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
        self.send_mapp = {
            1: ['A','proj_a_distr.csv', [0,1,2,3,4],],
            2: ['B','proj_b_distr.csv', [0,2,4],],
            3: ['C','proj_c_distr.csv', [2,4],],
            }  


    def get_contact_list(self):
        with open(os.path.join(self.csv_dir, self.csv_files[0]), 'r', encoding='utf-8-sig') as cf:
            data = csv.reader(cf)
            _, *result = [x for x in data]  # Excludes header on [0] index
            return result

    def start_sendreport(self):
        for i, v in self.send_mapp.items():
            to_list = []
            cc_list = []

            if self.weekday_today in v[2]:

                for x in self.contact_list:

                    if v[0] in x[1] and x[2] == 'TO':
                        to_list.append(x)
                    if v[0] in x[1] and x[2] == 'CC':
                        cc_list.append(x)

                att_dir = os.path.join(self.att_dir, x[1])
                today_date = self.today_timestamp.strftime('%Y%m%d')

                olapp = Dispatch('Outlook.Application')
                olmail = olapp.CreateItem(0)

                olmail.To = ';'.join(to_list)
                olmail.Cc = ';'.join(cc_list)
                olmail.Subject = 'WEEKLY DISTRIBUTION GROUP {} Rundate {}'.format(v[0], today_date)
                olmail.Attachments.Add(att_dir) 
                olmail.HTMLBody = f'Hi -- <br><br>' \
                                  f'Please see attached for GROUP {v[0]} weekly distribution report <br><br>' \
                                  f'Let me know if you have any questions'
                
                olmail.Display(False)
                time.sleep(0.5)
        return
    
    def start_menu(self):
        while True:
            print('\n----- MAIN MENU ------\n')
            for i, v in self.menu_mapp.items():
                print('{}: {}'.format(i, v[0]))
            user_input = input('Please select menu index number:\n')
            try:
                self.menu_mapp[int(user_input)][1]()
            except Exception as E:
                print(E)
                continue

def main():
    rs = ReportSender()
    rs.start_menu()

if __name__ == '__main__':
    main()

