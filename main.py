from dotenv import load_dotenv
from classes.emplookup import EmpLookup
from classes.pdfmerger import PdfMerger
from classes.projlauncher import ProjLauncher
from classes.reportsaver import FromDl
from classes.reportsender import ReportSender

import os

class MainLauncher:
    def __init__(self):
        load_dotenv()

        self.mdir = os.getenv('MDIR')

        self.menu_mapp = {
            # 1: ['EMPLOOKUP', self.],
            # 2: ['PDFMERGER', self.],
            # 3: ['HUBLAUNCH', self.],
            # 4: ['REPORTSAVER', self.],
            # 5: ['REPORTSENDER', self.],
            0: ['QUIT', exit],
        }

    
    def start_menu(self):
        while True:
            print('------- MAIN MENU -------')
            for k, v in self.menu_mapp.items():
                print('{}: {}'.format(k, v[0]))
            user_input = input('Please select index\n')
            try:
                self.menu_mapp[int(user_input)][1]()
            except Exception as E:
                print(E)

        
def main():
    mainlauncher = MainLauncher()
    mainlauncher.start_menu()

if __name__ == '__main__':
    main()

