# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:47:07 2018

@author: FAMILIA
"""

from turtle import *
from math import sqrt
L=90
b=40
pisos=1+int(input("Dime cuantos pisos en tu pirámide "))
o=0
Lr=L*pisos*sqrt(3)/4
p=0,0
ladoiz=0;
penup();
sety(Lr);
for i in range(pisos):
    ladoiz= xcor();
    k=i+3
    q= (180/k) -90
    for j in range(i+1):
        p=pos()
        o=heading()
        seth(q)
        fd(b);lt(90);pd();circle(b,360,k);pu()
        goto(p);seth(0);fd(L)
    setx(ladoiz);rt(120);fd(L)
ht()
done()