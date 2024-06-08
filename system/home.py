import streamlit as st
import csv
import pymysql
import os
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy as np
from datasets import Dataset
import streamlit_echarts
from streamlit_option_menu import option_menu
from auth import (get_auth, get_login, get_register,
                          get_forgot_password,get_Reset_password,updata_detail,updata_data)
from function import *
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker


options = ['数据模拟及可视化', '历史记录' , '个人信息']
icons = ['house', 'journal-text', 'gear']
startPage=2
st.set_option('deprecation.showPyplotGlobalUse', False)
plt.rcParams['font.family'] = 'SimHei'  # 替换为你选择的字体


with st.sidebar:
    selected = option_menu(f'欢迎来到本系统', options, icons=icons,
                           menu_icon="cast", default_index=startPage)
    
    

if selected == "历史记录":
    
    authenticator = get_auth()
    username=st.session_state['username']
    df=select(username)
    
    with st.form('my_form_3'):
        
        st.markdown("### 查看您的历史记录")
        st.write(df)
    
        df1=df['数据id']
        
        genre = st.selectbox(
            "选择您的历史记录",
            df1,  # 也可以用元组
            index=0
        )
         # 添加提交按钮
        submitted = st.form_submit_button("提交")

        # 处理表单提交
        if submitted:
            # 根据用户选择的数据 ID 获取相应的样本
            selected_sample = df[df['数据id'] == genre]
            
            # 显示选择信息
            st.write("您选择的历史记录是:")
            st.write(selected_sample)

            valStr=selected_sample.iat[0,1]
            
            values = [float(x) for x in valStr.split()]

            # 将选定的数据转换为 DataFrame
            newDF = pd.DataFrame(values)
            newDF=getNewDF(newDF)
            
            # 调用函数生成图形对象
            plot = generate_plot(newDF)
            # 将图形对象传递给Streamlit的函数
            st.pyplot(plot)
            
    
    
    
    

if selected == '数据模拟及可视化':
    
    authenticator = get_auth()
    username=st.session_state['username']
    st.markdown("# 基于深度学习的黄金价格模拟系统")
    st.markdown("***")
    st.markdown(" ")
    # df=f4_1(st.session_state['username'])
    
    st.markdown("**数据格式**为:消费者价格指数、利率、道琼斯工业平均指数、事件1的QuadClass、事件1的GoldsteinScale、事件1的NumMentions、事件1的AvgTone、事件2的QuadClass、事件2的GoldsteinScale、事件2的NumMentions、事件2的AvgTone....")
    st.markdown("***")
    st.markdown(" ")

    r1, r2, r3 = st.columns([1, 8, 1])
    
    with r2:
        st.markdown("## 输入数据")
        st.markdown("输入数据中，每个标签之前间以**空格**作为分割")
        st.markdown("此处输入假设未来发生的情况,点击**开始模拟**后即可获得结果")
        st.markdown("如果需要模拟多天的价格，输入每天数据后以'|'作为分割")
        
        with st.form("my_form_1"):
            # st.title("")
            st.markdown("### 价格模拟")
            text = st.text_input("请输入假设数据:")
            x=st.form_submit_button("开始模拟")
            res=''
            if x:
                if text == "":
                    st.write("请输入假设数据")
                else:
                    df=simulate(text)
                    st.write("价格模拟结果为:")
                    st.dataframe(df)
                    # 调用函数生成图形对象
                    plot = generate_plot(df)
                    # 将图形对象传递给Streamlit的函数
                    st.pyplot(plot)
                    
                    save2mysql(username,text,df)
                    
                    
    # excel比较特殊，读取的时候先要read()
    st.write(" ")
    st.markdown('***')
    st.markdown(" ")
    
    r1, r2, r3 = st.columns([1, 8, 1])

    with r2:
        st.markdown("## 上传数据")
        st.markdown("输入数据中，每个标签之前以单元格作为作为分割")
        st.markdown("不同行为不同天")
        st.markdown("上传格式为不带header的EXCEL文件,点击**开始模拟**后即可获得结果")
        st.write(" ")
        
        with st.form("my_form_5"):
            st.markdown("### 请上传您的数据")
            uploaded_file = st.file_uploader("请选择文件：", \
                                             accept_multiple_files=False, type=["xlsx", "xls"])
            x = st.form_submit_button("开始模拟")
            
            if x:
                if uploaded_file is not None:
                    df = pd.read_excel(uploaded_file.read(),header=None)
                    text= df.astype(str).apply(lambda x: ' '.join(x), axis=1).str.cat(sep=' | ')

                    df=simulate(text)
                    st.write("价格模拟结果为:")
                    st.dataframe(df)
                    
                    # 调用函数生成图形对象
                    plot = generate_plot(df)
                    # 将图形对象传递给Streamlit的函数
                    st.pyplot(plot)
                    
                    save2mysql(username,text,df)
                else:
                    st.write("请先上传您的数据")
                    
          
    st.write(" ")
    st.markdown('***')
    st.markdown(" ")
    r1, r2, r3 = st.columns([1, 8, 1])
    
    with r2:
        st.markdown("## 随机数据")
        st.markdown("可以使用随机数的方式来将其作为输入")
        st.markdown("点击**开始模拟**后即可获得结果")
        st.write(" ")
        
        with st.form("my_form_51"):
            st.markdown("### 生成随机数据")

            # r4,r5 = st.columns([10, 1])
            # with r4:
            days = st.text_input("请输入随机生成的天数(默认10天，最少1天)",value=10)
                
            x = st.form_submit_button("开始模拟")
            if x:
                days=int(days)
                text = ' '.join(map(str, getRandomNumbers()))
                
                for i in range(days-1):
  
                    # 将随机数序列转换为字符串，并用空格作为分隔符
                    random_numbers_str = ' '.join(map(str, getRandomNumbers()))

                    text=text+'|'+random_numbers_str
                    
                
                df=simulate(text)
                st.write("价格模拟结果为:")
                st.dataframe(df)
                
                # 调用函数生成图形对象
                plot = generate_plot(df)
                # 将图形对象传递给Streamlit的函数
                st.pyplot(plot)
                
                save2mysql(username,text,df)
                

if selected == "个人信息":
    
    authenticator = get_auth()
    username=st.session_state['username']
    
    # tab1, tab2, tab3, tab4,tab5= st.tabs(['登录', '注册', '忘记密码','重置密码','更改信息'])
    tab1, tab2, tab3, tab4= st.tabs(['登录', '注册', '忘记密码','修改密码'])
    updata_data(authenticator)
    
    
    with tab1:
        get_login(authenticator)
        if st.session_state["authentication_status"]:
            st.write(f'Logged username: **{st.session_state.username}**')
            st.write(f'Logged name: **{st.session_state.name}**')
            updata_data(authenticator)
    
    with tab2:
        get_register(authenticator)
        updata_data(authenticator)
    with tab3:
        get_forgot_password(authenticator)
        updata_data(authenticator)
    with tab4:
        get_Reset_password(authenticator)
        updata_data(authenticator)
        
    # with tab5:
    #     updata_detail(authenticator)
    #     updata_data(authenticator)