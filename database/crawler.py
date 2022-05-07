import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class Crawler:
    
    def set_header(host):
        user_agent = UserAgent()
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-TW,zh;q=0.9",
            "Host": host,  # 目標網站
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": user_agent.random,  # 使用者代理
            "Referer": "https://www.google.com/"  # 參照位址
        }
        return header

    def enroll():
        header = Crawler.set_header('enroll.tku.edu.tw')
        request = requests.get('http://enroll.tku.edu.tw/', headers=header)
        html = BeautifulSoup(request.text, 'html.parser')
        tr = html.find_all(class_='odd')
        results = []
        for i in tr:
            left = i.find_all(align='left')
            center = i.find_all(align='center')
            Event_name = left[0].text
            organizer = left[1].text
            url = 'http://enroll.tku.edu.tw/' + left[0].a['href']
            person = center[2].text
            results.append([Event_name,organizer,url,person])
        return results
    
    def ai():
        header = Crawler.set_header('www.ai.tku.edu.tw')
        results = []
        for page in range(1,3):
            request = requests.get('http://www.ai.tku.edu.tw/Front/News/News.aspx?id=QTwn%2B%2BDDe40=&page=' + str(page), headers=header)
            html = BeautifulSoup(request.text, 'html.parser')
            tr = html.find_all('tr')
            tr.pop(0)
            for i in tr:
                td = i.find_all('td')
                category = td[0].text
                date = td[1].text
                title = td[2].a.text
                url = td[2].a['href']
                results.append([category,date,title,url])
        return results

    def csie():
        header = Crawler.set_header('www.csie.tku.edu.tw')
        results = []
        for page in range(1,3):
            request = requests.get('http://www.csie.tku.edu.tw/Front/about/news/News.aspx?id=26J0iyD8bhA=&page=' + str(page), headers=header)
            html = BeautifulSoup(request.text, 'html.parser')
            tr = html.find_all('tr')
            tr.pop(0)
            for i in tr:
                td = i.find_all('td')
                category = td[0].text
                date = td[1].text
                title = td[2].a.text
                url = td[2].a['href']
                results.append([category,date,title,url])
        return results
