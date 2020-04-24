# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:46:29 2020

@author: Trif
"""

import numpy as np
import threading as thr
import tkinter as tk
import glob
import os
from time import sleep as sp
import pandas as pd

Gathering = True
Delete_After_Read = True
state_file = 'C:\\Users\\Trif\\Documents\\GitHub\\DicotRealtime\\State.txt'

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
