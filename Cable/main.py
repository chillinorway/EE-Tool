# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 07:06:18 2022

@author: aleksam
"""
import tkinter as tk
from tkinter.filedialog import Entry, StringVar, OptionMenu
import cable_tools as ct
import cable_metadata
import func_tools as ft






def dict_from_module(module):
    context = {}
    for setting in dir(module):
        # you can write your filter here
        # if setting.islower() and setting.isalpha():
        if not setting.startswith('_'):
            context[setting] = getattr(module, setting)
    return context

meta_data = dict_from_module(cable_metadata)




bundle_xy = {0:{'number_of_wires':2, 'cross_section':'AWG_24', 'wire_type':'wire_44A', 'tw':True},
             1:{'number_of_wires':4, 'cross_section':'AWG_22', 'wire_type':'wire_44A', 'tw':True},
             2:{'number_of_wires':6, 'cross_section':'AWG_26', 'wire_type':'wire_44A', 'tw':False}}



def define_bundle():
    '''
    Mulig å definere lengde på bundle og antall twist.
    
    '''


    pass


bundle_xy = {0:{'number_of_wires':4, 'cross_section':'AWG_24', 'wire_type':'wire_44A', 'tw':True},
             1:{'number_of_wires':1, 'cross_section':'AWG_16', 'wire_type':'wire_44A', 'tw':True}}

def bundle_processor(bundles = dict):
    translated_bundle = {}
    translated_bundles = {}
    for bundle in bundles:
        bundle_dict = bundles[bundle]
        if bundle_dict['tw'] == True:
            wire_type_key = bundle_dict['wire_type']+'_tw'
            cross_section = meta_data[wire_type_key][bundle_dict['cross_section']]
        else:
            cross_section = meta_data[wire_type_key][bundle_dict['cross_section']]
        translated_bundle['id'] = bundle
        translated_bundle['cross_section'] = cross_section
        translated_bundle['number_of_wires'] = bundle_dict['number_of_wires']
        translated_bundles[bundle] = translated_bundle
        translated_bundle = translated_bundle.fromkeys(translated_bundle, 0)
        
    only_wires_dia = ct.cable_dia_te_dev(translated_bundles)
    # Add cable length compensation... add x mm clearance pr meter of cable?
    cable_length = 3500
    clearance = 0.0001
    cable_length_compensation = cable_length * clearance 
    print(cable_length_compensation)
    
    wire_dia_w_compensation = cable_length_compensation + only_wires_dia
    print(wire_dia_w_compensation)
    # Find reccomended screen
    screen_data = meta_data['ray_10x']
    print(wire_dia_w_compensation)
    closest_screen = ft.closest_in_dict(dict_in=screen_data,value_in=wire_dia_w_compensation)
    print(closest_screen)
    wires_and_screen = wire_dia_w_compensation + 2
    print(wires_and_screen)
    # Find reccomended shrink...
    shrink_data = meta_data['dr_25']
    closest_shrink = ft.closest_in_dict(dict_in=shrink_data,value_in=wires_and_screen)
    print(closest_shrink)

    
    # res = find_heatshrink_thickness(only_wires_dia+2, 9.55, 1.22)
    # print(res+only_wires_dia)



bundle_dia = bundle_processor(bundles=bundle_xy)


def build_bundle(defined_bundle, number_of_screens=None, cable_length=None, heatshrink_type=None):
    dia = ct.cable_dia_te(defined_bundle)
    return dia

def select_wire_type(w_type):
    print(var_selected_wiretype.get())
    pass

def test():
    print("Test")

# print(build_bundle(defined_bundle=bundle_p1))

wire_types = [
"44A",
"55A",
"Radox 125"
] #etc




window = tk.Tk()
window.title("Sizing tool")
window.rowconfigure(0, minsize=200, weight=1)
frame_1 = tk.Frame(window, bd=2)
frame_2 = tk.Frame(window, bd=2)

frame_1.grid(row=0, column=0, sticky='nsew')
frame_2.grid(row=0, column=1, sticky='nsew')

var_selected_wiretype = StringVar(window)
var_selected_wiretype.set(wire_types[0]) # default value

var = StringVar(window)
var.set(wire_types[0]) # default value



wire_type_dropdown = OptionMenu(frame_2, var_selected_wiretype, *wire_types, command=select_wire_type)
wire_type_dropdown.grid(row=1, column=1, sticky='nsew')

dropdown = OptionMenu(frame_2, var, *wire_types, command=select_wire_type)
dropdown.grid(row=2, column=1, sticky='nsew')

save_button = tk.Button(frame_1, text='Save bundle', command=lambda: test())
save_button.grid(row=1, column=1, sticky='nsew')




def main():
    window.mainloop()

    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    