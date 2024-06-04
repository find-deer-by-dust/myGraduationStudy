import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def getData(fl,start,end):
    
    # 读取Excel文件
    df = pd.read_csv('./newCsv/new'+fl+'.csv')
    # 更改列名
    df.columns = ['time','data']

    # print(df.head())

    # 设置第一列为索引
    df = df.set_index('time')

    # 将索引列重命名为'time'
    df.index.names = ['time']

    index_pos1 = df.index.get_loc(start)
    index_pos2 = df.index.get_loc(end)

    return df.iloc[index_pos1:index_pos2]

start='2018-01-01'
end='2018-02-01'

# i ='消费者价格指数'
i ='利率'
data=getData(i,start,end)
# print(data.head())
# print(data.size)
plt.plot(data.index, data['data'],label=i)
    
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体

# 绘制折线图
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(10))


# 添加标题和标签
plt.title(i+' 从 '+start+' 到 '+end)
plt.xlabel('Date')
# plt.ylabel(fl)

plt.legend()
# 显示网格
plt.grid(True)

# 自动旋转日期标签以避免重叠
plt.xticks(rotation=45)

# 显示图形
plt.show()
