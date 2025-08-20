# 問題１　九九
# (while文の場合)

i = 1
while i <= 9:
  j = 1
  while j <= 9:
    print(f"{i}✖︎{j} = {i*j}")
    j +=1
  i += 1


# (for文の場合)
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i}✖︎{j} = {i*j}")


# 問題2　(解答)

#for文の場合
h = int(input("数字を入力して下さい"))

# 1行目
for i in range(h):
    print("*", end="")
print()

# 受取った値が1でない場合（1の場合は1行目のみの表示）
if h != 1:
    # 2～最終行前
    for i in range(2, h):
        print("*", end="")
        for j in range(2, h):
            print(" ", end="")
        print("*")
    # 最終行
    for i in range(h):
        print("*", end="")
    print()

#while文の場合
h = int(input("数字を入力して下さい"))
# 1行目
i = 1
while i <= h:
    print("*", end="")
    i = i + 1
print()

# 受取った値が1でない場合（1の場合は1行目のみの表示）
if h != 1:
    i = 2
    # 2～最終行前
    while i < h:
        print("*", end= "")
        j = 2
        while j < h:
            print(" ", end="")
            j = j + 1
        print("*")
        i = i + 1

    # 最終行表示
    i = 1
    while i <= h:
        print("*", end="")
        i = i + 1
    print()


#問題３ フィボナッチ数列
def Fib(n):
    a, b = 0, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n-2):
            a, b = b, a + b
        return b

print([Fib(n) for n in range(1, 22)])


#解答
def fib(n):
    a = 0
    b = 1
    while a < n:
        print(a, end=' ')
        tmp = a
        a = b
        b = tmp + b
    print()

# 関数に上限値を指定して実行
fib(10000)
