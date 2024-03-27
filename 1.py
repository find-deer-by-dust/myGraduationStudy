import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('new.xlsx', header=None)

# 假设第一列是 x 轴数据，第二列是 y 轴数据
x_data = df.iloc[:, 0]
y_data = df.iloc[:, 1]

# 绘制折线图
plt.plot(x_data, y_data)
plt.show()