# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:04:26 2018

@author: FAMILIA
"""

from turtle import *
from math import sqrt
from math import sin 
from math import radians
L=100
b=30
pisos=1+int(input("Dime cuantos pisos en tu pirámide "))
o=0
Lr=L*pisos*sqrt(3)/4
p=0,0
ladoiz=0;
up();
sety(Lr);
for i in range(pisos):
    ladoiz= xcor();
    k=i+3
    q= (180/k) -90
    ain=radians(360/k)
    aop=radians(90-(360/(2*k)))
    r=b*sin(aop)/sin(ain)
    for j in range(i+1):
        p=pos()
        o=heading()
        seth(q)
        fd(r);lt(90);pd();circle(r,360,k);pu()
        goto(p);seth(0);fd(L)
    setx(ladoiz);rt(120);fd(L)
ht()
done()