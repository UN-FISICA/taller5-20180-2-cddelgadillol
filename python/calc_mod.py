#!/usr/bin/env python
# -*- coding: UTF-8-*-
import math
import numpy as np
from numpy.linalg import inv,lstsq
from pylab import *
from scipy import  misc as  mi
from scipy.ndimage import label
import scipy.ndimage as  nd




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
	
def marca(b,numf,lalala):
		
	sizes = nd.sum(b, lalala, range(numf + 1))
	suma=np.sum(sizes)
	suma=suma/(numf)
	remtamaño=sizes>suma*1.5
	remtamaño2=sizes<(suma/5)
	remover=remtamaño[lalala]
	b[remover]=0
	remover=remtamaño2[lalala]
	b[remover]=0
	return b
	
def centro(b,numf,lalala,dx):
	datos=np.zeros(numf)
	cen=nd.measurements.center_of_mass(b,lalala, range(numf + 2))
	cpt=1
	while cpt<numf+1:
		datos[cpt-1]=cen[cpt][0]
		cpt=cpt+1
	inicial=datos[0]
	cpt=1
	while cpt<numf+1:
		datos[cpt-1]=(datos[cpt-1]-inicial)*dx
		cpt=cpt+1
	return datos
	
def curva(tiempo,datos):
	x=tiempo
	y=datos
	f=[]
	f.append(lambda x:np.ones_like(x))
	f.append(lambda x:x)
	f.append(lambda x:x**2)
	

	Xt=[]
	for fu in f:
		Xt.append(fu(x))
	Xt= np.array(Xt)
	X=Xt.transpose()
	
	a = np.dot(np.dot(inv(np.dot(Xt,X)),Xt),y)
	return a





def calc(image,hz,dx):
	
	temp=1/hz	
	b=image
	b=filtrado(b)
	lalala, numf = label(b)
	b=marca(b,numf,lalala)
	lalala, numf = label(b)
	
	datos=centro(b,numf,lalala,dx)
	
	
	tiempo=np.zeros(numf)
	cpt=0
	while cpt<numf:
		tiempo[cpt]=tiempo[cpt]+temp*cpt
		cpt=cpt+1
	inicial=datos[0]
	a=curva(tiempo,datos)
	acel=a[2]*2
	return (acel)   
