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

df = pd.read_csv('test.csv')
form = st.form(key="annotation",clear_on_submit = True)
with form:
    cols = st.columns((2))
    user_name = cols[0].text_input('User name')
    user_ID = cols[1].text_input('User ID')
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

    addrow = {'user_name':user_name,'user_ID':user_ID,'A':A,'B':B,'C':C,
                'D':D,'E':E,'F':F,'G':G,'H':H
                ,'I':I,'J':J,'K':K,'L':L,'M':M}
    submitted = st.form_submit_button(label="submit!")
    if submitted:
        if addrow['user_name'] != '' and addrow['user_ID'] != '':
            idList = df['user_ID'].tolist()
            if  addrow['user_ID'] in idList :
                index = df[df['user_ID']==addrow['user_ID']].index.values.astype(int)[0]
                #update
                df.at[index,'A'] = df.iloc[index]['A'] + addrow['A']
                df.at[index,'B'] = df.iloc[index]['B'] + addrow['B']
                df.at[index,'C'] = df.iloc[index]['C'] + addrow['C']
                df.at[index,'D'] = df.iloc[index]['D'] + addrow['D']
                df.at[index,'E'] = df.iloc[index]['E'] + addrow['E']
                df.at[index,'F'] = df.iloc[index]['F'] + addrow['F']
                df.at[index,'G'] = df.iloc[index]['G'] + addrow['G']
                df.at[index,'H'] = df.iloc[index]['H'] + addrow['H']
                df.at[index,'I'] = df.iloc[index]['I'] + addrow['I']
                df.at[index,'J'] = df.iloc[index]['J'] + addrow['J']
                df.at[index,'K'] = df.iloc[index]['K'] + addrow['K']
                df.at[index,'L'] = df.iloc[index]['L'] + addrow['L']
                df.at[index,'M'] = df.iloc[index]['M'] + addrow['M']
            else:
                df = df.append(addrow, ignore_index= True)
            df.to_csv('test.csv', index=False)
            df = pd.read_csv('test.csv')
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

grab = st.text_input('User name')
if st.button('get'):
    nameList = df['user_name'].tolist()
    if grab in nameList:
       gindex=df[df['user_name']==grab].index.values.astype(int)[0] 
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

delete_name = st.text_input('delete ID')
if st.button('Delete That Line!'):
    if (delete_name in df['user_ID'].tolist()):
        st.text('deleting...')
        df.drop(df[df['user_ID'] == delete_name].index,inplace=True)
        df.to_csv('test.csv', index=False)