# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:09:31 2022

@author: Aleksander
"""

import datetime
import serial
import keyboard
import csv

time_now = datetime.datetime.now().strftime("%y%m%dT%H%M%S")

with serial.Serial('COM4', 115200) as ser:
    ser.flushInput()
    while True:
        if keyboard.is_pressed('s'):
            break

        line = ser.read_until(b'\xbb')
        # print(line)
        with open(f"{time_now}.csv", "a", newline="") as f:
            writer = csv.writer(f, delimiter=" ")
            writer.writerow(line)
            
            
            