from datetime import datetime
from dotenv import load_dotenv

import os
import PyPDF2


class PdfMerger:
    def __init__(self):
        load_dotenv()

        self.mdir = os.getenv('MDIR')
        self.timestamp = datetime.today().strftime('%Y%m%d')
        self.merge_dir = os.path.join(self.mdir, 'pdf', self.__class__.__name__.lower())
        self.todo_list = self.get_tomerge_files()


    def get_tomerge_files(self):
        return [[x for x in os.listdir(os.path.join(self.merge_dir, 'tomerge'))]]
        
    def start_merger(self):
        dir_to_check = os.path.join(self.merge_dir, 'merged', self.timestamp)
        if os.path.isdir(dir_to_check):
            merger = PyPDF2.PdfFileMerger(strict=False)
            for x in self.todo_list:
                pdfile = PyPDF2.PdfFileReader(open(os.path.join(self.merge_dir, 'tomerge', x)))
                merger.append(pdfile)
            merger.write(os.path.join(dir_to_check, 'MERGED_{}.pdf'.format(self.timestamp)))
        else:
            os.mkdir(os.path.join(dir_to_check))
            print('dir created for {}'.format(self.timestamp))
            self.start_merger()

def main():
    pd = PdfMerger()
    pd.start_merger()

if __name__ == '__main__':
    main()
