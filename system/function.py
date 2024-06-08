
import pandas as pd

from keras.models import load_model
import joblib
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
import streamlit as st
import csv
import pymysql
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np
from datasets import Dataset
from mysql import *
import time
from datetime import datetime, timedelta


def getNewDF(res):
    df=pd.DataFrame(res)
    df.columns = ['模拟黄金价格 千美元/盎司']
    df.index = range(1, len(df) + 1)
    return df

# 定义函数进行归一化
def normalize_input(new_data, scaler):
    
    # new_data = new_data.fillna(0)
    new_data_normalized = pd.DataFrame(scaler.transform(new_data), columns=new_data.columns)
    
    return new_data_normalized

def predic(X_test):
  
    # 加载保存的scaler和模型
    scaler = joblib.load('./model/scaler.pkl')

    # 对新数据进行归一化
    # X_test_normalized = normalize_input(X_test, scaler)

    X_test_normalized = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)
    # 加载模型
    model = load_model('./model/lstm_model.h5')
    
    print("模型已成功加载")

    # 使用模型进行预测
    predictions = model.predict(X_test_normalized)
    
    return predictions


def simulate(text):
    l=9600+3

    allDF=pd.DataFrame()

    dataList=text.split('|')
    for dayData in dataList:
        dayDataList=dayData.split()

        # 转换为 DataFrame
        df = pd.DataFrame(dayDataList)
        # print(df)
        
        if df.shape[0]<l:
            # 计算需要添加的零值行数
            num_zeros_to_append = l- df.shape[0]
            # 创建零值DataFrame
            zeros_df = pd.DataFrame(0, index=range(num_zeros_to_append), columns=df.columns)
            # 将零值DataFrame附加到原始DataFrame末尾
            df = pd.concat([df, zeros_df], ignore_index=True)
            
            pass
        df = df.transpose()
        # print(df)
        allDF = pd.concat([allDF, df], ignore_index=True)
    
    # print(allDF)
    new_column_names = ['消费者', '利率', '道琼斯'] + [str(i) for i in range(1, 9601)]

    allDF.columns = allDF.columns.astype(str)
    # 使用 rename 函数将列名更改为新的名称列表
    allDF.columns = new_column_names
    p=predic(allDF)
    
    return getNewDF(p)


def generate_plot(df):
    
    x=df.index
    y=df['模拟黄金价格 千美元/盎司']
    # 使用 Matplotlib 绘制折线图
    fig, ax = plt.subplots()
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.plot(x, y)
    ax.set_xlabel('Date')
    ax.set_ylabel('模拟黄金价格 千美元/盎司')
    ax.set_title('黄金价格模拟结果')
    
    return fig

def save2mysql(username,text,df):
    timeID = insertInputTable(username,text)
    
    p=''
    for val in df.values.flatten():
        p=p+' '+str(val)
    insertResultTable(timeID,p)
    
def getRandomNumbers():
    random_numbers = np.random.uniform(0, 2, 9603)
    random_numbers = np.round(random_numbers, 2)
    return random_numbers
    
def main():
    # 这里是你的代码逻辑
    

    print(getTimeID())

if __name__ == "__main__":
    main()
