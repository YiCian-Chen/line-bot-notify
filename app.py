from flask import request, Flask
import os, urllib, json

client_id = os.environ['NOTIFY_CLIENT_ID']
client_secret = os.environ['NOTIFY_CLIENT_SECRET']
redirect_uri = f"https://tku-line-notify.herokuapp.com/callback/notify?state=TKU"

app = Flask(__name__)
@app.route("/callback/notify", methods=['GET'])
def callback_nofity():
    assert request.headers['referer'] == 'https://notify-bot.line.me/'
    code = request.args.get('code')
    state = request.args.get('state')

    # 接下來要繼續實作的函式
    # access_token = get_token(code, client_id, client_secret, redirect_uri)

    return '恭喜完成 LINE Notify 連動！請關閉此視窗。'


def get_token(code, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri):
    url = 'https://notify-bot.line.me/oauth/token'
    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret
    }
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url, data=data, headers=headers)
    page = urllib.request.urlopen(req).read()
    
    res = json.loads(page.decode('utf-8'))
    return res['access_token']


if __name__ == "__main__":
    app.run()