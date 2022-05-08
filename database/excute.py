from crawler import Crawler
from notify_db import notify_db

class excute:
    def all():
        excute.enroll()
        excute.csie()
        excute.ai()

    def enroll():
        conn = notify_db.set_db()
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
                msg = '\n' + Event_name + '\n' + organizer + '\n' + url
                notify_db.send_message(msg)
                
        conn.commit()
        cursor.close()
        conn.close()

    def csie():
        conn = notify_db.set_db()
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
                msg = '\n' + title + '\n\n' + category + '\n' + url + '\n' + date
                notify_db.send_message(msg)
                
        conn.commit()
        cursor.close()
        conn.close()
    
    def ai():
        conn = notify_db.set_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ai;")
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
                cursor.execute("INSERT INTO ai (category,date,title,url) VALUES (%s,%s,%s,%s);", (category,date,title,url))
                print("insert new data")

                # line notify 傳送訊息
                msg = '\n' + title + '\n\n' + category + '\n' + url + '\n' + date
                notify_db.send_message(msg)
                
        conn.commit()
        cursor.close()
        conn.close()
