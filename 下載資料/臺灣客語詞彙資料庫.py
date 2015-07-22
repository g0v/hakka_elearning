from bs4 import BeautifulSoup
from collections import OrderedDict
from csv import DictReader
import json
from os import makedirs
from os.path import join, dirname, abspath, basename
from random import random
import re
from time import sleep
from urllib.parse import urljoin, quote
from urllib.request import urlopen


class 臺灣客語詞彙資料庫:
    xls網址 = 'http://wiki.hakka.gov.tw/download-word.aspx'

    def __init__(self):
        self.專案目錄 = join(dirname(abspath(__file__)), '..')

    def 下載xls(self):
        目標資料夾 = join(self.專案目錄, 'raw')
        makedirs(目標資料夾, exist_ok=True)
        with urlopen(self.xls網址, timeout=10) as 網頁資料:
            網頁結構 = BeautifulSoup(網頁資料.read().decode('utf-8'), 'lxml')
            for 連結 in 網頁結構.findAll("a", {"class": "txt18px_RoyalPurple_Bold"}):
                xls檔案網址 = urljoin(self.xls網址, quote(連結['href']))
                with urlopen(xls檔案網址, timeout=10) as xls網路資料:
                    with open(join(目標資料夾, basename(連結['href'])), 'wb') as xls實體檔案:
                        xls實體檔案.write(xls網路資料.read())

if __name__ == '__main__':
    詞彙資料庫 = 臺灣客語詞彙資料庫()
    詞彙資料庫.下載xls()
