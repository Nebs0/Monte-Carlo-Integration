#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:14:42 2023

@author: nebiyousamuel
"""

# main.py

from mc_integration import MCintegrate

def f(x):
    return x

# Calculate the area of f(x) = x from 0 to 1
area = MCintegrate(f, 0., 1., 50)
print(area)