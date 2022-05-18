import psycopg2, requests, os, datetime

class notify_db:

    def set_db():
        host = "127.0.0.1"
        dbname = "db"
        user = "postgres"
        password = "0000"
        sslmode = "allow"
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        conn_string = os.environ['DATABASE_URL']
        return psycopg2.connect(conn_string)
        
    def insert_user(access_token, user_name, subscribe = True):
        conn = notify_db.set_db()
        cursor = conn.cursor()
        date = date = str(datetime.date.today())
        cursor.execute("INSERT INTO notify (access_token,user_name,subscribe,date) VALUES (%s,%s,%s,%s);", (access_token,user_name,subscribe,date))
        print("insert new user ", user_name , access_token)
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
                r = requests.post(url, data = data, headers=headers)
            except:
                pass
