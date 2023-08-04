#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:13:31 2023

@author: nebiyousamuel
"""

# mc_integration.py

import numpy as np
from random import random

def MCintegrate(f, a, b, n):
    x = np.linspace(a, b, num=n, endpoint=True)
    maxF = max(f(x))
    
    area = 0
    for i in range(n):
        randNoX = random()*(b-a)+(b-a)/2
        randNoY = random()*maxF
        if randNoY <= f(randNoX):
            area += 1
    
    boxArea = (b-a)*maxF
    integral = area/n * boxArea
    return integral