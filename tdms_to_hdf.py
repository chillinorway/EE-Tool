# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 16:14:56 2022

@author: Aleksander
"""

import scipy.io as sio
import h5py
import numpy as np
import pandas as pd
import nptdms
from collections import defaultdict, deque
import time
start_time = time.time()


sig_names = ['en', 'to', 'tre']

chunk_1 = np.random.randn(3,200000).T
chunk_2 = np.random.randn(3,100000).T

chunks = [chunk_1, chunk_2]
 
df1 = pd.DataFrame(chunk_1, columns=['en','to','tre'])
df2 = pd.DataFrame(chunk_2, columns=['en','to','tre'])
chunks = [df1,df2]


groups_dict = {}
dataset_dict = {}
with h5py.File('hdf.h5', 'a') as hdf:
    # Init
    hdf_group = hdf.create_group('data')
    for sig in sig_names:
        # Om dtype er 16 klarer ikke HDFview å se det. Kanskje matlab kan?
        dataset_dict[sig] = hdf_group.create_dataset(sig, shape=(0), compression="gzip", chunks=True, maxshape=(None,), dtype=np.float32)
    for chunk in chunks:
        for col_name in chunk:
            data = np.array(chunk[col_name]).astype(np.float16)
            dataset_dict[col_name].resize((dataset_dict[col_name].shape[0] + data.shape[0]), axis=0)
            dataset_dict[col_name][-data.shape[0]:] = data



readback_data = []
with h5py.File('hdf.h5', 'r') as f:
    group_keys = list(f.keys())
    for group_key in group_keys:
        data_sets = list(f[group_key])
        for data_set in data_sets:

            # ds_obj = f[data_set]
            ds_arr = f[f'{group_key}/{data_set}'][()]
            readback_data.append(ds_arr)



#%%
# import scipy.io as sio
# import h5py
# import numpy as np
# import pandas as pd
# import nptdms
# from collections import defaultdict, deque
# import time
# start_time = time.time()


# sig_names = ['en', 'to', 'tre']

# chunk_1 = np.random.randn(3,100000).T
# chunk_2 = np.random.randn(3,100000).T

# chunks = [chunk_1, chunk_2]
 
# df1 = pd.DataFrame(chunk_1, columns=['en','to','tre'])
# df2 = pd.DataFrame(chunk_2, columns=['en','to','tre'])
# chunks = [df1,df2]



# # chunk_1 = np.random.randn(3,100000)
# # chunk_2 = np.random.randn(3,100000)1

# # chunks = [chunk_1, chunk_2]

# data_dict = {}



# groups_dict = {}
# dataset_dict = {}
# with h5py.File('hdf.h5', 'a') as hdf:
#     # Init
#     for group in range((3)):
#         group = str(group)
#         groups_dict[group] = hdf.create_group(group)
        
#     for sig in sig_names:
        
#         dataset_dict[sig] = groups_dict[group].create_dataset(sig, shape=(0,), compression="gzip", chunks=True, maxshape=(None,), dtype=np.float16)

#     # for group_dict in groups_dict:
#         # gr = groups_dict[group_dict]
#         # for chunk in chunks:
#             # for col_name in chunk:
#                 # data = np.array(chunk[col_name]).astype(np.float16)
                
#                 # groups_dict[group]
                
#                 # dataset_dict[col_name].resize((dataset_dict[col_name].shape[0] + data.shape[0]), axis=0)
#                 # dataset_dict[col_name][-data.shape[0]:] = data
    
            
        























