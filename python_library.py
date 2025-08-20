# datetimeライブラリをインポート
from datetime import datetime

# now()で現在の日付と時刻を取得
now = datetime.now()

print("今日の日付は", now)

# strftimeでフォーマットを変更
formatted_date = now.strftime("%Y年%m月%d日")

print("今日の日付は", formatted_date)

# 日付の計算
from datetime import datetime, timedelta

# 現在の日付を取得
today = datetime.now()

# 7日後の日付を計算
future_date = today + timedelta(days=7)
formatted_future_date = future_date.strftime("%Y年%m月%d日")
print("7日後は:", formatted_future_date)

# 7日前の日付を計算
past_date = today - timedelta(days=7)
formatted_past_date = past_date.strftime("%Y年%m月%d日")
print("7日前は:", formatted_past_date)

import random

# 1から10までのランダムな整数を生成
random_number = random.randint(1, 10)
print(random_number)

fruits = ["apple", "banana", "cherry", "grape", "strawberry"]

# リストからランダムな要素を選ぶ
random_fruit = random.choice(fruits)
print(random_fruit)

numbers = [1, 2, 3, 4, 5]

# リストをシャッフル
random.shuffle(numbers)
print("Shuffled list:", numbers)
