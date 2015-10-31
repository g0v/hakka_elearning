# 客語能力認證資料檔

## 資料來源
* 臺灣客話詞彙資料庫
  * xls、HTML和mp3
  * 102年版教材
  * [xls](http://wiki.hakka.gov.tw/download-word.aspx)
  * html跟mp3：<http://wiki.hakka.gov.tw/search-detail.aspx?param=N>, 72338<=N<=118502
* 哈客網路學院教材
  * PDF檔和mp3
    * 每個mp3檔有10句語料
  * 每年更新
  * [初級](http://elearning.hakka.gov.tw/Kaga/Kaga_QDPrimary.aspx)
  * [中高級](http://elearning.hakka.gov.tw/Kaga/Kaga_QDMiddle.aspx)
* 哈客網路學院線上學習
  * HTML檔和mp3
    * mp3跟
  * 102年版
  * [初級](http://elearning.hakka.gov.tw/Kaga/wikiwords1.aspx)
  * [中高級](http://elearning.hakka.gov.tw/Kaga/wikiwords2.aspx)
  
  
## 下載語料
```
sudo apt-get install -y python3 python-virtualenv g++ libxml2-dev libxslt-dev python-dev
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
python 下載資料/臺灣客語詞彙資料庫.py 
```

* `合併/原始.csv`是合併臺灣客話詞彙資料庫全部的xls
* `合併/網站詞目.csv`是臺灣客話詞彙資料庫網頁上的資料

兩個檔除了少部份（14條）詞目不同外，`合併/網站詞目.csv`多包含外來語。

針對`合併/網站詞目.csv`處理造字，並轉出`網站詞目補造字.csv`。

## 產生資料庫格式
在使用`臺灣言語資料庫`的專案目錄下
```bash
sudo apt-get install -y python3 python-virtualenv
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
python 轉到臺灣言語資料庫/整合到資料庫.py
```
會產生`臺灣客話詞彙資料庫語料.yaml`語料檔

## 匯入臺灣言語資料庫
```bash
python manage.py 匯入資料 https://Taiwanese-Corpus.github.io/hakka_elearning/臺灣客話詞彙資料庫語料.yaml
```

## 開發試驗
在`hakka_elearning`專案目錄下
```
sudo apt-get install -y python-virtualenv g++ libxml2-dev libxslt-dev python-dev
virtualenv --python=python3 venv
. venv/bin/activate
python -m unittest 
```

