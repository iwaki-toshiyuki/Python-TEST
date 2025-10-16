import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import Cursor

#問1 基本的なグラフの作成（折れ線グラフ）
x = np.arange(10)
y = np.random.randint(-10,10,10)

#plt.plot(x,y)
#plt.show()

#問2 基本的なグラフの作成（散布図）
# x1 = np.random.randint(10,20,20)
# x2 = np.random.randint(20,30,20)
# y1 = np.random.randint(50,100,20)
# y2 = np.random.randint(0,40,20)

# plt.scatter(x1,y1)
# plt.scatter(x2,y2)
#plt.show()

#問3 基本的なグラフの作成（ヒストグラム）
# data = np.random.randint(0,10,10)
# plt.hist(data, bins=15)
# plt.show()

#問4 基本的なグラフの作成（棒グラフ）
x4 = ['Sam','John','Kevin','Adam']
y4 = np.random.randint(0,200,4)
# plt.bar(x4,y4)
# plt.show()

#問5 タイトルとラベル
x5 = np.arange(10)
y5 = np.random.randint(-10,10,10)
# plt.plot(x5,y5)
# plt.title('Result')
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.show()

#問6 軸範囲
# x1 = np.random.randint(10,20,20)
# x2 = np.random.randint(20,30,20)
# y1 = np.random.randint(50,100,20)
# y2 = np.random.randint(0,40,20)

# plt.scatter(x1,y1)
# plt.scatter(x2,y2)
# plt.xlim(0,40)
# plt.ylim(0,120)

# plt.show()

#問7 対数軸
x7 = np.linspace(0,10,500)
y7 = np.exp(x7)

# plt.yscale('log')
# plt.plot(x7,y7)
# plt.show()

#問8 凡例
x8 = np.linspace(0,2*np.pi,500)
y8_1 = np.sin(x8)
y8_2 = np.cos(x8) 

# plt.plot(x8,y8_1,label='sin')
# plt.plot(x8,y8_2,label='cos')

# plt.ylim(-2,2)
# plt.legend(loc=2)
# plt.show()

#問9 マーカの種類・サイズ変更
# x1 = np.random.randint(10,35,20)
# x2 = np.random.randint(5,45,20)
# x3 = np.random.randint(0,40,20)
# y1 = np.random.randint(50,100,20)
# y2 = np.random.randint(0,40,20)
# y3 = np.random.randint(20,80,20)

# plt.scatter(x1,y1,marker='*', s=80)
# plt.scatter(x2,y2,marker='^', s=60)
# plt.scatter(x3,y3,marker='x', s=30)

# plt.show()

#問10 注釈
# data = [5,3,4,2,0,3,2,1,4,6,8,5]
# plt.plot(data)
# plt.annotate('min value',xy=(4.2,0),xytext=(9,1), arrowprops=dict(facecolor='black',shrink=0.05))
# plt.show()

#問11 目盛り
# data = [5,3,4,2,0,3,2,1,4,6,8,5]
# plt.plot(data)
# plt.xticks(np.arange(12))
# plt.yticks(np.arange(0,10,2))
# plt.annotate('min value',xy=(4.2,0),xytext=(9,1), arrowprops=dict(facecolor='black',shrink=0.05))
# plt.show()

#問12 グリッド線
# data = [5,3,4,2,0,3,2,1,4,6,8,5]
# plt.plot(data)
# plt.grid(True)
# plt.show()

#問13 複数グラフの表示
names = ['Sam','John','Kevin','Adam']
values = [60,170,10,120]

plt.figure(figsize=(9,3))

#棒グラフ
#1行3列1番目
#plt.subplot(131)
#plt.bar(names,values)

#散布図
#1行3列2番目
#plt.subplot(132)
#plt.scatter(names,values)

#折れ線グラフ
#1行3列3番目
#plt.subplot(133)
#plt.plot(names,values)

#plt.show()

#問14 ヒートマップ
# data = np.random.rand(10,10)
# plt.imshow(data,vmin=0,vmax=1, cmap='Blues')
# plt.colorbar()
# plt.show()

#問15 3次元グラフ
# theta = np.linspace(-4*np.pi,4*np.pi,100)
# z = np.linspace(-2,2,100)
# r = z**2+1
# x = r*np.sin(theta)
# y = r*np.cos(theta)

# fig = plt.figure()
# ax = plt.axes(projection='3d')

# ax.plot(x,y,z,label = '3D Curve')
# ax.legend()
# plt.show()

#問16 円グラフ
# x = np.array([100,200,300,400,500])
# labels = ["Apple","Banana","Orange","Grape","Strawberry"]
# colors = ['red','yellow','orange','purple','pink']

# plt.pie(x,labels=labels,colors=colors,counterclock=False,startangle=90)
# plt.show()

#問17 GUIウィジェット
# fig = plt.figure(figsize=(8,6))
# ax = fig.add_subplot(111,facecolor = '#FFFFCC')

# x,y = 4*(np.random.rand(2,100)- .5)
# ax.plot(x,y,'o')
# ax.set_xlim(-2,2)
# ax.set_ylim(-2,2)

# cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

# plt.show()

#問18 演習問題 その1
fig = plt.figure(figsize=(9,6))

#グラフ1
# x1 = np.arange(10)
# y1 = np.random.randint(-10,10,10)

# ax1 = fig.add_subplot(211)
# ax1.set_title('Result')
# ax1.set_xlabel('x axis')
# ax1.set_ylabel('y axis')

# ax1.plot(x1,y1)
# ax1.plot()

# #グラフ2
# x2 = ['Sam','John', 'Kevin','Adam']
# y2 = np.random.randint(0,200,4)

# ax2 = fig.add_subplot(212)
# ax2.bar(x2,y2)

# plt.show()

#問19 演習問題 その2
# labels = 'Frogs','Hogs','Dogs','Logs'
# sizes = [15,30,45,10]
# explode = (0,0.1,0,0)

# plt.pie(sizes,explode=explode, labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
# plt.axis('equal')
# plt.show()

#問20 演習問題 その3
# mu1,sigma1 = 100,15
# mu2,sigma2 = 90,20
# mu3,sigma3 = 110,10
# x1 = mu1 + sigma1*np.random.randn(100)
# x2 = mu2 + sigma2*np.random.randn(100)
# x3 = mu3 + sigma3*np.random.randn(100)

# plt.hist([x1,x2,x3],bins=10,color= ['yellow','skyblue','blue'],label=['x1','x2','x3'],stacked=True)
# plt.title('histgram')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim(0,180)
# plt.grid(True)
# plt.legend(loc='upper left')
# plt.show()

