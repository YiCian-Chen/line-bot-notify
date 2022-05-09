from flask import request, Flask, render_template
import os, requests
from database.notify_db import notify_db
from database.excute import excute

client_id = os.environ['NOTIFY_CLIENT_ID']
client_secret = os.environ['NOTIFY_CLIENT_SECRET']
redirect_uri = f"https://tku-line-notify.herokuapp.com/callback/notify"

app = Flask(__name__)
@app.route("/callback/notify", methods=['GET'])
def callback_nofity():
    # assert request.headers['referer'] == 'https://notify-bot.line.me/'
    code = request.args.get('code')
    state = request.args.get('state')
    if(code == None):
        return "wrong"
    print("code = ",code)
    print("state = ",state)
    return render_template("code.html", code=code)

@app.route("/update", methods=['GET'])
def update():
    excute.all()
    print("update now")
    return render_template("update.html")

@app.route("/authorize", methods=['POST'])
def authorize():
    code = request.form.get('code')
    name = request.form.get('name')
    print("Auth code = ",code)
    print("Auth name = ",name)
    access_token = get_token(code, client_id, client_secret, redirect_uri)
    notify_db.insert_user(access_token,name)
    return render_template("access.html")

def get_token(code, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri):
    url = 'https://notify-bot.line.me/oauth/token'
    headers = { 'Content-Type': 'application/x-www-form-urlencoded'}
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    r = requests.post(url, data = data, headers=headers)
    print(r.json())
    return r.json()['access_token']
    
if __name__ == "__main__":
    app.run()