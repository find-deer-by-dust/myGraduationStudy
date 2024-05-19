import pandas as pd
import numpy as np

def all2Date2Date(start_date,end_date,csv_file_path = './newCsv/20160101_to_20230101.csv'):

    # 指定每次读取的行数
    chunk_size = 10000000

    # 使用 Pandas 分块读取 CSV 文件
    reader = pd.read_csv(csv_file_path, chunksize=chunk_size, header=None)

    fileName=str(start_date)+"_to_"+str(end_date)+".csv"

    # 逐块读取并打印部分内容
    for chunk in reader:
        # print(chunk)
        chunk=chunk[(chunk[0] >= start_date) & (chunk[0] < end_date)]
        
        if not chunk.empty:
            # print(chunk.head())  # 打印每个块的前几行内容
            chunk.to_csv('./newCsv/'+fileName, mode='a', header=False, index=False)
            
    print("finished "+fileName)


def Date2Date2sizeDate2Date(start_date,end_date,size):
    
    start_date=str(start_date)
    end_date=str(end_date)
    size=int(size)
    
    file='./newCsv/'+start_date+"_to_"+end_date+".csv"
    newFile='./newCsv/'+str(size)+'_'+start_date+"_to_"+end_date+".csv"

    df=pd.read_csv(file, header=None)
    print(df.head())

    days = list(set(df[0]))
    days.sort()
    
    newdf=pd.DataFrame()
    
    for i in days:

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

        one_row_df= one_row_df.iloc[:, :size]
        # print(one_row_df)
        newdf=pd.concat([newdf,one_row_df])
        
    print(newdf.head())
    
    newdf.to_csv(newFile,header=False, index=False)



start_date = 20180101
end_date = 20190601
size=1+100*(60/15)*24

all2Date2Date(start_date,end_date)

Date2Date2sizeDate2Date(start_date,end_date,size)