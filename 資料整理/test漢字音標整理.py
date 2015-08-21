from unittest.case import TestCase


class 漢字音標處理(TestCase):

    def 整理(self, 來源資料, 答案):
        漢字, 音標 = 來源資料
        處理 = 漢字音標處理()
        self.assertEqual(
            處理.整理對照漢字音標(漢字, 音標),
            答案
        )

    def test_一般(self):
        self.整理(
            ('本土化', 'bunˊ  tuˊ  faˇ'),
            [
                ('本土化', 'bunˊ tuˊ faˇ'),
            ]
        )

    def test_全形空白(self):
        self.整理(
            ('艾粄', 'ngieˇ　banˊ'),
            [
                ('艾粄', 'ngieˇ banˊ'),
            ]
        )

    def test_全形小括號(self):
        self.整理(
            ('千一(一千一百)', 'cien+ rhid^﹙rhid^ cien+ rhid^ bag^﹚'),
            [
                ('千一', 'cien+ rhid^'),
                ('一千一百', 'rhid^ cien+ rhid^ bag^'),
            ]
        )

    def test_全形小括號有頓號(self):
        self.整理(
            ('門牙(當門牙、前牙)', 'munˇngaˇ﹙dongˊmunˇngaˇ、qienˇngaˇ﹚'),
            [
                ('門牙', 'munˇngaˇ'),
                ('當門牙', 'dongˊmunˇngaˇ'),
                ('前牙', 'qienˇngaˇ'),
            ]
        )

    def test_有對應小括號(self):
        self.整理(
            ('同學（讀書伴、同窗）', 'tung hogˋ（tugˋ shuˋ panˋ、tung chungˋ）'),
            [
                ('同學', 'tung hogˋ'),
                ('讀書伴', 'tugˋ shuˋ panˋ'),
                ('同窗', 'tung chungˋ'),
            ]
        )

    def test_有對應小括號取代部份(self):
        self.整理(
            ('鄉（鎮、市、區）公所', 'hiongˋ（ zhinˊ、shi+、  kiˋ）gungˋ soˊ'),
            [
                ('鄉公所', 'hiongˋ gungˋ soˊ'),
                ('鎮公所', 'zhinˊ gungˋ soˊ'),
                ('市公所', 'shi+ gungˋ soˊ'),
                ('區公所', 'kiˋ gungˋ soˊ'),
            ]
        )

    def test_孤字音標有粗括(self):
        self.整理(
            ('鉛', 'ienˇ【ianˇ】'),
            [
                ('鉛', 'ienˇ'),
                ('鉛', 'ianˇ'),
            ]
        )

    def test_雙字音標有粗括(self):
        self.整理(
            ('應酬', 'in  cuˇ【in suˇ】'),
            [
                ('應酬', 'in  cuˇ'),
                ('應酬', 'in suˇ'),
            ]
        )

    def test_漢字音標攏有粗括(self):
        self.整理(
            ('嗋石【吸石】', 'hiab sag【kibˋ sag】'),
            [
                ('嗋石', 'hiab sag'),
                ('吸石', 'kibˋ sag'),
            ]
        )

    def test_音標粗括有斜線重覆音(self):
        self.整理(
            ('紫外線', 'ziiˋngoi  xien【ziiˋ/jiˋngoi  xien】'),
            [
                ('紫外線', 'ziiˋ ngoi xien'),
                ('紫外線', 'jiˋ ngoi xien'),
            ]
        )

    def test_音標粗括另外詞有斜線(self):
        self.整理(
            ('腦屎【腦屎漿】', 'noˋsiiˋ【noˋsiiˋ/xiˋjiongˊ】'),
            [
                ('腦屎', 'noˋsiiˋ'),
                ('腦屎漿', 'noˋsiiˋ'),
                ('腦屎漿', 'xiˋjiongˊ'),
            ]
        )

    def test_有細括佮粗括(self):
        self.整理(
            ('響哨笐(響笐仔)【響角】', 'hiongˋ sau gongˇ(hiongˋ gongˇeˋ)【hiongˋgogˋ】'),
            [
                ('響哨笐', 'hiongˋ sau gongˇ'),
                ('響笐仔', 'hiongˋ gongˇeˋ'),
                ('響角', 'hiongˋgogˋ'),
            ]
        )

    def test_有細括佮粗括有斜線(self):
        self.整理(
            ('調單(徵集令)', 'diau danˊ(ziinˊ  xib  lin)【ziinˊ/jinˊ  xib  lin】'),
            [
                ('調單', 'diau danˊ'),
                ('徵集令', 'ziinˊ  xib  lin'),
                ('徵集令', 'jinˊ  xib  lin'),
            ]
        )

    def test_有粗括有斜線和頓號(self):
        self.整理(
            ('瓦斯', 'ngaˋsiiˊ【ngaˋsiiˊ/xiˊ、ga siiˋ】'),
            [
                ('瓦斯', 'ngaˋsiiˊ'),
                ('瓦斯', 'ngaˋ xiˊ'),
                ('瓦斯', 'ga siiˋ'),
            ]
        )

    def test_粗括內有細括(self):
        self.整理(
            ('白鐡(白鐡仔)', 'pag tiedˋ(pag tiedˋeˇ)【(pag tiedˋeˋ)】'),
            [
                ('白鐡', 'pag tiedˋ'),
                ('白鐡仔', 'pag tiedˋeˇ'),
                ('白鐡仔', 'pag tiedˋeˋ'),
            ]
        )

    def test_漢字音標有粗括和頓號(self):
        self.整理(
            ('斗換【轉換、交換】', 'deuˋvon【zonˋvon、gauˊvon】'),
            [
                ('斗換', 'deuˋvon'),
                ('轉換', 'zonˋvon'),
                ('交換', 'gauˊvon'),
            ]
        )

    def test_音標斜線代表完整的詞(self):
        self.整理(
            ('支出', 'ziiˊcudˋ/ giˊcudˋ【ziiˊ/jiˊcudˋ】'),
            [
                ('支出', 'ziiˊcudˋ'),
                ('支出', 'giˊcudˋ'),
                ('支出', 'jiˊcudˋ'),
            ]
        )

    def test_雙斜線(self):
        self.整理(
            ('執政', 'ziibˋ  ziin【ziibˋ/jibˋ  ziin/jin】'),
            [
                ('執政', 'ziibˋ  ziin'),
                ('執政', 'jib jin'),
            ]
        )

    def test_特殊括號(self):
        self.整理(
            (
                '喊頭大雨(浩洪斗雨、喊盆大雨 〉',
                'hemˇteu taiˋ vuˋ(hauˇ fung  deuˋ vuˋ、hemˇpun taiˋvuˋ〉〈 hemˇpunˋtai  vu^、 hemˇteuˋtai vu^〉'
            ),
            [
                ('喊頭大雨', 'hemˇteu taiˋ vuˋ'),
                ('浩洪斗雨', 'hauˇ fung  deuˋ vuˋ'),
                ('喊盆大雨', 'hemˇpun taiˋvuˋ'),
                ('hemˇpunˋtai  vu^', None),
                ('hemˇteuˋtai vu^', None),
            ]
        )

    def test_用括號代替斜線(self):
        self.整理(
            ('畫圖', 'fa+ (vagˋ) tu'),
            [
                ('畫圖', 'fa+ tu'),
                ('畫圖', 'vagˋ tu'),
            ]
        )

    def test_用斜線邊仔有空白(self):
        self.整理(
            ('畫圖', 'faˋ / vagˋtuˇ'),
            [
                ('畫圖', 'faˋ+ tuˇ'),
                ('畫圖', 'vagˋtuˇ'),
            ]
        )

    def test_外來語無對應漢字(self):
        self.整理(
            ('鋁', 'liˋ(a+ lu miˋ)'),
            [
                ('鋁', 'liˋ'),
                ('a+ lu miˋ', None),
            ]
        )

    def test_分號代替頓號(self):
        self.整理(
            ('妻舅姆(妻舅姆仔、舅姆仔)', 'qiˊkiuˊmeˊ(qiˊkiuˊmeˊeˋ；kiuˊmeˊeˋ)'),
            [
                ('妻舅姆', 'qiˊkiuˊmeˊ'),
                ('妻舅姆仔', 'qiˊkiuˊmeˊeˋ'),
                ('舅姆仔', 'kiuˊmeˊeˋ'),
            ]
        )

    def test_逗號代替頓號(self):
        self.整理(
            ('麼个位所(哪，哪位)', 'maˋgaiˇ vui+ soˊ(nai+,nai+ vui+)'),
            [
                ('麼个位所', 'maˋgaiˇ vui+ soˊ'),
                ('哪', 'nai+'),
                ('哪位', 'nai+ vui+'),
            ]
        )

    def test_全形斜線代表全詞(self):
        self.整理(
            ('下晝', 'haˋ zhiuˋ／ ha+ zhiuˋ'),
            [
                ('下晝', 'haˋ zhiuˋ'),
                ('下晝', 'ha+ zhiuˋ'),
            ]
        )

    def test_全形斜線代表全詞合音(self):
        self.整理(
            ('無愛', 'moˇoiˋ／ moiˊ'),
            [
                ('無愛', 'moˇoiˋ／ '),
                ('moiˊ', None),
            ]
        )

    def test_加出來的全形斜線(self):
        self.整理(
            ('唱卡拉OK', 'chongˋ／ kaˇ la+ o+ kie+'),
            [
                ('唱卡拉 O K', 'chongˋ kaˇ la+ o+ kie+'),
            ]
        )

    def test_多出來的點(self):
        self.整理(
            ('頭那頂', 'teu  na denˋ【teuˋ naˋ.denˇ】'),
            [
                ('頭那頂', 'teu na denˋ'),
                ('頭那頂', 'teuˋ naˋ denˇ'),
            ]
        )

    def test_句型用句點代替刪節號(self):
        self.整理(
            ('毋單...猶過', 'mˋ danˇ ...ia  goo'),
            [
                ('毋單...猶過', 'mˋ danˇ … ia goo'),
            ]
        )

    def test_句型刪節符號(self):
        self.整理(
            ('毋單淨…還', 'm danˋciang+…han'),
            [
                ('毋單淨…還', 'm danˋ ciang+ … han'),
            ]
        )

    def test_多的符號要拿掉(self):
        self.整理(
            ('發', 'bod  hab'),
            [
                ('發', 'bod hab'),
            ]
        )
