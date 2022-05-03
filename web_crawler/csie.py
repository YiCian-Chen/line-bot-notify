import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
user_agent = UserAgent()
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-TW,zh;q=0.9",
    "Host": "www.csie.tku.edu.tw",  # 目標網站
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": user_agent.random,  # 使用者代理
    "Referer": "https://www.google.com/"  # 參照位址
}
request = requests.get('http://www.csie.tku.edu.tw/Front/about/news/News.aspx?id=26J0iyD8bhA=', headers=header)
html = BeautifulSoup(request.text, 'html.parser')
tr = html.find_all('tr')
tr.pop(0)

for i in tr:
    td = i.find_all('td')
    category = td[0].text
    date = td[1].text
    title = td[2].a.text
    url = td[2].a['href']
    print(category)
    print(date)
    print(title)
    print(url)