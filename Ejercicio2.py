# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:59:29 2018

@author: FAMILIA
"""

from turtle import *
from math import sqrt
L=120
b=40
a=int(input("Dime cuantos lados en tu poligono chiquito "))
q= (180/a)-90
o=0
p=0,0
for i in range(4):
    pu()
    fd(L);lt(90);
    o=heading()
    p=pos()
    seth(q)
    fd(b);lt(90);pd();circle(b,360,a);pu()
    goto(p);seth(o)
ht()
done()