# 客語能力認證資料檔

## 資料來源
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
* 臺灣客話詞彙資料庫
  * xls、HTML和mp3
  * 102年版教材
  * [xls](http://wiki.hakka.gov.tw/download-word.aspx)
  * html跟mp3：<http://wiki.hakka.gov.tw/search-detail.aspx?param=N>,N>=83775
  
  
##安裝
```
sudo apt-get install -y python-virtualenv g++ libxml2-dev libxslt-dev python-dev
virtualenv --python=python3 venv
. venv/bin/activate
pip install -r requirements.txt
```
  
