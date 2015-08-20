from csv import DictReader
from os.path import join, dirname, abspath
import re


class 漢字音標處理:
    pass

if __name__=='__main__':
    a=set()
    
    _專案目錄 = join(dirname(abspath(__file__)), '..')
    with open(join(_專案目錄,'合併','原始.csv')) as 檔案:
        for 一筆 in DictReader(檔案):
            漢字,音標=一筆['客家語言'],一筆['客語音標']
#             if '【' not in 音標 and '﹙' not in 音標 and '（' not in 音標 and '〈' not in 音標 and '(' in 音標:
#             if '.'  in 音標:
            print("('{}','{}')".format(漢字,音標))
            for b in 音標:
                if not re.match('[a-zA-Z]',b):
                    a.add(b)
                
    print(a)
    {'）', '+', '﹙', '/', '【', '，', '\u3000', '、', '（', '^', ']', '…', 'ˇ', ' ', 'ˆ', '.', '〉', '〈', '】', '\n', '(', '﹚', '`', ',', '／', '；', 'ˊ', 'ˋ', ')'}
