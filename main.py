# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 12:12:13 2021

@author: Renan
"""

import tkinter as tk


def calculate(*args):
    try:
        foot = float(feet.get())
        val = (0.3048 * foot * 10000 + 0.5)/10000
        meters.set(str(val))
    except:
        meters.set("Valor inválido")

class win:
    def __init__(self, master):
        global feet
        global meters

        feet = tk.StringVar()
        meters = tk.StringVar()
        
        mainframe = tk.LabelFrame(master, relief="ridge")
        feetlbl = tk.Label(mainframe, text="Pés")
        equilbl = tk.Label(mainframe, text="é equivalente a:")
        metlbl = tk.Label(mainframe, text="metros")
        entry = tk.Entry(mainframe, textvariable=feet, justify="center")
        button = tk.Button(mainframe, text="calcular", command=calculate)
        result = tk.Label(mainframe, textvariable=meters, relief="sunken")
        
        mainframe.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        feetlbl.grid(row=1, column=3)
        equilbl.grid(row=2, column=1)
        metlbl.grid(row=2, column=3)
        entry.grid(row=1, column=2)
        button.grid(row=3, column=2)
        result.grid(row=2, column=2, sticky="nsew")
        
        wids = [feetlbl, equilbl, metlbl, entry, button, result]
        
        for i in wids:
            i.grid_configure(padx=5, pady=5)
        
        entry.focus_force()
        button.bind("<Shift_L>", calculate)        

    
    
root = tk.Tk()
root.title("Conversor pés para metros")
root.resizable(False,False)
win(root)
root.mainloop()
