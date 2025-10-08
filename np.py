#配列の作成
import numpy as np

x = np.array([1, 2, 3, 4, 5])
print(x)

#配列の形状を調べる
x = np.array([[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]])
print(x.shape)

#配列の生成: arange()
y = np.arange(10)
print(y)

#配列操作
z = np.arange(10).reshape(2, 5)
print(z)

#ブロードキャスト
print(x + 5)