
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
import joblib  # 用于保存和加载模型

seed=22
random.seed(seed)
np.random.seed(seed)
tf.random.set_seed(seed)
os.environ['PYTHONHASHSEED'] = str(seed)
tf.config.experimental.enable_op_determinism()

# 指定 GPU 设备
physical_devices = tf.config.list_physical_devices('GPU') 
if len(physical_devices) > 0:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)

# 检查是否设置了 GPU
print("Num GPUs Available: ", len(physical_devices))

# 余下的代码与你的原始代码保持不变


start_date = 20180101
end_date = 20190601
size=9601

start_time = pd.Timestamp(str(start_date))
end_time = pd.Timestamp(str(end_date))


# 读取数据
priceFile='./price/DailyUSDPrice.xlsx'
price = pd.read_excel(priceFile,header=None)

# 将第 0 列转换为 datetime 类型
price[0] = pd.to_datetime(price[0])

price=price[(price[0] >= start_time) & (price[0] < end_time)]

# 将第 0 列设置为索引
price.set_index(0, inplace=True)

price=price/1000

# 重命名列
price.columns = ['price']

# 显示 DataFrame
print(price)


others=['new消费者价格指数','new利率','new道琼斯工业平均指数历史数据']
otherData=pd.DataFrame()
for i in others:
    file='./newCsv/'+i+'.csv'
    df=pd.read_csv(file)
    df.columns=[0,1]
    df[0] = pd.to_datetime(df[0], format='%Y-%m-%d')
    
    df=df[(df[0] >= start_time) & (df[0] < end_time)]
    
    df.set_index(0, inplace=True)
    # print(df)
    
    # 横向合并三个 DataFrame
    otherData= pd.concat([otherData,df], axis=1)


otherData.columns=['消费者','利率','道琼斯']
# 显示合并后的 DataFrame
print(otherData)



file='./newCsv/'+str(size)+'_'+str(start_date)+'_to_'+str(end_date)+'.csv'
GDELT=pd.read_csv(file,header=None)
GDELT[0] = pd.to_datetime(GDELT[0], format='%Y%m%d')
GDELT=GDELT[(GDELT[0] >= start_time) & (GDELT[0] < end_time)]
GDELT.set_index(0, inplace=True)
print(GDELT)



Y=price['price']
print(Y)



X=pd.concat([otherData,GDELT], axis=1)
X.columns = X.columns.astype(str) 

# 归一化数据
scaler = MinMaxScaler()
X = X.fillna(0)
X= pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
joblib.dump(scaler, './scaler.pkl')


print(X)


# 将数据集划分为训练集、验证集和测试集
train_size = int(len(X) * 0.7)
valid_size = int(len(X) * 0.2)
test_size = len(X) - train_size - valid_size

X_train, Y_train= X[:train_size],Y[:train_size]
X_valid, Y_valid= X[train_size:(train_size + valid_size)], Y[train_size:(train_size + valid_size)]
X_test, Y_test= X[(train_size + valid_size):], Y[(train_size + valid_size):]



def getLossAndPredictions(epochs,batch_size):
    
    # 2. 构建 LSTM 模型
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(X.shape[1],1)))
    model.add(LSTM(units=50))
    model.add(Dense(units=1))
    
    # 3. 模型编译
    model.compile(optimizer='adam', loss='mean_squared_error')
    # model.compile(optimizer='adam', loss='mean_absolute_error')

    # 4. 模型训练
    model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_valid, Y_valid))
    
    # 5. 模型评估
    loss = model.evaluate(X_test, Y_test)
    
    # 6. 模型应用（例如，进行预测）
    predictions = model.predict(X_test)
    model.save('./lstm_model.h5')
    return [loss,predictions]

getLossAndPredictions(50,32)






