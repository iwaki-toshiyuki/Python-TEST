#NumPyノック
import numpy as np
import matplotlib.pyplot as plt

#問1 ベクトルの定義
a = np.array([1,2,3,4])
b = np.array([[4],
             [-1],
             [6]])
print(a)
print(b)

#問2 行列の定義
c = np.array(
    [[-3,-2],
    [7,1]]
)
print(c)
d = np.array([[3,-2,0,1],
             [7,1,-1,2],
             [4,-5,1,3]])
print(d)

#問3 ベクトルの作成
e = np.zeros((1,2))
print(e)
f = np.ones((4,1))
print(f)

#問4 行列の作成
g = np.eye(3)
print(g)
h = np.eye(3,4)
print(h)

#問5 基本情報の取得
i = np.array([2,3,4])
j = np.array([[1.2,3.5,5.1],[-0.3,1.1,-4.5]])

#形状
print(i.shape)
print(j.shape)
#次元
print(i.ndim)
print(j.ndim)
#データ型
print(i.dtype)
print(j.dtype)
#要素数
print(i.size)
print(j.size)

#問6 インデックスとスライシング
k = np.arange(1,13,2)
L = np.array([[2,4,6],
            [-1,5,3],
            [0,-2,3]])
#1個前の数字まで取る
print(k[2:-1])
#逆順
print(k[::-1])
print(L[0])
print(L[2,0])
print(L[1:,1:])

#問7 四則演算
m = np.array([[1,3],[-2,4]])
n = np.array([[2,-1],[3,0]])
print(m+n)

m = np.array([[1,3],[-2,4]])
n = np.array([[2,-1],[3,0]])
print(m-n)

m = np.array([[-2,-5],[1,3]])
n = np.array([[3,0],[6,-2]])
print(m@n)
print(m.dot(n))

m = np.array([[3,5],[4,-1]])
n = np.array([[-2,1],[0,-3]])
print(m*n)

#問8 転置
o = np.array([[2,3,4]])
p = np.array([[1.2, 3.5, 5.1],[-0.3, 1.1, -4.5]])
print(o.T.shape)
print(p.T)

#問9 逆行列
q = np.array([[4,-2],[1,0]])
det = np.linalg.det(q)
inv = np.linalg.inv(q)
print(det)
print(q @ inv)

#問10 ブロードキャスト
r = np.array([[4,-2],[1,0]])
s = np.array([[8,1,5],[-3,0,-7]])
print(r*0.5)
print(s*2)

#問11 ベクトルのサイズ変更
t = np.arange(12)
print(t.reshape(3,4))

#問12 統計値
u = np.array([[2,4,6],
            [-1,5,-3],
            [0,-2,3]])

#最大値
print(u.max())
#最小値
print(u.min())
print(u.min(axis=0))
print(u.min(axis=1))
#総和
print(u.sum())
print(u.sum(axis=0))
print(u.sum(axis=1))
#平均値
print(u.mean())
#分散
print(u.var())
#標準偏差
print(u.std())

#問13 ユニバーサル関数 part1
v = np.array([0,1,2,4]).reshape(2,-1)

#平方根
print(np.sqrt(v))
print(np.exp(v))

#問14 ユニバーサル関数 part2
w = np.array([0,np.pi,np.pi/2,-np.pi/4]).reshape(2,-1)
print(np.sin(w))
print(np.cos(w))

#問15 行列の結合
x = np.array([0,1,-1,2,4,-3,5,-2,7]).reshape(3,-1)
y = np.array([-2,0,1,5,-1,2,-6,3,4]).reshape(3,-1)
#縦方向
z = np.vstack((x,y))
print(z)
#横方向
aa = np.hstack((x,y))
print(aa)

#問16 行列の分解
#縦方向
bb = np.vsplit(z,2)
print(bb)
#横方向
cc = np.hsplit(aa,2)
print(cc)

#問17 グラフ化
dd = np.linspace(0,2*np.pi,500)
print(dd)
print(dd.size)

plt.plot(dd,np.sin(dd))
plt.plot(dd,np.cos(dd))
#以下のコメントアウトを外すとグラフが出る。
#print(plt.show())

data = np.random.randint(0,30,100)
print(plt.hist(data))
#以下のコメントアウトを外すとヒストグラムが出る。
#print(plt.show())

#問18 演習課題 その1
ee = np.arange(-10,13,2).reshape(4,-1)
ff = np.eye(3,4) - 2
print(ee.shape,ff.shape)

gg = ee @ ff
print(gg)

#問19 演習課題 その2
hh = gg[:2, :2]
print(hh)

#転置
print(hh.T)

#逆行列
print(np.linalg.det(hh.T))

print(np.linalg.inv(hh.T))

#問20 演習課題 その3
data1 = np.random.randint(-100,100,300)
data2 = np.random.randint(-100,100,300)

print(plt.scatter(data1,data2))
#以下のコメントアウトを外すと散布図が出る。
print(plt.show())