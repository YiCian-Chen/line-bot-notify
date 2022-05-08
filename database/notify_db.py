import psycopg2, urllib

class notify_db:

    def set_db():
        host = "127.0.0.1"
        dbname = "db"
        user = "postgres"
        password = "0000"
        sslmode = "allow"
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        return psycopg2.connect(conn_string)
        
    def insert_user(access_token, user_name, subscribe = True):
        conn = notify_db.set_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO notify (access_token,user_name,subscribe) VALUES (%s,%s,%s);", (access_token,user_name,subscribe))
        conn.commit()
        cursor.close()
        conn.close()
    
    def send_message(text_message):
        conn = notify_db.set_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM notify;")
        rows = cursor.fetchall()
        conn.commit()
        cursor.close()
        conn.close()
        url = 'https://notify-api.line.me/api/notify'
        data = {'message': text_message}
        for i in rows:
            try:
                headers = {"Authorization": "Bearer "+ i[0]}
                data = urllib.parse.urlencode(data).encode()
                req = urllib.request.Request(url, data=data, headers=headers)
                page = urllib.request.urlopen(req).read()
            except:
                pass