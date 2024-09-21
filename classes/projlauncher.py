from dotenv import load_dotenv

import csv
import os
import time
import webbrowser


class ProjLauncher:
    def __init__(self):
        load_dotenv()
        self.mdir = os.getenv('MDIR')
        self.csv_dir = os.path.join(self.mdir, '_csv', self.__class__.__name__.lower())
        self.csvfiles = os.listdir(os.path.join(self.csv_dir))
        self.favlist_csv = self.load_favlist()
        self.select_menu = {
            0 : ['HUB', os.getenv('ERPURL_HUB'),],
            1 : ['DASHBOARD', os.getenv('ERPURL_DASHB'),],
            2 : ['GL', os.getenv('ERPURL_GL'),],
            3 : ['SETTINGS', os.getenv('ERPURL_SETTINGS'),],
            }


    def load_favlist(self):
        # loads the shortcuts for project codes
        filename = self.csvfiles[0] # index for favlist
        result = {}
        with open(os.path.join(self.csv_dir, filename), 
                  'r', encoding='utf-8-sig',) as cf:
            data = csv.reader(cf)
            result = {i:v for  i, v in enumerate(data)}
            return result

    def check_rq(self, user_input):
        if user_input.lower() == 'r':
            print('launching reports module')
            # webbrowser.open(os.getenv('ERPURL_REP'))
            time.sleep(0.3)
            exit()
        elif user_input.lower() == 'q':
            print('exiting...')
            time.sleep(0.3)
            exit()
        else:
            return

    def menu_printer(self, menu_toprint):
        for i, v in menu_toprint.items():
            print('{}: {}'.format(i, v[0]))
        print('--------------------')
        return
     
    def launch_proj(self,menu_url, projcode):
        # return webbrowser.open(menu_url.format(str(projnum)))
        print('launching {} for proj {}'.format(menu_url, projcode))
        return

    def start_launcher(self):
        print('\n---- MAIN MENU -----\n')
        time.sleep(0.5)
        print('project shortcut list:\n')
        self.menu_printer(self.favlist_csv)
        projindex = input('Please select proj index option or:\n' \
                             '"r" to launch reports module or\n' \
                             '"q" to exit\n'
                             )
        try:
            self.check_rq(projindex)
            projcode = self.favlist_csv[int(projindex)][0]
            print('chosen proj index: {}'.format(projcode))
            time.sleep(0.3)
            while True:
                self.menu_printer(self.select_menu)
                menu_index = input('Please select menu index option or:\n' \
                                    '"r" to launch reports module or\n' \
                                    '"q" to exit\n'
                                    )
                
                try:
                    self.check_rq(menu_index)
                    self.launch_proj(self.select_menu[int(menu_index)][1], projcode)
                    exit()
                except Exception as E:
                    print('{}\nPlease enter valid index\n'.format(E))
                    continue

        except Exception as E:
            print('{}\nplease enter valid index!'.format(E))
            self.start_launcher()


def main():
    pj = ProjLauncher()
    pj.start_launcher()
    
if __name__ == '__main__':
    main()

