# Code to separate cases of different diseases into different files
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob


raw_files = glob.glob('./Data/raw/*')
processed_files = './Data/processed/'
input_file = processed_files + 'processed_cleaned_cases.csv'
dengue_file = processed_files + 'dengue_cases.csv'
zika_file = processed_files + 'zika_cases.csv'

# read total data of cases
df_data = pd.read_csv(input_file, dtype={'provincia_id': str, 'departamento_id':str})

# separate dengue cases
df_dengue = df_data[df_data['evento_nombre'] == 'Dengue']

# separate zika cases
df_zika = df_data[df_data['evento_nombre'] == 'Zika']

# saving zika and dengue registers
df_dengue.to_csv(dengue_file, index = False)
df_zika.to_csv(zika_file, index = False)

