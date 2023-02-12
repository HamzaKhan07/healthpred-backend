import numpy as np
import pandas as pd

df=pd.read_csv('HeadthPred-Data.csv', encoding='cp1252')

# search in df
newDf=(df.loc[df['Disease']=='Diabetes'])
desc=str(newDf.iloc[0]['Disease Description']).replace('\n', '')

medications=str(newDf.iloc[0]['Medicine and Description']).replace('\n', '')
medList=medications.split('$')
medications_name=[]
medications_desc=[]

# separate medications name and desc
for medication in medList:
    if medication!='':
        name_and_desc=medication.split(':')

        medications_name.append(name_and_desc[0])
        medications_desc.append(name_and_desc[1])

print(desc)
print(medications_name)
print(medications_desc)



