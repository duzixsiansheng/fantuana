import pandas as pd

df = pd.read_csv('test.csv')
#print(df[df['user_name']=='steve'].index.values.astype(int)[0])
#print(df.iloc[0]['B'])
for index, row in df.iterrows():
    print(row[0])
    tmp = []
    for item in row:
        
        tmp.append(item)
    #print(tmp)
    #print(tmp.count(0))

    print(df['user_name'].tolist())