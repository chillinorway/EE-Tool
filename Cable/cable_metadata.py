# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 07:20:30 2021

@author: aleksam
"""
""" 
    Radox:
    https://www.bartec.de/ProdCatalogue/Assets/Datasheets/lng_0/Radox125Wire_E.pdf
    Radox tåler høyere temperatur enn de som inneholder PVC som NEK400 omhandler
    Kan være at man kan gjøre vurderinger på om ikke man kan kjøre tynnere ledere enn hva en er vant til?
"""

wire_44A = {'AWG_26': 0.86,
            'AWG_24': 1.02,
            'AWG_22': 1.5,
            'AWG_20': 1.4,
            'AWG_16': 1.83,
            'AWG_14': 2.26,
            'AWG_12': 2.74}

wire_44A_tw = {'AWG_26': 1.73,
               'AWG_24': 2.03,
               'AWG_22': 2.38,
               'AWG_20': 2.79,
               'AWG_18': 3.3,
               'AWG_16': 3.65,
               'AWG_14': 4.52,
               'AWG_12': 5.48}

# Ikke oppdatert
wire_55A= {'AWG 24': 1.02,
            'AWG 22': 1.5,
            'AWG 20': 1.4,
            'AWG 16': 1.83,
            'AWG 14': 2.26,
            'AWG 12': 2.74}


wire_radox_125 = {'0.25 mm²':1.3,
                  '0.34 mm²':1.5,
                  '0.50 mm²':2.0,
                  '0.75 mm²':2.25,
                  '1.00 mm²':2.6,
                  '1.50 mm²':2.85,
                  '2.50 mm²':3.35,
                  '4.00 mm²':4.95,
                  '6.00 mm²': 4.65}

# Ikke oppdatert
wire_100G = {'0.25 mm²':1.08,
             '0.50 mm²':1.45,
             '0.75 mm²':1.65,
             '1.00 mm²':1.80,
             '1.50 mm²':2.13,
             '2.50 mm²':2.63,
             '4.00 mm²':3.17}

xffr = {'XFFR-03':4.8,
        'XFFR-04':7.15,
        'XFFR-07':9.55,
        'XFFR-11':14.25,
        'XFFR-15':4.8,
        'XFFR-20':7.15,
        'XFFR-30':9.55}


dr_25 = {'1/8':1.6, 
          '3/16':2.4, 
          '1/4':3.2, 
          '3/8':4.75, 
          '1/2':6.35, 
          '3/4':9.5, 
          '1':12.7, 
          '1 1/2':19.0, 
          '2':25.4}

# dr_25 = {'1/8':3.2, 
#          '3/16':4.8, 
#          '1/4':6.4, 
#          '3/8':9.5, 
#          '1/2':12.7, 
#          '3/4':19.0, 
#          '1':25.4, 
#          '1 1/2':38.0, 
#          '2':50.8}

ray_10x = {'5':3.0, '7.5':4.0, '9.5':6.0, '14.0':7.5, '22.0':10.0, '24.0':12.5, '38.0':20.0}

# dr_25 = {'DR-25 1/8':{'Max_recovered_after_heating': 2.4, 'Recovered_wall_thickness': 0.76}, 
#          'DR-25 3/16':{'Max_recovered_after_heating': 3.6, 'Recovered_wall_thickness': 0.84},
#          'DR-25 1/4':{'Max_recovered_after_heating': 4.8, 'Recovered_wall_thickness': 0.89},
#          'DR-25 3/8':{'Max_recovered_after_heating': 7.15, 'Recovered_wall_thickness': 1.02},
#          'DR-25 1/2':{'Max_recovered_after_heating': 9.55, 'Recovered_wall_thickness': 1.22},
#          'DR-25 3/4':{'Max_recovered_after_heating': 14.25, 'Recovered_wall_thickness': 1.45}}

boot = {}

