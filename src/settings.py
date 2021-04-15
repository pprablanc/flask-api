import os
import pandas as pd
import numpy as np
import netCDF4 as nc
import matplotlib.pyplot as plt


# def load_data():
'''Description: load netcdf4 files, store it in a dataframe and preprocess the data.

Return: df (DataFrame):
            columns:
                'time'      (int):                  row year
                'cereal'    (str):                  cereal type
                'yield_map' (numpy masked array):   yield map
                'mean_yield' (str):                 mean yield for a given map
'''
print('Loading files ...')
full_dataset = dict(time=[], type=[], nc=[])
path = 'data/raw'
with os.scandir(path) as dir_data:
    for sub_dir_data in dir_data:
        for f in os.scandir(os.path.join(path, sub_dir_data.name)):
            path_f = os.path.join(path, sub_dir_data.name, f.name)
            time = int(f.name.split('_')[1][:4])
            full_dataset['time'].append(time)
            full_dataset['type'].append(sub_dir_data.name)
            full_dataset['nc'].append(nc.Dataset(path_f, 'r'))
df = pd.DataFrame(full_dataset)
print('Files loaded ...')

# Dataset preprocessing
print('Dataset preprocessing ...')
df.sort_values(["type", "time"], ignore_index=True, inplace=True)  # sorting by time

# Add a 'yield' column for display purpose
# Remask with -1/0 to avoid flatten amplitude
mask_value = 0
list_var = []
for row in df["nc"]:
    row_tmp = row["var"][:]
    row_tmp.set_fill_value(-mask_value)
    mask = row_tmp.mask
    list_var.append(np.ma.masked_array(row_tmp.filled(fill_value=-mask_value), mask))
df["yield_map"] = list_var

# add yield_mean to avoid repeating code
df["yield_mean"] = df["yield_map"].apply(lambda row: row.data.mean())
df["id"] = df.index.values

# nc column not necessary anymore
df.drop("nc", axis="columns", inplace=True)
print('Data import completed.')
    # return df
