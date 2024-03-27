import pandas as pd

# 读取Excel文件
df = pd.read_excel('price.xlsx', header=None)

# 将第一列转换为datetime格式
df[df.columns[0]] = pd.to_datetime(df[df.columns[0]], format='%Y/%m/%d')

# 设置第一列为索引
df.set_index(df.columns[0], inplace=True)

# 生成完整的日期范围
date_range = pd.date_range(start=df.index.min(), end=df.index.max())

# 重新索引DataFrame以包含完整的日期范围
df = df.reindex(date_range)

# 使用插值方法填充缺失值（这里使用的是向前填充）
df = df.interpolate(method='time')

# 将处理后的 DataFrame 保存为新的 Excel 文件
df.to_excel('new.xlsx')

