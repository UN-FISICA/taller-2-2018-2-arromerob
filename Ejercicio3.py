# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:04:04 2018

@author: FAMILIA
"""

from turtle import *
L=120
b=40
a=int(input("Dime cuantos lados en tu poligono chiquito "))
m=int(input("Dime cuantos lados en tu poligono grande "))
q= (180/a)-90
o=0
p=0,0
n=360/m
for i in range(m):
    up()
    fd(L);lt(n);
    o=heading()
    p=pos()
    seth(q)
    fd(b);lt(90);pd();circle(b,360,a);pu()
    goto(p);seth(o)
ht()
done()