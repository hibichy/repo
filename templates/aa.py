#あああ

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# データの読み込み
df = pd.read_csv('data.csv', encoding='utf-8')

#データの可視化
sns.pairplot(df, hue='class')

#データの分割　学習用とテスト用
from sklearn.model_selection import train_test_split
X = df.drop('class', axis=1)
y = df['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#機械学習モデルの作成
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(X_train, y_train)

#評価指標の算出
from sklearn.metrics import accuracy_score
y_pred = lr.predict(X_test)
print('Accuracy: %.2f' % accuracy_score(y_test, y_pred))

#モデルの保存
import pickle
pickle.dump(lr, open('model.pkl', 'wb'))

