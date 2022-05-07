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
cursor.execute("SELECT * FROM csie;")
rows = cursor.fetchall()

data = Crawler.csie()
for i in data:
    count = 0
    for j in rows:
        if i[2] == j[2]:
            count += 1
    if not count:
        category = i[0]
        date = i[1]
        title = i[2]
        url = i[3]
        cursor.execute("INSERT INTO csie (category,date,title,url) VALUES (%s,%s,%s,%s);", (category,date,title,url))
        print("insert new data")
        # line notify 傳送訊息
        
conn.commit()
cursor.close()
conn.close()
