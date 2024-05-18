import pandas as pd

files=['道琼斯工业平均指数历史数据','利率','消费者价格指数']

for file in files:
    newFile='./newCsv/new'+file+'.csv'
    file='./newCsv/'+file+'.csv'

    
    # 读取CSV文件
    df = pd.read_csv(file)

    df = df.iloc[:,0:2]
    df.columns = ['Date', 'Data']
    
    # 将第一列转换为datetime格式
    df['Date'] = pd.to_datetime(df['Date'])
    # 去除重复的日期，只保留最后一次出现的记录
    df = df.drop_duplicates(subset='Date', keep='last')

    # 设置第一列为索引
    df.set_index('Date', inplace=True)

    # 将第二列转换为数值类型
    
    if isinstance(df['Data'][0], str):
        df['Data'] = df['Data'].str.replace(',', '')    
    df['Data'] = pd.to_numeric(df['Data'], errors='coerce')


    # 生成完整的日期范围
    date_range = pd.date_range(start=df.index.min(), end=df.index.max())

    # 重新索引DataFrame以包含完整的日期范围
    df = df.reindex(date_range)

    # 使用插值方法填充缺失值（这里使用的是时间插值）
    df = df.interpolate(method='time')

    print(df.head())

    df.to_csv(newFile)

