from datetime import datetime
from dotenv import load_dotenv

import os


class FromDl:
    def __init__(self):
        load_dotenv()

        self.mdir = os.getenv('MDIR')
        self.dl_dir = os.getenv('DL_DIR')
        self.csv_dir = os.path.join(self.mdir, '_csv', self.__class__.__name__.lower(0))
        self.timestamp = datetime.today().strftime('%Y%m%d')

    
    def create_daily_folder(self):



def main():
    fd = FromDl()
    fd.timestamp

if __name__ == '__main__':
    main()
