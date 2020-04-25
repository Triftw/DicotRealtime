# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:46:29 2020

@author: Trif
"""

import numpy as np
import threading as thr
import tkinter as tk
from tkinter import *
import glob
import os
from time import sleep as sp
from PIL import Image,ImageTk
import pandas as pd

Gathering = True
Delete_After_Read = True
state_file = 'C:\\Users\\Trif\\Documents\\GitHub\\DicotRealtime\\State.txt'
state = 'knotting'
def StopGathering(): #Get stop message from VBA
    Gathering = False
    with open (state_file,'w') as f:
        f.write('stop')

#Funcion for Recognize one file
def Recognize(fname):
    pd.readcsv(fname)
    # recognition


def doGathering():#Keep getting New File in folder
    list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    while Gathering:
        sp(1)
        list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
        if max(list_of_files, key=os.path.getctime) != latest_file:
            TBDeleted = latest_file
            print(max(list_of_files, key=os.path.getctime))
            latest_file = max(list_of_files, key=os.path.getctime)
            if Delete_After_Read :
                os.remove(TBDeleted)
            else:
                print('No new file')

def Keydown(e):
    global state
    global tex
    global tlabel
    buttonID = None
    if e.char == ' ':
        buttonID = 1
        print('GG')
        if state == 'knotting':
            tex.set('Please reset and then press space')
            state = 'reseting'
        elif state == 'reseting':
            tex.set('Please finish the knot and press space')
            state = 'knotting'
#Image
FigureEight = Image.open('Images//figureeight.jpg')
#Slip = Image.open('slip.jpg')
#Overhand = Image.open('overhand.jpg')
#Window
window = tk.Toplevel()
frm = Frame(window)
frm.pack(fill=BOTH, expand=1)
window.geometry("600x450+400+100")

FE = ImageTk.PhotoImage(FigureEight)
ImageLabel = Label(frm,image = FE)
#ImageLabel.image = FE
ImageLabel.place = (10,80)
ImageLabel.pack()

bottomframe = Frame(frm)
bottomframe.pack(side = tk.BOTTOM)

frm.bind("<KeyPress>", Keydown)
frm.focus_set()


tex = tk.StringVar()
s = "Please finish the knot and press space"
tex.set(s)
tlabel = Label(bottomframe,textvariable = tex,justify = tk.LEFT)
tlabel.pack(side = tk.LEFT)

'''
for i in range(4):
    btn = tk.Button(btn_frame, text=pos[i], fg=color[i], bg=looseColor, command=lambda m=pos[i], btn=i: getBtnInput(m, btn))
    btn.config(height=10, width=50)
    buttons.append(btn)

buttons[0].grid(row=1, column=1)
buttons[1].grid(row=1, column=2)
buttons[2].grid(row=2, column=1)
buttons[3].grid(row=2, column=2)
'''
#nexttrial_button = tk.Button(next_btn_frame, text='next trial', fg='black', command=nextTrialBtn)
#nexttrial_button.grid(row=4, column=1)


window.mainloop()