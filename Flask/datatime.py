# datetimeライブラリをインポート
from datetime import datetime

#Flaskライブラリをインポート
from flask import Flask

#pytzをインストール
import pytz

# Flaskのインスタンスをappという名前で作成
app = Flask(__name__)

# now()で現在の日付と時刻を取得
now = datetime.now()
print("現在時刻は" + now.strftime("%Y年%m月%d日 %H時%M分%S秒") + "です。")


#正解
# /timeへgetでアクセスしたら現在時刻を知らせる
@app.route('/time', methods=['GET'])
def current_time():
    dt_now = datetime.now(pytz.timezone('Asia/Tokyo'))
    date = dt_now.strftime('%Y年%m月%d日  %H時%M分%S秒')
    return f'現在時刻は{date}です'


