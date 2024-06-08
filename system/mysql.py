import pymysql
import pandas as pd
import streamlit
import time
from datetime import datetime, timedelta
import pymysql
import pandas as pd
import streamlit
import time

def getTimeID():
    # 获取当前时间的时间戳（以纳秒为单位）
    nanoseconds = time.time_ns()
    # 将纳秒时间戳转换为秒和纳秒
    seconds = nanoseconds // 1_000_000_000
    nanoseconds %= 1_000_000_000
    # 将时间戳转换为标准时间格式
    standard_time = datetime.fromtimestamp(seconds)
    # 创建一个 timedelta 对象来表示纳秒的部分
    nanoseconds_delta = timedelta(microseconds=nanoseconds // 1_000)
    # 添加纳秒的部分到标准时间
    standard_time_with_ms = standard_time + nanoseconds_delta
    # 格式化时间为所需格式
    formatted_time = standard_time_with_ms.strftime("%Y-%m-%d %H:%M:%S:%f")

    return formatted_time

def insertResultTable(milliseconds,p):
     # 创建连接
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='毕业设计',
                           charset='utf8mb4')
    # 创建游标
    cursor = conn.cursor()

    try:
        # 执行插入操作
        cursor.execute("""
            INSERT INTO 模拟结果表 (数据id, 模拟值)
            VALUES (%s, %s)
        """, (milliseconds,p))
        # 提交事务
        conn.commit()
    except Exception as e:
        # 发生错误时回滚
        conn.rollback()
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()


def insertInputTable(username,text):
    
    # 创建连接
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='毕业设计',
                           charset='utf8mb4')
    # 创建游标
    cursor = conn.cursor()

    timeID=getTimeID()
    try:
        # 执行插入操作
        cursor.execute("""
            INSERT INTO 输入数据表 (数据id, 用户名, 输入数据)
            VALUES (%s, %s, %s)
        """, (timeID, username, text))
        # 提交事务
        conn.commit()
    except Exception as e:
        # 发生错误时回滚
        conn.rollback()
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()
        
    return timeID

def select(username):
    # 创建数据库连接
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='123456',
                           database='毕业设计',
                           charset='utf8mb4')

    # 创建游标
    cursor = conn.cursor()

    try:
        # 执行 SQL 查询
        
        cursor.execute("""
            SELECT  a.数据id,b.模拟值,a.输入数据
            FROM 输入数据表 a,模拟结果表 b
            where a.数据id=b.数据id and 用户名= '{}'
        """.format(username))
        
        # 获取查询结果
        result = cursor.fetchall()

        # 将查询结果转换为 DataFrame
        df = pd.DataFrame(result, columns=['数据id','模拟值','输入数据'])
        return df
    except Exception as e:
        print("查询失败:", e)
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()
    


def main():
    # 这里是你的代码逻辑
    # data=pd.DataFrame()
    # insertInputTable('lcy','dawdadwa d')

    print(select('lcy'))
    pass

if __name__ == "__main__":
    main()
