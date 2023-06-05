# Code that reads and concatenates all publically available data in one file
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob


raw_files = glob.glob('./Data/raw/*')
processed_files = './Data/processed/'
output_file = processed_files + 'processed_cases.csv'

df_total = pd.DataFrame()
counter = 0 

for raw_file in raw_files:
    df_tmp = pd.read_csv(raw_file)
    if(counter == 4): # drops extra column on this dataframe
        df_tmp = df_tmp.drop(columns = ['Unnamed: 10'])
    if(sum('anio' == df_tmp.keys()) or sum('ano' == df_tmp.keys())): # renames year
        df_tmp.rename(columns = {'anio':'año', 'ano': 'año'}, inplace = True)
    df_total = pd.concat([df_total,df_tmp],axis = 0)
    counter = counter + 1

# corrects index and then drops extra column
df_total = df_total.reset_index()    
df_total = df_total.drop(columns = ['index'])

# check for processed files directory
if not os.path.exists(processed_files):
    os.makedirs(processed_files)

# save final processed data
df_total.to_csv(output_file,index=False)