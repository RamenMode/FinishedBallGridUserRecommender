import pandas as pd
import numpy as np
import UpdateWeights as UW

df = pd.read_csv('UserMatrix.csv')
df['UID'] = df.columns.values
df = df.set_index('UID')
df.columns = df.columns.map(str)
df.index = df.index.map(str)

def checkUpdateLogin(user):
    flag = False
    i = df.index.values.tolist().index(user)
    for i in range(0, df.shape[0]):
        for x in range(0, df.shape[1]):
           if(df.iloc[i, x] > 0.3):
                flag = True
        if flag == False:
            UW.updateWeights(df.index.values[i])
        flag = False
# done, working

checkUpdateLogin('313209076380074563')

#overall: Timestamps, flask, publish API, deploy to computer