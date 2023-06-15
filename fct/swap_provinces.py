# Code that swarps provinces names and codes
# when incorrectly input into the system
# Code developed by Denise Cammarota

import numpy as np
import pandas as pd
import os
import sys 
import glob

def swap_provinces(df):
    
    # df is input dataframe to modify
    
    # reading the extra file with provinces names and codes
    prov_id_file = './Data/raw/provincias_codigos.csv'
    df_prov = pd.read_csv(prov_id_file)

    # getting lists of provinces names and codes
    prov_names = df_prov['provincia_nombre']
    prov_ids = df_prov['provincia_id']

    # casting to list
    prov_names = prov_names.to_list()
    prov_ids = prov_ids.to_list()
    
    # casting elements of lists to strings
    prov_ids = [str(i) for i in prov_ids]
    
    # replacing ids of Buenos Aires and CABA for correct ones with 0s
    prov_ids = ['02' if item == '2' else item for item in prov_ids]
    prov_ids = ['06' if item == '6' else item for item in prov_ids]
    # replacing Tierra del Fuego name for the one used in the dengue data
    prov_names = ['Tierra del Fuego' if item == 'Tierra del Fuego, Antártida e Islas del Atlántico Sur' else item for item in prov_names]
    
    # castings ids to strings to do the replacement 
    df['provincia_id'] = df['provincia_id'].astype(str)
    
    
    # correcting common CABA and Buenos Aires mistakes
    df['provincia_nombre'] = df['provincia_nombre'].replace('CABA', 'Ciudad Autónoma de Buenos Aires')
    df['provincia_id'] = df['provincia_id'].replace('CABA', 'Ciudad Autónoma de Buenos Aires')
    df['provincia_nombre'] = df['provincia_nombre'].replace('2','02')
    df['provincia_nombre'] = df['provincia_nombre'].replace('6','06')
    df['provincia_id'] = df['provincia_id'].replace('2','02')
    df['provincia_id'] = df['provincia_id'].replace('6','06')
    
    # fixing typing mistakes where a letter is accidently uppercase
    prov_names_aux = [i.lower() for i in prov_names] # lowercase province names
    df['provincia_nombre_aux'] = df['provincia_nombre'].str.lower() # lowercase column
    df['provincia_id_aux'] =  df['provincia_id'].str.lower() #lowercase column
    df['provincia_nombre_aux'] = df['provincia_nombre_aux'].replace(prov_names_aux, prov_names)
    df['provincia_id_aux'] = df['provincia_id_aux'].replace(prov_names_aux, prov_names)
    
    # replacing the correction in the original dataframe
    df['provincia_nombre'] = df['provincia_nombre_aux']
    df['provincia_id'] = df['provincia_id_aux']
    df = df.drop(columns = ['provincia_nombre_aux','provincia_id_aux'])
    
    # doing the swapping 
    df['provincia_nombre'] = df['provincia_nombre'].replace(prov_ids, prov_names)
    df['provincia_id'] = df['provincia_id'].replace(prov_names, prov_ids)

    
    return df