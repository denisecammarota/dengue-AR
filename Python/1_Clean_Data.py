# Code that does data cleaning
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob

# insert this new path 
sys.path.insert(1, './fct/')

# import swap_provinces function
from swap_provinces import swap_provinces

# input and output file names and paths 
raw_files = glob.glob('./Data/raw/*')
processed_files = './Data/processed/'
input_file = processed_files + 'processed_cases.csv'
output_file = processed_files + 'processed_cleaned_cases.csv'

# read total data of cases
df_data = pd.read_csv(input_file)

# swaps weeks and events that were swapped in data collection
filt_swap = df_data['semanas_epidemiologicas'].isin(['Dengue ','Dengue'])
df_aux = df_data.copy()
df_data.loc[filt_swap,'semanas_epidemiologicas'] = df_aux.loc[filt_swap,'evento_nombre']
df_data.loc[filt_swap,'evento_nombre'] = df_aux.loc[filt_swap,'semanas_epidemiologicas']

# removed space from clasifications that have 'Dengue ' 
# changes them for 'Dengue'
df_data = df_data.replace('Dengue ','Dengue')
# and also renames Zika cases
df_data = df_data.replace('Enfermedad por Virus del Zika','Zika')

# fixing provinces names and codes 

# swapping province names and ids when wrong
df_data = swap_provinces(df_data)

# saving the final result 

# check for processed files directory
if not os.path.exists(processed_files):
    os.makedirs(processed_files)

# save final processed data
df_data.to_csv(output_file,index=False)