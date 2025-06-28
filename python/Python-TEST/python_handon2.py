#問題1
i = int(input("一つ目の数字を入力してください"))
j = int(input("二つ目の数字を入力してください"))

print("i =", i, ", j =", j)

# 値の入れ替え
i, j = j, i

print("i =", i, ", j =", j)

#問題2
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*",end=" ")
        if i == j:
            print("\n")
        j +=1
    i += 1

#問題3　素数判定
limit = 20000
total = 0
for i in range(2, limit):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
          total += i
print(total)
