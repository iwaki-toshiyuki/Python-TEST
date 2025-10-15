import pandas as pd
import matplotlib.pyplot as plt

#問1 データの読み込み
df = pd.read_csv('CSV/weather.csv')
#print(df)

#問2 データの中身確認
#先頭確認
#print(df.head(3))
#末尾確認
#print(df.tail(3))

#問3 不要な列、行の削除

df.columns

df3 = df[['年月日',
    '平均気温(℃)',
    '最高気温(℃)',
    '最低気温(℃)',
    '降水量の合計(mm)',
    '最深積雪(cm)',
    '平均雲量(10分比)',
    '平均蒸気圧(hPa)',
    '平均風速(m/s)',
    '日照時間(時間)'
    ]][1:]
print(df3)

#問4 データ型、サイズ、列名、行名の確認

#データ型
print(df3.dtypes)

#サイズ
print(df3.shape)

#列名
print(df3.columns)

#行名（インデックス番号）
print(df3.index)

#問5 任意の要素の取得

#要素番号(インデックス)で指定
print(df3.iloc[4:10, 2:6])

#カラム名で指定
print(df3.loc[5:10, '最高気温(℃)':'最深積雪(cm)'])


#問6 条件抽出
df_people = pd.read_csv('CSV/people.csv')
print(df_people)

df6 = df_people[df_people['nationality'] == 'America']
print(df6)
df6_2 = df_people.query('nationality == "America"')
print(df6_2)
df6_3 = df_people[df_people['nationality'].isin(['America'])]
print(df6_3)

df6_age = df_people[(df_people['age'] >= 20) & (df_people['age'] < 30)]
print(df6_age)
df6_age2 = df_people.query('age >= 20 & age <30')
print(df6_age2)

#問7 ユニークな値の抽出
print(df_people['nationality'].unique())
print(df_people['name'].unique())

#問8 重複除去
print(df_people.drop_duplicates(subset='nationality'))

#問9 カラム名変更

df3.columns = ['年月日',
    '平均気温',
    '最高気温',
    '最低気温',
    '降水量の合計',
    '最深積雪',
    '平均雲量',
    '平均蒸気圧',
    '平均風速',
    '日照時間'
    ]

print(df3)

df9 = df3.rename(columns={
    '平均気温': '平均'
})

print(df9)

#問10 並び替え
df10 = df3.sort_values('最高気温', ascending=False)
print(df10)

#問11 ダミー変数の処理
print(df_people['nationality'])
print(pd.get_dummies(df_people,columns=['nationality'], dtype=int))

#問12 欠損値の確認
print(df3.isnull())

#問13 欠損値の補完
print(df3.fillna(0).head())

#問14 欠損値の削除
print(df3.dropna(axis=1).head()) #axisを1にすると列方向を指定できる

#問15 ユニークな値と出現回数
df_iris = pd.read_csv('CSV/iris.csv')
print(df_iris.head())
print(df_iris['Class'].value_counts())

#問16 グループごとの集計
print(df_iris.groupby('Class').mean())

#問17 統計量の確認
#平均値
print(df3.mean(numeric_only=True))
#中央値
print(df3.median(numeric_only=True))
#標準偏差
print(df3.std(numeric_only=True))
#最大値
print(df3.max(numeric_only=True))
#最小値
print(df3.min(numeric_only=True))
#カラムごとに表形式で統計量等を出力
print(df3.describe())

#問18 折れ線グラフの表示
print(df3[:50].plot(x='年月日',y=['平均気温','最高気温','最低気温'], legend=False))
#print(plt.show())

#問19 相関係数の算出
print(df3[['平均気温','降水量の合計','日照時間']].corr())
print(df3.corr(numeric_only=True))

#問20 データの出力
print(df3.fillna(0).to_csv('CSV/export.csv',index=False))