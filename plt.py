import numpy as np
import matplotlib.pyplot as plt
 
x = np.linspace(-5, 5, 100) # -5から5までを100ステップに分けた配列を生成
y = np.sin(x) # xの各値に対してsin関数の値を計算
 
plt.plot(x, y) # 折れ線グラフをプロット
plt.show() # グラフを表示

#折れ線グラフ
data = [2, 4, 6, 3, 5, 8, 4, 5]
plt.plot(data)
plt.show()

#棒グラフ
a = range(0, 7)
b = [55, 21, 61, 98, 85, 52, 99]
plt.bar(a, b)
plt.show()

#散布図
x = [10, 51, 44, 23, 55, 95]
y = [5, 125, 2, 55, 19, 55]
plt.scatter(x, y)
plt.show()

#円グラフ
labels = ["A", "B", "C", "D", "E"]
data = [54, 32, 18, 44, 29]
plt.pie(data, labels=labels, autopct="%1.1f%%")
plt.show()

#ヒストグラム
x = np.random.normal(10, 5, 1000)
plt.hist(x, bins=30)
plt.show()

#箱ひげ図
data = np.random.normal(10, 5, 100)
plt.boxplot(data)
plt.show()

#複数のグラフを並べて描画
fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 1行2列のサブプロットを作成
 
x = np.linspace(0, 10, 100)
 
axs[0].plot(x, np.sin(x)) # 1つ目のサブプロットにsinグラフを描画
axs[1].plot(x, np.cos(x)) # 2つ目のサブプロットにcosグラフを描画
 
plt.show()