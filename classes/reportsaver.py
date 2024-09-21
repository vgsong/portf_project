from datetime import datetime
from dotenv import load_dotenv

import os


class FromDl:
    def __init__(self):
        load_dotenv()
        self.timestamp = datetime.today().strftime('%Y%m%d')
        self.mdir = os.getenv('MDIR')
        self.dl_dir = os.getenv('DL_DIR')
        self.csv_dir = os.path.join(self.mdir, '_csv', self.__class__.__name__.lower())
        self.dailydir = os.path.join(self.csv_dir, self.timestamp)

        self.file_in = ['Project List', 
                        'AR AGED', 
                        'GL MAPP', 
                        ]

    def create_daily_folder(self):
        if not os.path.isdir(self.dailydir):
            os.mkdir(self.dailydir)
            print('dir created for {}'.format(self.timestamp))
        else:
            print('daily {} folder already exist...dir not created'.format(self.timestamp))
        return

    def get_dl_files(self):
        fromdl_dir = os.path.join(self.dailydir)
        

        print(self.get_latest_report('GL MAPP'))
            


        return

    def get_latest_report(self, report_name):
        _ = [os.path.join(self.dl_dir, x) for x in os.listdir(self.dl_dir) if report_name in x]
        return max(_, key=os.path.getctime)
        


def main():
    fd = FromDl()
    fd.get_dl_files()

if __name__ == '__main__':
    main()
