from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
 
# Irisデータセットをロード
iris = datasets.load_iris()
X = iris.data
y = iris.target
 
# トレーニングデータとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
 
# サポートベクターマシン(SVM)を使って分類器を作成
clf = svm.SVC(gamma='auto')
 
# トレーニングデータにて学習
clf.fit(X_train, y_train)
 
# テストデータで検証
test_result = clf.predict(X_test)
 
print(test_result)
print(y_test)
