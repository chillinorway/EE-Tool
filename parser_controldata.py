# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:08:02 2022

@author: Aleksander
"""

import pandas as pd
import matplotlib.pyplot as plt

with open('./go/221202T140146.csv', 'r') as f:
    data = f.readlines()
    data = [el for el in data if el != '\n']
    data = [el.split() for el in data]
    new = []
    for l in data:
        data = [int(el) for el in l] 
        new.append(data)

def get_bit_in_byte(byte, pos):
    return (byte >> pos) & 1


results={'a':[],
         'b': [],
         'c': [],
         'd': [],
         'e1': [],
         'e2': [],
         'f': []}

for l in new:
    if len(l) == 21:
        msb_1 = l[8]
        msb_2 = l[17]
        l = l[1:20]
        
        # byte_array = (((msb_1&8!=0) << 7) | (l[0] << 6 | ((msb_1&7!=0) <<7) | l[1]))
        # results['a'].append(byte_array)
        
        b1 = l[0] | (get_bit_in_byte(msb_1, 8) << 8)
        b2 = l[1] | (get_bit_in_byte(msb_1, 7) << 8)
        byte_array = b1 << 8 | b2
        # byte_array = (l[0] << 8) | (l[1]) | get_bit_in_byte(msb_1, 7) << 16
        results['a'].append(byte_array)
        
        b1 = l[2] | (get_bit_in_byte(msb_1, 6) << 8)
        b2 = l[3] | (get_bit_in_byte(msb_1, 5) << 8)
        byte_array = (b1 << 8 | b2) / 1000.0
        # byte_array = ((l[2] << 8) | (l[3] << 0) | (get_bit_in_byte(msb_1, 6) << 16)) / 1.0
        results['b'].append( byte_array)
        
        
        b1 = l[4] | (get_bit_in_byte(msb_1, 4) << 8)
        b2 = l[5] | (get_bit_in_byte(msb_1, 3) << 8)
        byte_array = (b1 << 8 | b2) / 100.0
        # byte_array = ((l[4] << 8) | (l[5] << 0) | (get_bit_in_byte(msb_1, 5) << 16)) / 100.0  
        results['c'].append( byte_array)
        
        
        b1 = l[6] | (get_bit_in_byte(msb_1, 2) << 8)
        b2 = l[7] | (get_bit_in_byte(msb_1, 1) << 8)
        byte_array = (b1 << 8 | b2) / 100.0
        # byte_array = ((l[6] << 8) | (l[7] << 0) | (get_bit_in_byte(msb_1, 4) << 16)) / 100.0  
        results['d'].append( byte_array)
        
        
        b1 = get_bit_in_byte(l[9], 7)
        b2 = get_bit_in_byte(l[9], 6)
        b3 = get_bit_in_byte(l[9], 5)
        b4 = get_bit_in_byte(l[9], 4)
        b5 = get_bit_in_byte(l[9], 3)
        b6 = get_bit_in_byte(l[9], 2)
        b7 = get_bit_in_byte(l[9], 1)
        b8 = get_bit_in_byte(l[9], 0)
        # byte_array = ((l[10] << 8) | (l[11] << 0) | (get_bit_in_byte(msb_1, 3) << 16)) / 1000.0 
        results['e1'].append(b7)
        results['e2'].append(b8)
        
        byte_array = ((l[10] << 8) | (l[11] << 0)) / 100.0 
        results['f'].append( byte_array)    
    
    
df = pd.DataFrame.from_dict(results)


for key in results.keys():
    plt.clf()
    plt.plot(results[key])
    plt.title(key)
    plt.show()
# res = ''.join(str(res))
# with open('./go/results.txt', 'w') as f:
#     res = str(res)
#     f.write(str(res))