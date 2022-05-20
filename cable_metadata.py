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

wire_44A = {'AWG 24': 1.02,
            'AWG 22': 1.5,
            'AWG 20': 1.4,
            'AWG 16': 1.83,
            'AWG 14': 2.26,
            'AWG 12': 2.74,
            '0.25 mm²': 1.2}

# Ikke oppdatert
wire_55A= {'AWG 24': 1.02,
            'AWG 22': 1.5,
            'AWG 20': 1.4,
            'AWG 16': 1.83,
            'AWG 14': 2.26,
            'AWG 12': 2.74,
            '0.25 mm²': 1.2}


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

dr_25 = {'DR-25 1/8':2.4, 
         'DR-25 3/16':3.6,
         'DR-25 1/4':4.8,
         'DR-25 3/8':7.15,
         'DR-25 1/2':9.55,
         'DR-25 3/4':14.25}

