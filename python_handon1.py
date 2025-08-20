# 問題１　九九
i = 1
while i < 10:
  j = 1
  while j < 10:
      print(f"{i*j}",end="  ")

      j +=1
  print("「{}」の段です".format(i))
  i += 1

# 別解(for文の場合)

for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end= " ")
    print("「{}」の段です".format(i))

# 問題2
# 複数行コメントアウトしている。
'''
i = int(input("数字を入力してください"))

if(i%3==0):
  print("foo")
else:
  print("hoo")
'''
# 問題3
i = int(input("一つ目の数字を入力してください"))
j = int(input("二つ目の数字を入力してください"))


print(i+j)

