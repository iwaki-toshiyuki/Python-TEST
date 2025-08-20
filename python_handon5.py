#課題1 素数判定

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime2(m):
    if m <= 1:
        return False
    elif m <= 3:
        return True
    elif m % 2 == 0 or m % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if m % i == 0 or m % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("1つ目の数字を入力してください"))
m = int(input("2つ目の数字を入力してください"))
if (is_prime(n))and(is_prime2(m)):
    print("True")
else:
    print("False")


#解答(課題１)
num1 = int(input("1つ目の数字を入力して下さい"))
num2 = int(input("2つ目の数字を入力して下さい"))

if num1 <= 1 or num2 <= 1:
    print(False)
else:
    for i in range(2, (num1 // 2) + 1):
        if num1 % i == 0:
            print(False)
            break
    else:
        for i in range(2, (num2 // 2) + 1):
            if num2 % i == 0:
                print(False)
                break
        else:
            print(True)

#課題2 バブルソート：前から2つずつデータを比較し並べ替える．

def bubble_sort(data):
    """バブルソート：前から2つずつデータを比較し並べ替える．"""
    for i in range(len(data)):
        for j in range(len(data) - i -1):
            if data[j] > data[j+1]: #左の方が大きい場合
                data[j], data[j+1] = data[j+1], data[j] #前後入れ替え

    return data

if __name__ == '__main__':
    DATA = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = bubble_sort(DATA.copy())

    print(f"{DATA}  →  {sorted_data}")


#課題3 マージソート：リストを半分ずつ分割 → 並べ替えしながら再構築

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2    #半分の位置を計算

    # 再帰的に分割
    left = merge_sort(data[:mid])        #左側を分割
    right = merge_sort(data[mid:])      #右側を分割

    #統合
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:         #左<=右のとき
            result.append(left[i])    #左側から1つ取り出して追加
            i += 1
        else:
            result.append(right[j])  #右側から1つ取り出して追加
            j += 1

    # 残りをまとめて追加
    if i < len(left):
        result.extend(left[i:])      #左側の残りを追加
    if j < len(right):
        result.extend(right[j:])    #右側の残りを追加

    return result

if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = merge_sort(data)
    print(f"{data} → {sorted_data}")
