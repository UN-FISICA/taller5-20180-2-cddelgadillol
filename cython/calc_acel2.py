#!/usr/bin/python
# -*- coding: UTF-8-*-
from  calc_mod2 import *
import math
import numpy as np
from numpy.linalg import inv,lstsq
from pylab import *
from scipy import  misc as  mi
from scipy.ndimage import label
import scipy.ndimage as  nd


def crearf(x):
	f=[]
	f.append(lambda x:np.ones_like(x))
	f.append(lambda x:x)
	f.append(lambda x:x*x)
	return f
	
	
	

def filtrado(b):
	porsi=b
	b=nd.maximum_filter(b, size=3)
	b=where(b>190,0,255)
	b=nd.maximum_filter(b, size=2)
	cpw=0
	cpw2=0
	
	while cpw<b.shape[0]:
		while cpw2<b.shape[1]:
			sema=b[cpw][cpw2][0]+b[cpw][cpw2][1]+b[cpw][cpw2][2]
			if sema>0:
				b[cpw][cpw2][0]=255
				b[cpw][cpw2][1]=255
				b[cpw][cpw2][2]=255
				
			cpw2=cpw2+1
		cpw2=0
		cpw=cpw+1
	if b[0][0][0]==0:
		b=b	
	else:
		b=porsi
		b[:,:,2]=0
		b=where(b<35,0,255)
		b=nd.maximum_filter(b, size=2)
		
	return b
 

 
def  calc_ace(image,hz,dx):
	a=array(imread(image))
	a=filtrado(a)
	scel=calc(a,hz,dx)
	print(scel)
calc_ace("b2.jpeg",1/0.5,0.5)

#bfiltrada=nd.median_filter(a,size=1)          b=bfiltrada
