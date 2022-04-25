import streamlit as st
import pandas as pd
import numpy as np
import os
import time


st.set_page_config(layout="centered")
st.title('Label Tool')

#
#汉堡贴纸 甜品贴纸 奶茶贴纸 韩餐日料贴纸 川菜贴纸 粤式早茶 地方特色贴纸 火锅贴纸 烤串贴纸 香锅麻辣烫贴纸 面粉贴纸 异域风味贴纸 小吃贴纸
#

df = pd.read_csv('fantuan_after.csv')
form = st.form(key="annotation",clear_on_submit = True)
with form:
    cols = st.columns((2))
    user_name = cols[0].text_input('微信名')
    user_ID = cols[1].text_input('微信号')
    cols = st.columns((4))
    A = cols[0].number_input('汉堡贴纸',min_value=-100,max_value=1000,step=1,value=0)
    B = cols[1].number_input('甜品贴纸',min_value=-100,max_value=1000,step=1,value=0)
    C = cols[2].number_input('奶茶贴纸',min_value=-100,max_value=1000,step=1,value=0)
    D = cols[3].number_input('韩餐日料贴纸',min_value=-100,max_value=1000,step=1,value=0)
    cols = st.columns((4))
    E = cols[0].number_input('川菜贴纸',min_value=-100,max_value=1000,step=1,value=0)
    F = cols[1].number_input('粤式早茶',min_value=-100,max_value=1000,step=1,value=0)
    
    G = cols[2].number_input('地方特色贴纸',min_value=-100,max_value=1000,step=1,value=0)
    H = cols[3].number_input('火锅贴纸',min_value=-100,max_value=1000,step=1,value=0)
    cols = st.columns((4))
    I = cols[0].number_input('烤串贴纸',min_value=-100,max_value=1000,step=1,value=0)
    J = cols[1].number_input('香锅麻辣烫贴纸',min_value=-100,max_value=1000,step=1,value=0)
    K = cols[2].number_input('面粉贴纸',min_value=-100,max_value=1000,step=1,value=0)
    L = cols[3].number_input('异域风味贴纸',min_value=-100,max_value=1000,step=1,value=0)
    cols = st.columns((4))
    M = cols[0].number_input('小吃贴纸',min_value=-100,max_value=1000,step=1,value=0)

    addrow = {'微信名':user_name,'微信号':user_ID,'汉堡贴纸':A,'甜品贴纸':B,'奶茶贴纸':C,
                '韩餐日料贴纸':D,'川菜贴纸':E,'粤式早茶':F,'地方特色贴纸':G,'火锅贴纸':H
                ,'烤串贴纸':I,'香锅麻辣烫贴纸':J,'面粉贴纸':K,'异域风味贴纸':L,'小吃贴纸':M}
    submitted = st.form_submit_button(label="submit!")
    if submitted:
        if addrow['微信名'] != '' and addrow['微信号'] != '':
            idList = df['微信号'].tolist()
            if  addrow['微信号'] in idList :
                index = df[df['微信号']==addrow['微信号']].index.values.astype(int)[0]
                #update
                df.at[index,'汉堡贴纸'] = df.iloc[index]['汉堡贴纸'] + addrow['汉堡贴纸']
                df.at[index,'甜品贴纸'] = df.iloc[index]['甜品贴纸'] + addrow['甜品贴纸']
                df.at[index,'奶茶贴纸'] = df.iloc[index]['奶茶贴纸'] + addrow['奶茶贴纸']
                df.at[index,'韩餐日料贴纸'] = df.iloc[index]['韩餐日料贴纸'] + addrow['韩餐日料贴纸']
                df.at[index,'川菜贴纸'] = df.iloc[index]['川菜贴纸'] + addrow['川菜贴纸']
                df.at[index,'粤式早茶'] = df.iloc[index]['粤式早茶'] + addrow['粤式早茶']
                df.at[index,'地方特色贴纸'] = df.iloc[index]['地方特色贴纸'] + addrow['地方特色贴纸']
                df.at[index,'火锅贴纸'] = df.iloc[index]['火锅贴纸'] + addrow['火锅贴纸']
                df.at[index,'烤串贴纸'] = df.iloc[index]['烤串贴纸'] + addrow['烤串贴纸']
                df.at[index,'香锅麻辣烫贴纸'] = df.iloc[index]['香锅麻辣烫贴纸'] + addrow['香锅麻辣烫贴纸']
                df.at[index,'面粉贴纸'] = df.iloc[index]['面粉贴纸'] + addrow['面粉贴纸']
                df.at[index,'异域风味贴纸'] = df.iloc[index]['异域风味贴纸'] + addrow['异域风味贴纸']
                df.at[index,'小吃贴纸'] = df.iloc[index]['小吃贴纸'] + addrow['小吃贴纸']
            else:
                df = df.append(addrow, ignore_index= True)
            df.to_csv('fantuan_after.csv', index=False)
            df = pd.read_csv('fantuan_after.csv')
        else:
            st.text('Name or ID cannot be empty!')
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')
dl = convert_df(df)
if st.button('show csv'):   
    st.write(df)
st.download_button(label=' Download Current Result',
                                data=dl ,
                                file_name= 'label.csv')

grab = st.text_input('微信名')
if st.button('get'):
    nameList = df['微信名'].tolist()
    if grab in nameList:
       gindex=df[df['微信名']==grab].index.values.astype(int)[0] 
       grab_df = df.loc[[gindex]]
       st.write(grab_df)
    else:
        st.text('No that person')

if st.button('check'):
    name_price = []
    for index, row in df.iterrows():
    
        tmp = []
        for item in row:
            
            tmp.append(item)
        if tmp.count(0) < 11:
            name_price.append(tmp[0])
    st.write(name_price)

delete_name = st.text_input('delete 微信号')
if st.button('Delete That Line!'):
    if (delete_name in df['微信号'].tolist()):
        st.text('deleting...')
        df.drop(df[df['微信号'] == delete_name].index,inplace=True)
        df.to_csv('fantuan_after.csv', index=False)