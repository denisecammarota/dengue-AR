# Code to separate national cases of dengue or zika, national count 
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob
import datetime

#def get_cases_country(disease):
    # disease is either dengue or zika
    
file_dengue = './Data/processed/dengue_cases.csv'
df_dengue = pd.read_csv(file_dengue)
    
df_dengue = df_dengue.groupby(['provincia_id','año','semanas_epidemiologicas'])['cantidad_casos'].sum()
df_dengue = df_dengue.to_frame()
df_dengue = df_dengue.reset_index()

# now we have to pad and add the initial day of each epidemiological week
# the time period of cases we are considering
year_max = max(df_dengue['año'])
year_min = min(df_dengue['año'])
start_date = str(year_min) + '-01-01'
end_date = str(year_max) + '-12-31'

# extracting weeks and years
dates_range = pd.date_range(start=start_date, end=end_date)
years = dates_range.strftime('%G')
weeks = dates_range.strftime('%V')

# creating new dataframe which will have the results
df_res = pd.DataFrame({'YEAR': years, 'WEEK':weeks})
df_res['YEAR'] = df_res['YEAR'].astype(int)
df_res['WEEK'] = df_res['WEEK'].astype(int)
df_res['CASES'] = 0
df_res = df_res.groupby(['YEAR','WEEK'])['CASES'].sum()
df_res = df_res.to_frame()
df_res = df_res.reset_index()

# now we put the first day of the week in this dataframe 
df_res['FIRST_DAY'] = pd.date_range(start=start_date, end = end_date, freq='W-MON')
df_res = df_res[['YEAR','WEEK','FIRST_DAY', 'CASES']]

