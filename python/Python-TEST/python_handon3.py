#問題1
'''不正解
def main():
    count_same = 0
    previous = None
    all_same = True

    for i in range(10):
        try:
            num = int(input("数字を入力してください: "))
        except ValueError:
            print("数字を入力してください。")
            return

        if i == 0:
            previous = num
        else:
            if num == previous:
                count_same += 1
                print(f"{count_same}回連続")
            else:
                all_same = False
                print("連続なし")
            previous = num

if __name__ == "__main__":
    main()
'''


#解答(for文）
x = ""
v = 1
for i in range(10):
    j = int(input("数字を入力して下さい"))
    if j == x:
        v = v + 1
        print("{}回連続".format(v))
        if v == 10:
            print("perfect!!")
    else:
        v = 1
        print("連続なし")
    x = j

#解答(while文）
x = ""
v = 1
i = 1
while i <= 10:
    j = int(input("数字を入力して下さい"))
    if j == x:
        v = v + 1
        print("{}回連続".format(v))
        if v == 10:
            print("perfect!!")
    else:
        v = 1
        print("連続なし")
    x = j
    i = i + 1

# 問題2
'''不正解
def has_five(n):
  return '5' in str(n)

# ユーザーに入力を求める
number_str = input("整数を入力してください: ")

# 入力された文字列を整数に変換
try:
    number = int(number_str)
    if has_five(number):
        print(f"{number} には5が含まれています。")
    else:
        print(f"{number} には5は含まれていません。")

except ValueError:
    print("無効な入力です。整数を入力してください。")
'''

#解答
x = list(map(int, input()))
for i in x:
    if i == 5:
        print("5です!!")
    else:
        print("5じゃないです")

#別解
# 【プラスα】xをリストにせず、str型として扱うことも可能
'''
x = input()
for i in x:
		if int(i) == 5:
				print("5です!!")
    else:
        print("5じゃないです")
'''


#問題3
i = int(input("一つ目の数字1 "))
j = int(input("二つ目の数字2 "))

add = i + j
sub = i - j

print("足し算の合計{}".format(add))
print("引き算の合計{}".format(sub))
