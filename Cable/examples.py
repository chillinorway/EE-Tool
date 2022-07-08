# -*- coding: utf-8 -*-
"""
Created on Thu May 19 07:02:48 2022

@author: aleksam
"""

import cable_tools as ct
import numpy as np

# bundle_p1 = {5: 1.83, 2: 2.26} 
# print(ct.cable_dia_te(bundle_p1))
# print(ct.find_heatshrink_thickness(7.19, 4.8, 1.02) + ct.cable_dia_te(bundle_p1))

# # Example
# print(ct.cable_dia_cc([1.83]*5+[2.26]*2))
# print(ct.find_heatshrink_thickness(6.11, 4.8, 1.02) + ct.cable_dia_cc([1.83]*5+[2.26]*2))
# print()

bundle_p1 = {5: 1.83, 2: 2.26, 38:1.02} 
print(ct.cable_dia_te(bundle_p1))
# print(ct.find_heatshrink_thickness(ct.cable_dia_te(bundle_p1), 6.4, 1.22) + ct.cable_dia_te(bundle_p1))

# print()


'''
Definere antall ledere, tverrsnitt, antall skjermer og lengde, samt krympestrømpetype.



'''




# bundle_p2 = {8: 2.2, 2: 1.27} 
# print(ct.cable_dia_te(bundle_p2))
# print(ct.nr_build_ups(bundle_dia=10.5, target_dia=30.6, heat_shrink_thickness=2.2))


# Anita
# bundle_p1 = {16: 1.02, 2: 1.83} 
# print(ct.cable_dia_te(bundle_p1))
# print(ct.find_heatshrink_thickness(ct.cable_dia_te(bundle_p1), 6.4, 1.22) + ct.cable_dia_te(bundle_p1))




# print(ct.cable_dia_cc([2.85]*4))

# bundle_p2 = {4: 2.85}
# print(ct.cable_dia_te(bundle_p2))


# print(f'{ct.find_heatshrink_thickness(12.7, 6.4, 1.22):.2f}')

# print(f'{ct.find_heatshrink_thickness(9.5, 9.5, 1.45):.2f}')

# print(f'{ct.find_heatshrink_thickness(10.5, 6.4, 1.22):.2f}')
# print(f'{ct.find_heatshrink_thickness(11.98, 6.4, 1.22):.2f}')
# print(f'{ct.find_heatshrink_thickness(13.28, 9.5, 1.45):.2f}')
# print()
# print(f'{ct.find_heatshrink_thickness(10.5, 9.5, 1.45):.2f}')
# print(f'{ct.find_heatshrink_thickness(11.98, 9.5, 1.45):.2f}')
# print(f'{ct.find_heatshrink_thickness(13.28, 9.5, 1.45):.2f}')



ct.define_bundle()