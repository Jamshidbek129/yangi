# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 23:57:23 2023

@author: shoki
"""
import turtle as t
import colorsys
t.bgcolor('black')
h=1
t.tracer(200)
t.pensize(1)
def drawing(a,n):
    t.circle(5+n,60)
    t.right(a)
    t.circle(5+n,60)
t.goto(0,0)
for i in range(600):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=0.005
    t.pencolor(c)
    drawing(180,i)

    drawing(1/2, 0)

t.done()
    
        