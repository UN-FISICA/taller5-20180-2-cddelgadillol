#!/usr/bin/python
# -*- coding: UTF-8-*-
from  calc_mod import *

 
def  calc_ace(image,hz,dx):
	a=array(imread(image))
	scel=calc(a,hz,dx)
	print(scel)
calc_ace("b2.jpeg",1/0.5,0.5)

#bfiltrada=nd.median_filter(a,size=1)          b=bfiltrada
