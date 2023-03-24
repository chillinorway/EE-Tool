# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 16:51:12 2022

@author: Aleksander
"""

import tkinter as tk    
from tkinter.filedialog import askopenfilename, askdirectory, asksaveasfilename, Entry                
from tkinter import ttk
from PIL import ImageTk, Image 
import cv2
import numpy as np
import glob
import os


def pick_file():
    _logopath = askopenfilename()
    logopath.set(_logopath)
    # forhåndsvis logofunksjon()
    print(logopath.get())

def input_directory():
    dir = askdirectory()
    input_dir.set(dir)
    
def output_directory():
    dir = askdirectory()
    output_dir.set(dir)
    
def process():
    _logopath = logopath.get()
    _output_dir = output_dir.get()
    for image in glob.glob(f'{input_dir.get()}/*.*'):
        print(image)
        # img = cv2.imread(image)
        # h_img, w_img = img.shape

        
        

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Vannmerkeverktøy")
        self.parent.minsize(800, 400)
        tabControl = ttk.Notebook(self.parent)
        self.parent.geometry()
        c1 = tk.Canvas(self.parent, width=100-10, height=100-10)
        c1.create_oval(5,5,10-5,10-5, fill='black')
        tab0 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)

        tabControl.add(tab0, text ='Intro')
        tabControl.pack(expand = 1, fill ="both")

        ferrule_txt = tk.Text(tab3, wrap=tk.WORD)
        ferrule_txt.pack(fill="both", expand=True)


        btn_open = tk.Button(tab0, text='Velg vannmerkefil', command=lambda: pick_file())
        btn_open.pack()
        btn_open = tk.Button(tab0, text='Input bildemappe', command=lambda: input_directory())
        btn_open.pack()
        btn_open = tk.Button(tab0, text='Output bildemappe', command=lambda: output_directory())
        btn_open.pack()
        btn_run = tk.Button(tab0, text='Kjør Vannmerke for faen', command=lambda: process())
        btn_run.pack()


def run_gui():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    
if __name__ == "__main__": 
    root = tk.Tk()
    clicked = tk.StringVar()
    bundle_var = tk.StringVar()
    
    input_dir = tk.StringVar()
    output_dir = tk.StringVar()
    logopath = tk.StringVar()
    
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
    
