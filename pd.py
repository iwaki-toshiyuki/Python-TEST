import pandas as pd

# CSVファイルの読み込み
df1 = pd.read_csv('./test.csv')
 
# Excelファイルの読み込み
df2 = pd.read_excel('./test.xlsx')
 
# JSONファイルの読み込み
df3 = pd.read_json('./test.json')

#列の選択
series = df1['Name']
print(series)

#条件を指定した行の選択
filtered_df1 = df1[df1['ID'] == 1]
print(filtered_df1)

filtered_df2 = df1[df1['ID'] > 8]
print(filtered_df2)

#グループ化と集約
grouped_df = df1.groupby('Name').agg({'Age': 'sum'})
print(grouped_df)

#新しいカラムの追加
df1['Gender'] = ['male', 'female', 'male', 'female', 'male', 'female',
                 'male', 'male', 'female', 'female']
print(df1)