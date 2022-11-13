import pandas as pd

data = pd.read_csv('data.csv').to_dict('records')
for i in data:
    i['Address'] = i['Address'].replace('\t', '').replace('\n', '').replace('\r', ' ')


ty = pd.DataFrame(data)
ty.to_csv('data2.csv',index=False)