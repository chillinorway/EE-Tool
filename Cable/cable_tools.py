# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:43:46 2022
Samling av verktøy for elmek
@author: Aleksander
"""

import math
import circlify as cc
import calc_dia





"""
Cable diameter tools
Kompensering for twist? Eller hente ut verdier for twist i datablad. Finnes for 44 og 55. Veit ikke med radox.
"""


def _metadata_lookup():
    pass

def _length_compensation():
    pass

def nr_build_ups(bundle_dia:float, target_dia:float, heat_shrink_thickness:float):
    """
    Kalkulere antall krympestrømper som skal til for å
    bygge opp fra bunt diameter til bakende på konnektor
                                            *********
                                            *       *
            --------------------------------        *
                                                    *
            --------------------------------        *
                                            *       *
                                            *********
    Tjukkelsen på strømpe endres avhengig av hvor mye den krympes inn,
    dette blir ikke tatt hensyn til her pr nå.
    """
    return f'{int((target_dia - bundle_dia) / (heat_shrink_thickness * 2)  - 1):.2f}' # -1 for å trekke fra strømpa som skal gå over hele kabelen


# =============================================================================
# 
# =============================================================================


def find_heatshrink_thickness(bundle_dia, lowest_shrink_dia, shrink_thickness):
    # Thickness of cable w/shrink: ((lowest_shrink_dia / bundle_dia) * (shrink_thickness*2)) + bundle_dia
    return ((lowest_shrink_dia / bundle_dia) * (shrink_thickness)) * 2

def add_screen():
    
    pass


def nr_build_ups_2(bundle_dia, target_dia):
    """ Legge inn target og bundle dia.  
        Automatisk finne frem til hvilken strømpe som passer og hvilke
        karakteristikker den har mtp tjukkelse.
        
        Om avviket mellom bundle_dia og target_dia er for stort må man kanskje gå bort fra build up!?
        Burde gå for den største mulige strømpa antakelig.
        
        Fikse formelen under.. den stemmer ikke.
    """

    stop_t = 2.2

    i = 0
    build_dia = bundle_dia
    number_of_ais = []
    while build_dia <= target_dia:
        i+=1
        fac = target_dia / build_dia
        thickness = fac * stop_t
        build_dia = build_dia + (thickness*2)
        # print(build_dia)
        number_of_ais.append(i)
    return number_of_ais   

nr_build_ups_2(bundle_dia=10.5, target_dia=30.6)    

# =============================================================================
# 
# =============================================================================
factor = {1: 1, 2: 1.415, 3: 1.242, 4: 1.205, 5: 1.208, 6: 1.225, 7: 1.15}

# annenhver n skal være opphøyd i 2? Den n som ikke er opphøyd skal multipliseres med sin dia.
def cable_dia_te(bundle:dict):
    """
    Formula from TE Connectivity:
    Bundle diameter = Factor x √n * d² + n₂² + d₂² )
    """
    l = []
    exponent = 1
    for i, number_of_wires in enumerate(bundle):
        number_of_wires_key = number_of_wires
        if i % 2 == 1:
            exponent = 2
            res = (number_of_wires**exponent) + (bundle[number_of_wires_key]**2)
        else:
            exponent = 1
            res = (number_of_wires**exponent) * (bundle[number_of_wires_key]**2)
        l.append(res)
    if number_of_wires > 7:
        number_of_wires_key = 7
        
    bundle_diameter = factor[number_of_wires_key] * math.sqrt((sum(l)))
    return bundle_diameter

def cable_dia_te_dev(bundles:dict):
    """
    Formula from TE Connectivity:
    Bundle diameter = Factor x √n * d² + n₂² + d₂² )
    """
    l = []
    exponent = 1
    # print(bundles)
    for i, bundle in enumerate(bundles):
        bundle = bundles[bundle]
        # print(bundle)
        number_of_wires = bundle['number_of_wires']
        if i % 2 == 1:
            exponent = 2
            res = (number_of_wires**exponent) + (bundle['cross_section']**2)
        else:
            exponent = 1
            res = (number_of_wires**exponent) * (bundle['cross_section']**2)
        l.append(res)
    if number_of_wires > 7:
        number_of_wires = 7
        
    bundle_diameter = factor[number_of_wires] * math.sqrt((sum(l)))
    return bundle_diameter


# =============================================================================
# 
# =============================================================================

def cable_dia_cc(bundle:list):
    bundley = cc.circlify(bundle, show_enclosure=True)
    density = cc.density(bundley)
    cc.bubbles(bundley)
    diameter = calc_dia.EnvelopeDiameter(bundle, density*100) # Calculate total diameter
    return diameter


bundle_p1 = {5: 1.83, 2: 2.26, 38:1.02} 













# =============================================================================
# 
# =============================================================================

"""
Wire magnetism 

F/dL = mu*I1*I2 / 2 * pi * r

F/dL [N/m]
mu = 4*pi*10^-7 T*m/A

r = distanse mellom ledere [m]
"""

"""
r= μ I1 I2 /(2 π (F/ΔL)) = 4π *10(-7) T*m/A * 2 A * 1 A / (2 π * 20*10(-6)N/m)
"""

"""
Eksempel 1:
I1 = U1 / R1
U1 = 230VAC
R1 = 10 ohm

I2 = U2 / R2
U2 = 24VDC
R2 = 5 ohm
"""

mu = 4 * math.pi * 10e-7

r = 1
I1 = 230 / 10
I2 = 24 / 2

# I1 = 2
# I2 = 1
# r=0.1

F_dL = (mu * I1 * I2) / (2 * math.pi * r)
# print(F_dL)
# print(4 * 10e-6)

# =============================================================================
# 
# =============================================================================


# Spenningsfall

def voltage_drop(input_voltage, current, wire_material, wire_length, cross_section, cos_phi, phases):
    """
    Parameters
    ----------
    current : float. Amount of current flowing in the circuit
    wire_material : str. cu for copper, au for aluminium
    wire_length : int. total amount of wire used. L+L-, L1/L2/L3
    cross_section : float. Area of metal wire in mm²
    phases : number of phases used. 1 for one phase. 3 for 3 phase.
    ----------
    Returns:
    v_drop in percentage
    """
    if wire_material == "al":
        rho = 0.028
    else:
        rho = 0.0175
    if phases == 3:
        sqrt_value = 1.73
    else:
        sqrt_value = 1
    
    v_drop = (current * cross_section * wire_length * cos_phi * sqrt_value * rho) / cross_section
    v_drop_percent = v_drop / input_voltage * 100
    return v_drop, v_drop_percent


dropV_dropPerCent = voltage_drop(input_voltage=6, current=2, wire_material='cu', wire_length=10, cross_section=2.5, cos_phi=1, phases=3)

# print(dropV_dropPerCent)

# =============================================================================
# 
# =============================================================================


