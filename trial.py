#Pythonのライブラリをインポート
import numpy as np
from flask import Flask, request, jsonify, render_template

#Flaskのインスタンスを作成
app = Flask(__name__)

#モデルをロード
import pickle
model = pickle.load(open('model.pkl', 'rb'))

#htmlをレンダリングする
@app.route('/')
def home():
    return render_template('index.html')
