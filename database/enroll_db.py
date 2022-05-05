import psycopg2

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


# Update connection string information
host = "127.0.0.1"
dbname = "db"
user = "postgres"
password = "0000"
sslmode = "allow"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
cursor = conn.cursor()
# Drop previous table of same name if one exists
# cursor.execute("SELECT * FROM enroll;")
# rows = cursor.fetchall()
# print(rows)


for i in tr:
    left = i.find_all(align='left')
    center = i.find_all(align='center')
    Event_name = left[0].text
    organizer = left[1].text
    url = 'http://enroll.tku.edu.tw/' + left[0].a['href']
    person = center[2].text
    cursor.execute("INSERT INTO enroll (event_name, organizer,url) VALUES (%s,%s,%s);", (Event_name,organizer,url))
print("insert seccess")

cursor.execute("SELECT * FROM enroll;")
rows = cursor.fetchall()
print(rows)

conn.commit()
cursor.close()
conn.close()
