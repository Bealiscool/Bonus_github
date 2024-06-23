#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:49:33 2023

@author: phyoung
"""
n = int(input("Enter the number of layers(2 to 5) = "))
s = int(input("Enter the side length of the top layer = "))
g = int(input("Enter the growth of each layer = "))
w = int(input("Enter the trunk width(odd number, 3 to 9) = "))
h = int(input("Enter the trunk height(4 to 10) = "))


for i in range(s):
    print(" "*((s+(n-1)*g-1)-i), "#"*(i*2+1))
for i in range(1, n):
    for j in range(1, s+g*i):
        print(" "*((s+(n-1)*g-1)-j), "#"*(j*2+1))
for i in range(h):
    print(" "*((s+(n-1)*g-1)-(w//2)), "|"*w)        


