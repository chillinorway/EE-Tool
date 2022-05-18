# -*- coding: utf-8 -*-
"""
Created on Mon May 16 21:43:46 2022

Samling av verktøy for elmek

@author: Aleksander
"""



def nr_build_ups(bundle_dia:float, target_dia:float, heat_shrink_thickness:float):
    """
    Kalkulere antall krympestrømper som skal til for å
    bygge opp fra buntdiameter til bakende på konnektor
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
    return int((target_dia - bundle_dia) / (heat_shrink_thickness * 2)  - 1) # -1 for å trekke fra strømpa som skal gå over hele kabelen

print(nr_build_ups(bundle_dia=10.5, target_dia=30.6, heat_shrink_thickness=2.2))


start_t = 1
stop_t = 2.2

bundle_dia = 10.5
target_dia = 30.6

i = 0
build_dia = bundle_dia

while build_dia <= target_dia:
    i+=1
    fac = target_dia / build_dia
    thickness = fac * stop_t
    build_dia = build_dia + (thickness*2)
    print(build_dia)

print(i)

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


xy = voltage_drop(input_voltage=6, current=2, wire_material='cu', wire_length=10, cross_section=2.5, cos_phi=1, phases=3)

print(xy)




