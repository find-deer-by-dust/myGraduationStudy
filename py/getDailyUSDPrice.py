import pandas as pd

# 读取Excel文件
df = pd.read_excel('./price/Prices.xlsx', header=None, sheet_name='Daily')

# 提取需要的数据范围
df = df.iloc[6:, 2:4]
df = df.rename(columns={2: 'Date', 3: 'Price'})
print(df.head())

# 将第一列转换为datetime格式
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# 设置第一列为索引
df.set_index('Date', inplace=True)

# 将第二列转换为数值类型
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# 生成完整的日期范围
date_range = pd.date_range(start=df.index.min(), end=df.index.max())

# 重新索引DataFrame以包含完整的日期范围
df = df.reindex(date_range)

# 使用插值方法填充缺失值（这里使用的是向前填充）
df = df.interpolate(method='time')

# 将处理后的 DataFrame 保存为新的 Excel 文件
df.to_excel('./price/DailyUSDPrice.xlsx', header=None)


