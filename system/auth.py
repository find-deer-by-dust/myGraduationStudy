"""Supports authentication page."""
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth

with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


def get_auth():
    return stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['pre-authorized']
    )
    

    
def updata_data(authenticator):
    import yaml
    import pandas as pd
    from yaml.loader import SafeLoader
    
    with open(r'./config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    usernames_info = []
    credentials = config.get('credentials', {}).get('usernames', {})
    for username, info in credentials.items():
        user_info = {
            '用户名': username,
            '邮箱': info.get('email', ''),
            '姓名': info.get('name', ''),
            '密码': info.get('password', '')
        }
        usernames_info.append(user_info)
    df = pd.DataFrame(usernames_info)
    import pymysql
    import pandas as pd

    # 创建连接
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           password='123456',
                           database='毕业设计',
                           charset='utf8mb4')
    # 将 DataFrame 转换为要插入的数据行的列表
    data = df.values.tolist()

    # 插入数据的 SQL 语句
    sql = "INSERT INTO 用户信息表 (用户名, 邮箱, 姓名, 密码) VALUES (%s, %s, %s, %s)"

    # 获取游标
    cursor = conn.cursor()
        
    try:
        # 执行 TRUNCATE TABLE 语句
        cursor.execute("TRUNCATE TABLE 用户信息表;")
        # 执行插入操作
        cursor.executemany(sql, data)
        # 提交事务
        conn.commit()
    except Exception as e:
        # 发生错误时回滚
        conn.rollback()
        conn.rollback()
    finally:
        # 关闭游标和连接
        cursor.close()
        conn.close()

def get_login(authenticator):
    
    # 修改过
    # authenticator.login()
    authenticator.login('登录')

    if st.session_state["authentication_status"]:
        # st.write(f'Logged username: **{st.session_state.username}**')
        st.markdown("**登录成功！**")
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')

    else:
        st.error('Username/password is incorrect')


def get_register(authenticator):
    
    if not st.session_state["authentication_status"]:
        try:
            # if authenticator.register_user(pre_authorization=False,domains=['gmail.com', 'yahoo.com','qq.com','163.com'],clear_on_submit=False):
            if authenticator.register_user(form_name='注册',preauthorization=False):
                # save_config_to_deta(config)
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('Registration is successful!')
        except Exception as e:
            st.error(e)
    else:
        st.write('登录用户无需注册服务')

def get_forgot_password(authenticator):
    if not st.session_state["authentication_status"]:

        try:
            (username_of_forgotten_password,
             email_of_forgotten_password,
             new_random_password) = authenticator.forgot_password(form_name='忘记密码')
            if username_of_forgotten_password:
                # Here you can access the forgotten password. It can also get the email and random password.
                # This random password can be sent to the user via email using email services.
                # This needs to be implemented. One email service that you can use is courier.
                st.success('Successfully get the user info.')
                st.write(f'Your new password is {new_random_password}. Keep it and update it.')
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
            else:
                st.error('Sorry username is not found.')
        except Exception as e:
            st.error(e)
    else:
        st.write('已登录的用户请修改密码')

def get_Reset_password(authenticator):
    if st.session_state["authentication_status"]:
        try:
            if authenticator.reset_password(st.session_state["username"],form_name='修改密码'):
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
                st.success('Password modified successfully')
        except Exception as e:
            st.error(e)
    else:
        st.write("您还没有登录")

def updata_detail(authenticator):
    
    if st.session_state["authentication_status"]:
        try:
            # 修改过
            # if authenticator.update_user_details(st.session_state["username"]):
            if authenticator.update_user_details(st.session_state["username"],form_name='更改信息'):
                st.success('Entries updated successfully')
                with open('./config.yaml', 'w') as file:
                    yaml.dump(config, file, default_flow_style=False)
        except Exception as e:
            st.error(e)
    else:
        st.write("您还没有登录")

