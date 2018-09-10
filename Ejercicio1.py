# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 16:38:09 2018

@author: FAMILIA
"""
from turtle import *
from math import sqrt
c=40
d=c/2
C=100
D=C+d
a=c/2 * sqrt(2)
pu();
for i in range(4):
    fd(D);lt(90);fd(d);lt(45);pd();circle(a,360,4);pu()
    rt(45);bk(d);rt(90);bk(d);lt(90)
ht()
done()