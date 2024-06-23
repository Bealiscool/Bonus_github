#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 07:14:37 2023

@author: phyoung
"""
#基本設定
h = float(input("Input the height of the 1st ball: "))
m1 = float(input("Input the mass of the 1st ball: "))
m2 = float(input("Input the mass of the 2nd ball: "))

#數值
g = 9.8
u = m1 * g * h
v1 = (2 * g * h) ** (1 / 2)

v2 = (2 * m1 * v1) / (m1 + m2) 

#結果
print("The velocity of the 1st ball after slide: ", v1)
print("The velocity of the 2nd ball after collision: ", v2)