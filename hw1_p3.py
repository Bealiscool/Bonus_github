#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 06:46:02 2023

@author: phyoung
"""
#輸入
v = float(input("Input velocity: "))
c = 299792458

#公式
p = v / c
r = 1 / (1 - v**2/c**2)**(1/2)

tp1 = 4.3 / r
tp2 = 6.0 / r
tp3 = 309 / r
tp4 = 2000000 / r

#輸出
print("Percentage of light speed = ", p)
print("Travel time to Alpha Centauri = ", tp1)
print("Travel time to Barnard's Star = ", tp2)
print("Travel time to Betelgeuse (in the Milky Way) = ", tp3)
print("Travel time to Andromeda Galaxy (closest galaxy) = ", tp4) 