# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:38:46 2020

@author: Trif
"""

import glob
import os
from time import sleep as sp

list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
while True:
    sp(1)
    list_of_files = glob.glob('C:\\Users\\Trif\\Desktop\\NewFile\*') # * means all if need specific format then *.csv
    if max(list_of_files, key=os.path.getctime) != latest_file:
        print(max(list_of_files, key=os.path.getctime))
        latest_file = max(list_of_files, key=os.path.getctime)
    