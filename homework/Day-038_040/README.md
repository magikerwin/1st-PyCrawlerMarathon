## 1. Collect 500+ news from [Cupoy News](https://www.cupoy.com/newsfeed/topstory).
- Use selenium for dynamic website.

| No | Title |	Url | Introduction |
| ---------| --------| ---------| ---------|
|0	|《就愛斷捨離》線上看影評：想靠「斷捨離」整理人生，卻為何狠狠傷害了所愛之人？-風傳媒	|https://www.storm.mg/lifestyle/2313545|	《模犯生》天才少女「小琳」魅力再度征服大銀幕｜《把哥哥退貨可以嗎》廢柴哥哥「桑尼」化身天菜前...|
|1	|武漢肺炎風暴》山東、浙江爆發監獄羣聚感染！司法廳長、監獄長免職，中國病例16連降破功-風傳媒	|https://www.storm.mg/article/2317402	|中國國家衛健委21日上午公佈武漢肺炎（新冠肺炎）最新數據統計，顯示20日全國除湖北以外地區新...
|2	|武漢肺炎風暴》中國驚傳「治癒」病例10天後二度感染病毒！-風傳媒	|https://www.storm.mg/article/2317847	|中國爆發的布武漢肺炎（新冠肺炎）疫情詭譎，《人民日報》21日報導，四川成都一名患者治癒後，回...
|3	|咳嗽流鼻水1個月，就醫才說曾和檢疫者「聊天」　醫師嘆：宣導還不夠嗎？-風傳媒	|https://www.storm.mg/article/2317650	|武漢肺炎（新冠肺炎）疫情延燒，臺灣目前已有26例確診病例，如何有效防疫也成為全民關注焦點。不...
|4	|公主號臺籍旅客下船了！魔術師陳日昇驚險取得檢驗報告　卡關原因曝光-風傳媒	|https://www.storm.mg/article/2317594	|爆發嚴重武漢肺炎（新冠肺炎）疫情的日籍郵輪「鑽石公主號」近日解除隔離，旅客紛紛開始下船，而臺...
|5	|武漢肺炎又增兩例　24例的女兒、孫女確診-風傳媒	|https://www.storm.mg/article/2317499	|中央流行疫情指揮中心今（21）日公佈新增2例武漢肺炎（新冠肺炎，COVID-19）病例，為案...
|6	|「江子翠」是誰？憑什麼捷運站用他命名？揭祕90％臺灣人都不知道的5個「寶島日常」-風傳媒	|https://www.storm.mg/lifestyle/887483	|生活中處處可見被大眾「遺忘」的迷思，這類迷思偏向生活中的「冷知識」，不知道並不影響生活，但卻...
|7	|中研院發現肺腺癌的致命基因，宛如犯罪者聯盟 - TechNews 科技新報	|https://technews.tw/2020/02/21/integrative-ana...	|肺腺癌患者逐年增加，中央研究院 20 日指出，肺腺癌組織的非編碼核糖核酸「PTTG3P」表現...
|8	|研究：吸食大麻者更容易產生錯誤記憶 - TechNews 科技新報	|https://technews.tw/2020/02/20/cannabis-can-ma...	|每個人可能都有過「錯誤記憶」的情況，誤以為自己記憶中是曾經發生過的事，但這種情況可能在一些人...
|9	|【每 15 分鐘就有一位女性遭性侵】為何即使判性侵犯「絞刑」，仍無法解決印度的社會問題？ |https://buzzorange.com/2020/02/21/sexual-assau...	|【我們為什麼選擇這篇文章？】 全球的女權意識逐漸上升，但印度的女性權益卻不見成長。印度內政部...
| ...| ...| ...| ...|
## 2. Extract and save 500+ news.
- Use requests for static website.
- Save website content on external txt.

## 3. Get top-50 keywords for each new.
- Ignore nonsense words using [jieba](https://github.com/fxsjy/jieba). (ex. 能夠, 建議, 相當, 18, 15, 每個, 顯示, 相關, ...)

## 4. Count all keywords.
| Keyword  | Count   |
| ---------| --------|
|2020| 106|
|台灣|	99|
|中國|	82|
|疫情|	73|
|武漢|	71|
|肺炎|	68|
|美國|	55|
|網站|	52|
|報導|	49|
|2019|	47|
|新聞|	38|
|技術|	34|
|口罩|	33|
|病毒|	33|
|防疫|	33|
|電子|	33|
|市場|	33|
|設計|	32|
|人員|	32|
|國家|	31|

## 5. Visualization
- Generate Word Clouds in Python using [wordcloud module](https://amueller.github.io/word_cloud/).

<img src="./wordcloud.png">
