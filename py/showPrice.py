import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件
df = pd.read_excel('./price/DailyUSDPrice.xlsx', header=None)

# 设置第一列为索引
df = df.set_index(0)

# 更改列名
df.columns = ['price']

# 将索引列重命名为'time'
df.index.names = ['time']

start='2016-01-01'
end='2017-01-01'
index_pos1 = df.index.get_loc(start)
index_pos2 = df.index.get_loc(end)

data=df.iloc[index_pos1:index_pos2]

import matplotlib.pyplot as plt

# 绘制折线图
plt.plot(data.index, data['price'])

# 添加标题和标签
plt.title('Price Trend from '+start+' to '+end)
plt.xlabel('Date')
plt.ylabel('Price')

# 显示网格
plt.grid(True)

# 自动旋转日期标签以避免重叠
plt.xticks(rotation=45)

# 显示图形
plt.show()
