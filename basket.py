import pandas as pd
from pandas import DataFrame,Series
import matplotlib as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('ucan10.csv')

df.columns = ['visitorid','time','course_id','session_id']
df.session_id = df.session_id.astype('str')

pv_df = df.iloc[:,[0,1,2]]

pvc = pv_df.groupby(['visitorid','course_id'],as_index=False).count()

course_s = pvc.course_id.drop_duplicates().sort_values().reset_index(drop=True)

c_viewer = {}
for i in course_s:
    c_viewer[i] = DataFrame(pv_df[pv_df.course_id == i].visitorid.values)
    c_viewer[i].columns = ['visitorid']



course_pv = {}
matrix = DataFrame()
tmpdf = DataFrame()
index = 0
for i in course_s:
    course_i_df = pvc[pvc.course_id == i]
    
    for j in course_s:
        course_j_user = c_viewer[j]
        
        value = pd.merge(course_i_df,course_j_user,how='inner')['pv'].sum()
        
        tmpdf.loc[i,j] = value
    
    print(index,len(course_s))
    index += 1