# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:38:46 2020

@author: Trif
"""

import glob
import os
import pandas as pd
from time import sleep as sp


    
Delete_After_Read = True
state_file = 'C:\\Users\\Trif\\Documents\\GitHub\\DicotRealtime\\State.txt'

def StopGathering():
    with open (state_file,'w') as f:
        f.write('stop')

# Read Model

#Funcion for Recognize one file
def Recognize(fname):
    pd.readcsv(fname)

list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
while True:
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
    