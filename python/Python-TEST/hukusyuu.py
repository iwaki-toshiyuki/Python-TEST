momo = 100 * 5
mikan = 40 * 8
nashi = 80 * 5
kiwi = 60 * 9
suika = 90 * 20
kaki = 110 + 10

# Pythonの出力コマンド
print(momo + mikan + nashi + kiwi + suika + kaki) # 計算結果を表示

# Pythonの変数
# name = input("あなたの名前を入力してください: ")
# print("こんにちは、" + name + "さん！")

#age = input("いくつですか？")

#print("あなたは" + age + "歳ですね！")

# if文
# score = int(input("年齢を入力してください: "))

# if score >= 20:
#     print("成人です")
# else:
#     print("未成年です")

# 配列
fruits = ["momo", "mikan", "nashi", "kiwi", "suika", "kaki"]

print(fruits[0])
print(fruits[5])

#for文　range関数で範囲を選択
for i in range(1,6):
    print(i)


# 引数
def add(a,b):
		return a + b

print(add(2, 7))

# クラス
class Raretech:
		def study(self):
			return "学ぶって楽しい"

raretech = Raretech()
print(raretech.study())

# ライブラリ、インポート(mymodule.pyというファイル作成済み)
from mymodule import hello, PI

print(hello("Python"))
print(PI)
