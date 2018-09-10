# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 19:06:36 2018

@author: FAMILIA
"""

from turtle import *
from math import sqrt
L=100
b=40
a=int(input("Dime cuantos lados en tu poligono chiquito "))
pisos=1+int(input("Dime cuantos pisos en tu pirámide "))
q= (180/a)-90
o=0
Lr=L*pisos*sqrt(3)/4
p=0,0
ladoiz=0
penup();
sety(Lr);
for i in range(pisos):
    ladoiz= xcor();
    for j in range(i):
        p=pos()
        o=heading()
        seth(q)
        fd(b);lt(90);pd();circle(b,360,a);pu()
        goto(p);seth(0);fd(L)
    setx(ladoiz);rt(120);fd(L)
ht()
done()