import threading
import wget
import zipfile
import os
import datetime
import pandas as pd



def downloadCsv(time):
    print(time)
    time=time.strftime("%Y%m%d%H%M%S")
    
    url="http://data.gdeltproject.org/gdeltv2/"+time+".export.CSV.zip"
    filename=time+".export.CSV"
    
    if not os.path.exists('./csv/zip/'+filename+'.zip'):
        wget.download(url,'./csv/zip/')
        print()
        
    zip_file = zipfile.ZipFile('./csv/zip/'+filename+'.zip')
    zip_extract = zip_file.extractall('./csv/')
    
    try:
        df=pd.read_csv('./csv/'+filename, sep='\t', header=None)
        df=df[[1,29,30,31,34]]
        df.to_csv('./csv/'+filename,index=False,header=None)
    except:
        1
    

# 2015-02-18 23:00:00
def function(start,end):
    start= datetime.datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end= datetime.datetime.strptime(end, "%Y-%m-%d %H:%M:%S")
    
    while (end>=start) :
        download_tasks = []
        
        # 添加任务
        for i in range(64):
            download_tasks.append(start)
            start=start + datetime.timedelta(minutes=15)
            
        
        threads = []
        for task in download_tasks:
            thread = threading.Thread(target=downloadCsv, args=(task,))
            thread.start()
            threads.append(thread)

        # 等待所有线程完成
        for thread in threads:
            thread.join()

function("2015-03-01 00:00:00","2024-03-01 00:00:00")


