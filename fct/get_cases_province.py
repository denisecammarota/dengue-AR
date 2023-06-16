# Code to separate cases of dengue or zika by province
# that is, output is epidemic curve in province as a whole 
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob
import datetime

def get_cases_country(disease, id_province):
    # disease is either dengue (0) or zika (1) numeric
    # id_province is the province ID according to INDEC string
    
    if(disease == 0):
        file_cases = './Data/processed/dengue_cases.csv'
    else:
        file_cases = './Data/processed/zika_cases.csv'
        
    df_cases = pd.read_csv(file_cases, dtype={'provincia_id': str})
    df_cases = df_cases.groupby(['año','semanas_epidemiologicas'])['cantidad_casos'].sum()
    df_cases = df_cases.to_frame()
    df_cases = df_cases.reset_index()
    
    # now we have to pad and add the initial day of each epidemiological week
    # the time period of cases we are considering
    year_max = max(df_cases['año'])
    year_min = min(df_cases['año'])
    start_date = str(year_min) + '-01-01'
    end_date = str(year_max) + '-12-31'
    
    # extracting weeks and years
    dates_range = pd.date_range(start=start_date, end=end_date)
    years = dates_range.strftime('%G')
    weeks = dates_range.strftime('%V')
    
    # creating new dataframe which will have the results
    # grouping same weeks and years, using dummy column to group more easily
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
    
    
    # now we merge the empty results dataframe with the real dengue data
    # filtering and dropping the province name
    filt_cases = (df_cases['provincia_id'] == id_province)
    df_cases = df_cases[filt_cases] 
    df_cases = df_cases.drop(columns = ['provincia_id'])
    
    # renaming columns to merge
    df_cases['YEAR'] = df_cases['año']
    df_cases['WEEK'] = df_cases['semanas_epidemiologicas']
    df_cases['CASES'] = df_cases['cantidad_casos']
    df_cases = df_cases.drop(columns = ['semanas_epidemiologicas', 'año', 'cantidad_casos'])
    
    # merging and getting the final dataframe 
    df_final = df_res[['YEAR', 'WEEK']].merge(df_cases, 
                                               on=('YEAR', 'WEEK'),   
                                               how='left')
    
    # replacing NaNs by zeros
    df_final['CASES'] = df_final['CASES'].fillna(0)
    
    # adding province id into the results
    df_final['ID_PROVINCE'] = id_province
    
    return df_final


