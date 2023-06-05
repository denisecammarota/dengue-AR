# Code to separate cases of different diseases into different files
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob


raw_files = glob.glob('./Data/raw/*')
processed_files = './Data/processed/'
final_file = processed_files + 'processed_cases.csv'

# read total data of cases
df_data = pd.read_csv(final_file)

# filter registers that have a evento_nombre wrong

# separate dengue cases


# separate zika cases

