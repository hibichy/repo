#単回帰分析を実装する
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

# データの読み込み
df = pd.read_csv('data.csv', encoding='utf-8')

# データの可視化
plt.scatter(df['x'], df['y'])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

# データの分割　学習用とテスト用
from sklearn.model_selection import train_test_split
X = df[['x']]
y = df['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# 機械学習モデルの作成
lr = LinearRegression()
lr.fit(X_train, y_train)

# 評価指標の算出
from sklearn.metrics import mean_squared_error
y_pred = lr.predict(X_test)
print('MSE: %.2f' % mean_squared_error(y_test, y_pred))

# モデルの保存
import pickle
pickle.dump(lr, open('model.pkl', 'wb'))

# モデルの読み込み
model = pickle.load(open('model.pkl', 'rb'))

# 予測
print(model.predict([[10]]))

# モデルの読み込み
model = pickle.load(open('model.pkl', 'rb'))



