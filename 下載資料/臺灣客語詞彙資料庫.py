from bs4 import BeautifulSoup
from csv import DictWriter, DictReader
import html
from os import makedirs, listdir
from os.path import join, dirname, abspath, basename
from urllib.parse import urljoin, quote
from urllib.request import urlopen
from xlrd import open_workbook
from 資料整理.造字表 import 造字表


class 臺灣客語詞彙資料庫:
    xls網址 = 'http://wiki.hakka.gov.tw/download-word.aspx'
    詞條網址 = 'http://wiki.hakka.gov.tw/search-detail.aspx?param={}'

    def __init__(self):
        self.專案目錄 = join(dirname(abspath(__file__)), '..')
        self.原始檔資料夾 = join(self.專案目錄, 'raw')
        self.合併原始csv = join(self.專案目錄, '合併', '原始.csv')
        self.合併網址csv = join(self.專案目錄, '合併', '網站詞目.csv')
        self.補造字網址csv = join(self.專案目錄, '合併', '網站詞目補造字.csv')

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

    def 下載網頁詞條而且合做一隻csv(self):
        makedirs(dirname(self.合併網址csv), exist_ok=True)
        with open(self.合併網址csv, 'w') as csv檔案:
            欄位名 = [
                '編號', '客家語言', '等級', '腔調', '客語音標',
                '華語辭義(限100字)', '英語詞義(限200字)', '客語音檔網址',
                '客語例句', '華語翻譯', '客語例句網址',
            ]
            資料檔案 = DictWriter(csv檔案, fieldnames=欄位名)
            資料檔案.writeheader()
            這馬編號 = 0
            連紲無效的數量 = 0
            while 連紲無效的數量 < 100000:
                print(這馬編號)
                try:
                    資料 = self.下載網頁詞條(這馬編號)
                    if 資料 is None:
                        連紲無效的數量 += 1
                    else:
                        連紲無效的數量 = 0
                        資料檔案.writerow(資料)
                except Exception as 錯誤:
                    print(錯誤)
                else:
                    這馬編號 += 1

    def 下載網頁詞條(self, 編號):
        with urlopen(self.詞條網址.format(編號), timeout=100) as 網頁資料:
            網頁結構 = BeautifulSoup(
                網頁資料.read().decode('utf-8'), 'lxml')
        資料table = 網頁結構.find_all(
            id='ctl00_ContentPlaceHolder1_FormView1')[0].find('table')
        if 資料table is None:
            return None
        表格資料 = []
        for tr in 資料table.find_all('tr', recursive=False):
            表格資料.append(tr.find_all('td', recursive=False))
        資料 = {}
        資料['編號'] = str(編號)
        資料['客家語言'] = 表格資料[0][1].get_text().strip()
        資料['等級'] = 表格資料[0][2].get_text().strip()
        try:
            資料['腔調'] = 表格資料[2][1].find(
                "input", {'checked': "checked"}
            ).find_next_sibling('label').get_text().strip()
        except AttributeError:
            pass
        資料['客語音標'] = 表格資料[1][1].get_text().strip()
        資料['華語辭義(限100字)'] = 表格資料[3][1].get_text().strip()
        資料['英語詞義(限200字)'] = 表格資料[4][1].get_text().strip()
        資料['客語音檔網址'] = 表格資料[1][2].find(
            "param", {'name': 'FlashVars'}
        )['value'].split('=', 1)[1]
        資料['客語例句'] = 表格資料[5][1].get_text().strip()
        資料['華語翻譯'] = 表格資料[6][1].get_text().strip()
        資料['客語例句網址'] = 表格資料[5][2].find(
            "param", {'name': 'FlashVars'}
        )['value'].split('=', 1)[1]
        return 資料

    def 原始和網站csv合併(self):
        self.合併原始csv = join(self.專案目錄, '合併', '原始.csv')
        欄位名 = [
            '編號', '客家語言', '等級', '腔調', '客語音標',
            '華語辭義(限100字)', '英語詞義(限200字)', '客語音檔網址',
            '客語例句', '華語翻譯', '客語例句網址',
        ]
        造字 = 造字表()
        with open(self.補造字網址csv, 'w') as 輸出:
            資料檔案 = DictWriter(輸出, fieldnames=欄位名)
            資料檔案.writeheader()
            with open(self.合併網址csv) as 輸入:
                for 一筆 in DictReader(輸入):
                    資料 = {}
                    for 欄位, 內容 in 一筆.items():
                        資料[欄位] = html.unescape(
                            造字.換造字(
                                內容
                            )
                        )
                    資料檔案.writerow(資料)


if __name__ == '__main__':
    詞彙資料庫 = 臺灣客語詞彙資料庫()
    詞彙資料庫.下載xls()
    詞彙資料庫.xls合做一隻csv()
    詞彙資料庫.下載網頁詞條而且合做一隻csv()
    詞彙資料庫.原始和網站csv合併()
