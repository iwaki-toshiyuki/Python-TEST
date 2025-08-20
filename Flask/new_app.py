from datetime import datetime
from flask import Flask, request
import pytz
import locale
import random

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)


# localhost:5000にアクセスした時の処理
@app.route('/', methods=['GET'])
def raretech_message():
    return '夢は、目標に向かって毎日歩みを進めた者だけが叶えられる。\
            今日の二時間は、その一歩だ'


# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{date}です'


# /dateにアクセスすると、入力メッセージが表示される
@app.route('/date', methods=['POST'])

def current_day_week ():

    """
    コマンド例: curl -X POST -d 'days=2022-10-03' http://localhost:5000/date
    """

    w_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    input_date = request.form.get('days')
    # 受け取った文字を日付に変換する
    date = datetime.strptime(input_date, '%Y-%m-%d')

    # 日付を曜日に変換する
    week = date.weekday()

    return f'{date}は{w_list[week]}です'

# /aphorismにアクセスすると、入力メッセージが表示される
@app.route('/aphorism', methods=['POST'])

def random_message_view():

    """
    コマンド例: curl -s -X POST http://localhost:5000/aphorism
    """

    message = ["少年よ大志を抱け", "三顧の礼", "四面楚歌", "1パーセントのひらめきと99パーセントの努力", "ポツダム宣言"]

    # リストからランダムな要素を選ぶ
    random_message = random.choice(message)

    return f'{random_message}'


# /fortuneにアクセスすると、入力メッセージが表示される
@app.route('/fortune', methods=['GET'])

def fortune_slip():

    """
    コマンド例: curl -s -X POST http://localhost:5000/fortune
    """

    message = ["大吉", "中吉", "小吉"]

    # リストからランダムな要素を選ぶ
    random_message = random.choice(message)

    return f'{random_message}'


# /dateにアクセスすると、入力メッセージが表示される
@app.route('/message', methods=['POST'])

def gratitude_message():

    """
    コマンド例: curl -X POST -d 'name=hoge' http://localhost:5000/message
    """

    username = request.form.get('name')
    return f'毎日お疲れ様。{username}さん、これからも情熱を忘れずに行こう!!!'

@app.route('/login', methods=['POST'])
def login_message():
    """
    コマンド例: curl -X POST -d
    '{"username": "hoge", "password": "123456"}'
    http://localhost:5000/login
    """
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    return f'username..."{username}"とpassword..."{password}"を登録しました。'


if __name__ == '__main__':
    app.run()
