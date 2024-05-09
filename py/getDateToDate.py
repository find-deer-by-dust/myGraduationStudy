import pandas as pd
import numpy as np

start_date = 20160101
end_date = 20170101


# 指定 CSV 文件路径
csv_file_path = './newCsv/all.csv'

# 指定每次读取的行数
chunk_size = 10000000

# 使用 Pandas 分块读取 CSV 文件
reader = pd.read_csv(csv_file_path, chunksize=chunk_size, header=None)

fileName=start_date+"_to_"+end_date+".csv"

# 逐块读取并打印部分内容
for chunk in reader:
    # print(chunk)
    chunk=chunk[(chunk[0] >= start_date) & (chunk[0] < end_date)]
    
    if not chunk.empty:
        # print(chunk.head())  # 打印每个块的前几行内容
        chunk.to_csv('./newCsv/'+fileName, mode='a', header=False, index=False)
        
print("finished "+fileName)

df=pd.read_csv('./newCsv/'+fileName, header=None)

print(df.head())

# 对列表进行排序
l = list(set(df[0]))
l.sort()

newdf=pd.DataFrame()

for i in l:

    print(i)
    tmp= df[df[0]==i].copy()

    # 删除每一行最开始的时间
    tmp.drop(columns=[0], inplace=True)

    # 获取 DataFrame 的值并展平为一维数组
    one_row_data = tmp.values.flatten()
  
    # 在数组的开头插入时间
    one_row_data = np.insert(one_row_data, 0, i)
    
    # 将一维数组转换为 DataFrame，并转置
    one_row_df = pd.DataFrame([one_row_data])
    
    # print(one_row_df)
    newdf=pd.concat([newdf,one_row_df])
    
print(newdf.head())

newdf.to_csv('./newCsv/new'+fileName, index=False)