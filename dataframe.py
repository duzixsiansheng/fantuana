import pandas as pd

df = pd.read_csv('label.csv')
df.drop(columns=['微信名'])

# df.fillna(0)
# #df['汉堡贴纸','甜品贴纸','奶茶贴纸','韩餐日料贴纸','川菜贴纸','粤式早茶','地方特色贴纸','火锅贴纸','烤串贴纸','香锅麻辣烫贴纸','面粉贴纸','异域风味贴纸','小吃贴纸'] = df['汉堡贴纸','甜品贴纸','奶茶贴纸','韩餐日料贴纸','川菜贴纸','粤式早茶','地方特色贴纸','火锅贴纸','烤串贴纸','香锅麻辣烫贴纸','面粉贴纸','异域风味贴纸','小吃贴纸'].fillna(0)
# df['汉堡贴纸'] = df['汉堡贴纸'].fillna(0).astype(int)
# df['甜品贴纸'] = df['甜品贴纸'].fillna(0).astype(int)
# df['奶茶贴纸'] = df['奶茶贴纸'].fillna(0).astype(int)
# df['韩餐日料贴纸'] = df['韩餐日料贴纸'].fillna(0).astype(int)
# df['川菜贴纸'] = df['川菜贴纸'].fillna(0).astype(int)
# df['粤式早茶'] = df['粤式早茶'].fillna(0).astype(int)
# df['地方特色贴纸'] = df['地方特色贴纸'].fillna(0).astype(int)
# df['火锅贴纸'] = df['火锅贴纸'].fillna(0).astype(int)
# df['烤串贴纸'] = df['烤串贴纸'].fillna(0).astype(int)
# df['香锅麻辣烫贴纸'] = df['香锅麻辣烫贴纸'].fillna(0).astype(int)
# df['面粉贴纸'] = df['面粉贴纸'].fillna(0).astype(int)
# df['异域风味贴纸'] = df['异域风味贴纸'].fillna(0).astype(int)
# df['小吃贴纸'] = df['小吃贴纸'].fillna(0).astype(int)

#print(df[df['user_name']=='steve'].index.values.astype(int)[0])
#print(df.iloc[0]['B'])
df.to_csv('fantuan_after1.csv', index=False)