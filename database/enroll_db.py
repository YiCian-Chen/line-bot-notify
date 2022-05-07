import psycopg2
from crawler import Crawler

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
cursor.execute("SELECT * FROM enroll;")
rows = cursor.fetchall()

data = Crawler.enroll()
for i in data:
    count = 0
    for j in rows:
        if i[0] == j[0]:
            count += 1
    if not count:
        Event_name = i[0]
        organizer = i[1]
        url = i[2]
        cursor.execute("INSERT INTO enroll (event_name, organizer,url) VALUES (%s,%s,%s);", (Event_name,organizer,url))
        print("insert new data")
        # line notify 傳送訊息
        
conn.commit()
cursor.close()
conn.close()
