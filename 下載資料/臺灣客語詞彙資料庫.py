from bs4 import BeautifulSoup
from csv import DictWriter
from os import makedirs, listdir
from os.path import join, dirname, abspath, basename
from urllib.parse import urljoin, quote
from urllib.request import urlopen
from xlrd import open_workbook


class 臺灣客語詞彙資料庫:
    xls網址 = 'http://wiki.hakka.gov.tw/download-word.aspx'

    def __init__(self):
        self.專案目錄 = join(dirname(abspath(__file__)), '..')
        self.原始檔資料夾 = join(self.專案目錄, 'raw')
        self.合併原始csv = join(self.專案目錄, '合併', '原始.csv')
        self.合併網址csv = join(self.專案目錄, '合併', '網址.csv')

    def 下載xls(self):
        makedirs(self.原始檔資料夾, exist_ok=True)
        with urlopen(self.xls網址, timeout=10) as 網頁資料:
            網頁結構 = BeautifulSoup(網頁資料.read().decode('utf-8'), 'lxml')
            for 連結 in 網頁結構.findAll("a", {"class": "txt18px_RoyalPurple_Bold"}):
                xls檔案網址 = urljoin(self.xls網址, quote(連結['href']))
                with urlopen(xls檔案網址, timeout=10) as xls網路資料:
                    with open(join(self.原始檔資料夾, basename(連結['href'])), 'wb') as xls實體檔案:
                        xls實體檔案.write(xls網路資料.read())

    def xls合做一隻csv(self):
        makedirs(dirname(self.合併原始csv), exist_ok=True)
        with open(self.合併原始csv, 'w') as csv檔案:
            欄位名 = ['序號', '索引鍵', '客家語言', '等級', '腔調', '類別',
                   '客語音標', '華語辭義(限100字)', '英語詞義(限200字)', '客語例句', '華語翻譯']
            資料檔案 = DictWriter(csv檔案, fieldnames=欄位名)
            資料檔案.writeheader()
            for 檔名 in sorted(listdir(self.原始檔資料夾), key=lambda s: s[::-1]):
                if 檔名.endswith('.xls'):
                    with open_workbook(join(self.原始檔資料夾, 檔名)) as 檔案:
                        資料表 = 檔案.sheets()[0]
                        目錄 = {}
                        for 第幾隻, 標題 in enumerate(資料表.row_values(0)):
                            目錄[第幾隻] = 標題.strip()
                        目錄 = 資料表.row_values(0)
                        for 第幾列 in range(1, 資料表.nrows):
                            資料 = {}
                            for 第幾隻, 內容 in enumerate(資料表.row_values(第幾列)):
                                資料[目錄[第幾隻]] = 內容.strip()

                            資料檔案.writerow(資料)

if __name__ == '__main__':
    詞彙資料庫 = 臺灣客語詞彙資料庫()
    詞彙資料庫.下載xls()
    詞彙資料庫.xls合做一隻csv()
