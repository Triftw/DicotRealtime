# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:46:29 2020

@author: Trif
"""

import numpy as np
import threading as thr
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import glob
import os
import csv
import random
from time import sleep as sp
from PIL import Image,ImageTk
import pandas as pd
Usernum = 6
datapath = 'C:\\Users\\Trif\\Documents\\GitHub\\DicotRealtime'
if not os.path.exists(datapath+'\\U'+str(Usernum)):
    os.mkdir(datapath+'\\U'+str(Usernum))
else:
    print("CHECK USERNUM")
datapath=datapath+'\\U'+str(Usernum)+'\\'
kcnt = [0,0,0,0]
list_cnt = 0
#klist = [0,1,2,3]
#klist = [0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,0,0,1,1,1,2,2,2,3,3,3]
klist = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,0,0,0,1,1,1,2,2,2,3,3,3]
rename = []
random.shuffle(klist)
Gathering = True
Delete_After_Read = False
state_file = 'C:\\Users\\Trif\\Documents\\GitHub\\DicotRealtime\\State.txt'
state = 'knotting'
with open (state_file,'w') as f:
        f.write('start')
def StopGathering(): #Send stop message to VBA
    print('STOPPED!')
#    Gathering = False
    with open (state_file,'w') as f:
        f.write('stop')
def MoveData():
    global rename
    with open('important.txt','w') as imp:
        for s in rename:
            imp.write(s[0]+','+s[1]+'\n')
    mcnt = 0
    for s in rename:
        os.rename(s[0],s[1])
        mcnt +=1
    rename = []
    print(str(mcnt)+' files moved!')
#Funcion for Recognize one file
def Recognize(fname):
    pd.read_csv(fname)
    # recognition
def SaveData(fn,kt):
    global Usernum
    global datapath
    global kcnt
    kcnt[kt] = kcnt[kt]+1
    if kt == 0:
        nfn = 'o'+str(kcnt[kt])+'u'+str(Usernum)+'.csv'
    elif kt == 1:
        nfn = 'e'+str(kcnt[kt])+'u'+str(Usernum)+'.csv'
    elif kt == 2:
        nfn = 's'+str(kcnt[kt])+'u'+str(Usernum)+'.csv'
    elif kt == 3:
        nfn = 'c'+str(kcnt[kt])+'u'+str(Usernum)+'.csv'
    else:
        print('ERROR')
    rename.append([fn,(datapath+nfn)])
    #os.rename(fn,datapath+nfn)
def doGathering():#Keep getting New File in folder
    global state
    global glob
    global os
    global tex
    global list_cnt
    global klist
    global Gathering
    global sp
    print('Start doGathering')
    list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)
    while Gathering:
        sp(1)
        list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
        if max(list_of_files, key=os.path.getctime) != latest_file:
            TBDeleted = latest_file
            #print(max(list_of_files, key=os.path.getctime))
            latest_file = max(list_of_files, key=os.path.getctime)
            if state == 'saving':
                SaveData(latest_file, klist[list_cnt])
                list_cnt +=1
                if list_cnt== len(klist):
                    tex.set('Do Not Move! Thanks.')
                    state = 'END'
                    StopGathering()
                    sp(10)
                    MoveData()
                    print('DONE!!!')
                    tex.set('Move Data Done. Thanks Again!')
                else:
                    tex.set('Please reset and then press NEXT')
                    state = 'reseting'
            elif Delete_After_Read :
                if os.path.exists(TBDeleted):
                    os.remove(TBDeleted) 
            #else:
                #print('No new file')

def Keydown(e):
    global state
    global tex
    global tlabel
    global ImageLabel
    global list_cnt
    global rename
    buttonID = None
    if e.char == '.':
        buttonID = 1
        if state == 'knotting':
            tex.set('Please Wait!')
            state = 'saving'
    if e.char == '0':
        if state == 'reseting':
            tex.set('Please finish the knot and press DONE')
            state = 'knotting'
            ImageLabel.configure(image = Imgs[klist[list_cnt]])
    if e.char == 's':
        StopGathering()
    if e.char == 'm':
        mcnt = 0
        with open('important.txt','w') as imp:
            for s in rename:
                imp.write(s[0]+','+s[1]+'\n')
        for s in rename:
            os.rename(s[0],s[1])
            mcnt +=1
        rename = []
        print(str(mcnt)+'files moved!')
#Image
Eight = Image.open('Images//i2.png')
Slip = Image.open('Images//i3.png')
Overhand = Image.open('Images//i1.png')
Clove = Image.open('Images//i4.png')
#Window
window = tk.Toplevel()
frm = Frame(window)
frm.pack(fill=BOTH, expand=1)
window.geometry("600x450+100+100")


E = ImageTk.PhotoImage(Eight)
S = ImageTk.PhotoImage(Slip)
O = ImageTk.PhotoImage(Overhand)
C = ImageTk.PhotoImage(Clove)
Imgs = [O,E,S,C]
ImageLabel = Label(frm,image = Imgs[klist[0]])
#ImageLabel.image = FE
ImageLabel.place = (10,80)
ImageLabel.pack()

bottomframe = Frame(frm)
bottomframe.pack(side = tk.BOTTOM)

frm.bind("<KeyPress>", Keydown)
frm.focus_set()

fontStyle = tkFont.Font(family="Arial", size=24)
tex = tk.StringVar()
s = "Please finish the knot and press DONE"
tex.set(s)
tlabel = Label(bottomframe,textvariable = tex,justify = tk.LEFT,font=fontStyle)
tlabel.pack(side = tk.LEFT)

#w = thr.Thread(target = window.mainloop)
#w.start()
#doGathering()
Tgather = thr.Thread(target = doGathering)
Tgather.start()
window.mainloop()
#Tgather.join()