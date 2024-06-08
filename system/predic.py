import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import MaxAbsScaler
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.optimizers import Adam
from itertools import product
import random
import os
from keras.models import load_model
import joblib
from sklearn.preprocessing import MinMaxScaler


# 加载保存的scaler和模型
scaler = joblib.load('scaler.pkl')

# 定义函数进行归一化
def normalize_input(new_data, scaler):
    new_data = new_data.fillna(0)
    new_data_normalized = pd.DataFrame(scaler.transform(new_data), columns=new_data.columns)
    return new_data_normalized

# 假设X_test是用户输入的新数据
X_test = pd.DataFrame({
    'feature1': [7],
    'feature2': [8]
})

# 对新数据进行归一化
X_test_normalized = normalize_input(X_test, scaler)

# 加载模型
model = load_model('./system/model/lstm_model.h5')
print("模型已成功加载")


# 使用模型进行预测
predictions = model.predict(X_test_normalized)
print(predictions)
