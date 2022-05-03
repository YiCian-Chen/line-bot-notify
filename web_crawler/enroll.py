import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
user_agent = UserAgent()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Host": "enroll.tku.edu.tw",  # 目標網站
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": user_agent.random,  # 使用者代理
    "Referer": "https://www.google.com/"  # 參照位址
}
request = requests.get('http://enroll.tku.edu.tw/', headers=header)
html = BeautifulSoup(request.text, 'html.parser')
tr = html.find_all(class_='odd')

for i in tr:
    left = i.find_all(align='left')
    center = i.find_all(align='center')
    Event_name = left[0].text
    organizer = left[1].text
    url = 'http://enroll.tku.edu.tw/' + left[0].a['href']
    person = center[2].text
    print(Event_name)
    print(organizer)
    print(url)
    print(person)

    # request = requests.get(url)
    # html = BeautifulSoup(request.text, 'html.parser')
    # info = html.find(id='info')
    # print(info.text)#問題:無法將全部內容截取出來
'''
<tr class="odd"> 
    <td align="center">1</td> 
    <td align="center">2022-05-04<br/>2022-05-19</td> 
    *<td align="left"><a href="course.aspx?cid=askx2022050401" target="_blank">
        【生活X香氣】-精油手作，找尋屬於你的療癒香氣(名額釋出)</a><br/></td>
    <td align="center"><span class="font_s lineheight_s">學生<br/></span></td> 
    <td align="center">2022-04-29<br/>2022-05-04</td>
    *<td align="left"><span class="font_s lineheight_s">諮商職涯暨學習發展輔導中心</span></td>
    <td align="center"><a href="signup.aspx?m=local&amp;cid=askx2022050401" 
        target="_blank">校內報名</a>額滿</td>
</tr>
'''
'''
<div id = "info" > <h3 > 活動內容：< /h3 > <p > 1.課程內容
<br > (1)管理工作簿選項和設定
<br > (2)管理和格式化資料
<br > (3)創建進階公式和巨集
<br > (4)管理進階圖表和表格
<br > 2.課程資訊：
<br > (1)上課時間：5/22(日)9: 00~12: 00、13: 00~16: 00
<br > (2)考試時間：5/22 (日)16: 00~17: 00
<br >
<br > (3)報名費用：1, 600元。(原價 2, 980元)
<br > (4)名    額：50名
<br > (5)上課地點：B1012電腦教室
<br >
<br > 3.報名網址： http: // enroll.tku.edu.tw/course.aspx?cid = askx20220522
<br > 4.報名時間：5/2(一)21: 00
<br >
<br > 備註：
<br > 1.審核繳費名單於5/6(五)12: 00依報名順序公告於報名網頁附加檔案處。
<br > 2.保證金繳費時間：5/9(一)及5/10(二)08: 00~12: 00、13: 00~16: 00
<br > 3.逾時繳費不予受理，並將名額由備取遞補，若無法前來繳費，可請同學協助代繳或於繳費截止時間前來電或來信保留繳費名額。
<br > 4.繳費時請自備整數費用，恕不找零。
<br > 5.繳費地點：諮輔中心B413辦公室
<br > 6.若疫情嚴峻，學校採全校遠距授課，該課程會異動為線上課程。< /p > <h3 > 活動時間：< /h3 > <p > 2022/05/22 09: 00 ~ 2022/05/22 17: 00 < /p > <h3 > 報名時間：< /h3 > <p > 2022/05/02 21: 00 ~ 2022/05/05 12: 00 < /p > <h3 > 活動地點：< /h3 > <p > 商管大樓 B1012 < /p > <div > <span class = 'inline' > 活動時數：< /span > 7.0 小時 < /div > <div > <span class = 'inline' > 報名人次上限：< /span > 65 名 < span class = 'msg' > (額滿) < /span > </div > <div > <span class = 'inline' > 預估錄取名額：< /span > 50 名 < /div > <div > <span class = 'inline' > 活動對象：< /span > 教師、學生、職員 < /div > <br > <br > </div >
'''
