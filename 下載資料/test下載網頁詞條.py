from unittest.case import TestCase
from 下載資料.臺灣客語詞彙資料庫 import 臺灣客語詞彙資料庫


class 下載網頁詞條試驗(TestCase):

    def setUp(self):
        self.詞彙資料庫 = 臺灣客語詞彙資料庫()

    def test_下載一般詞條(self):
        self.assertEqual(
            self.詞彙資料庫.下載網頁詞條(83775),
            {
                '編號': '83775',
                '腔調': '四縣',
                '等級': '初級',
                '客家語言': '頭那',
                '客語音標': 'teuˇ naˇ',
                '客語音檔網址': 'http://wiki.hakka.gov.tw/file/102/si/SI-01_001.mp3',
                '華語辭義(限100字)': '頭',
                '英語詞義(限200字)': 'head',
                '客語例句': '頭那大愛戴較(過)大頂个帽仔。',
                '客語例句網址': 'http://wiki.hakka.gov.tw/file/102/si/SI-01_001s.mp3',
                '華語翻譯': '頭大要戴比較大的帽子。',
            }
        )

    def test_下載空的詞條編號(self):
        self.assertIsNone(
            self.詞彙資料庫.下載網頁詞條(10)
        )

    def test_下載無腔調詞條(self):
        self.assertEqual(
            self.詞彙資料庫.下載網頁詞條(75358),
            {
                '編號': '75358',
                '等級': '外來語',
                '客家語言': '吉普',
                '客語音標': 'zi buˋ',
                '客語音檔網址': 'http://wiki.hakka.gov.tw/file/99_4/li/00047_si.wav',
                '華語辭義(限100字)': '吉普車',
                '英語詞義(限200字)': 'jeep',
                '客語例句': '吾姊丈頭擺做兵係駛吉普个。',
                '客語例句網址': 'http://wiki.hakka.gov.tw/file/99_4/si/s00047_si.mp3',
                '華語翻譯': '我姊夫之前當兵是開吉普車的。',
            }
        )