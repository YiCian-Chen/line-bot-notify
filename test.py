from flask import request, Flask

app = Flask(__name__)
@app.route("/", methods=['GET'])
def callback_nofity():
    
    return '恭喜完成 LINE Notify 連動！請關閉此視窗。'

@app.route("/1", methods=['GET'])
def callback_1():
    # assert request.headers['referer'] == 'localhost'
    code = request.args.get('code')
    state = request.args.get('state')
    print("code = ",code)
    print("state = ",state)
    return "p"


if __name__ == "__main__":
    app.run()