#!/usr/bin/python
# -*- coding: UTF-8-*-
import math
from numpy  import array

def labels(b):
	cpw=0
	cpw2=0
	sema=0;
	numf=-1
	traba=0
	while cpw<len(b[:,1]):
		while cpw2<len(b[1,:]):
			sema=b[cpw][cpw2][0]+sema
			if b[cpw][cpw2][0]>0:
				if traba==0:
					numf=numf+1
					traba=12
				b[cpw][cpw2][0]=numf
				b[cpw][cpw2][1]=numf
				b[cpw][cpw2][2]=numf
			cpw2=cpw2+1
		if sema==0:
			traba=0
		sema=0
		cpw2=0
		cpw=cpw+1
	der = (b,numf)
	return der

def Areaz(lalala, numf):
	cpw=0
	cpw2=0
	sema=0;
	hnumf=1
	traba=0
	b=lalala
	lista=[]
	while hnumf<numf+1:
		while cpw<len(b[:,1]):
			while cpw2<len(b[1,:]):
				if b[cpw][cpw2][0]==hnumf:
					sema=sema+1
				cpw2=cpw2+1
			cpw2=0
			cpw=cpw+1
		hnumf=hnumf+1
		lista.append(sema)
		sema=0
		cpw=0
	der = lista
	return der

def sume(matr):
	tama=len(matr)
	hnumf=0
	sema=0
	while hnumf<tama:
		sema=sema+matr[hnumf]
		hnumf=hnumf+1
	der = sema
	return der
	
def centroll(lalala,dx):
	cpw=0
	cpw2=0
	sema=0;
	anterior=0;
	traba=0
	b=lalala
	
	respuesta=0
	while cpw2<len(b[1,:]):
		while cpw<len(b[:,1]):
			if b[cpw,cpw2][0]>0:
				sema=sema+1
			cpw=cpw+1
		if sema>anterior:
			respuesta=cpw2
		anterior=sema
		sema=0
		cpw=0
		cpw2=cpw2+1
		
	der = respuesta
	return der
def centrol(lalala,dx):
	b=lalala
	ae=dx
	rop=centroll(b,ae)
	cpw=0
	cpw2=0
	sema=0;
	numf=-1
	traba=0
	lista=[]
	while cpw<len(b[:,1]):
		if b[cpw,rop][0]>0:
			sema=sema+1
			traba=8
		if b[cpw,rop][0]==0:
			if traba==8:
				traba=4
				envio=cpw-(sema/2)
				lista.append(envio)
			sema=0
		cpw=cpw+1
	cp=0
	inicial=lista[0]
	while cp<len(lista):
		lista[cp]=(lista[cp]-inicial)*dx
		cp=cp+1
	der = lista
	return der

def transp(Xtt):
	tal=len(Xtt[1]);
	conteo=0
	conteo2=0
	cosa=[None]*tal
	for i in range(tal):
		cosa[i]=[None]*3
	while conteo<3:
		while conteo2< tal:
			cosa[conteo2][conteo]=Xtt[conteo][conteo2]
			conteo2=conteo2+1
		conteo=conteo+1
		conteo2=0
	sol=array(cosa)
	return(sol)
def transp2(Xtt):
	tal=len(Xtt);
	Xtt=array(Xtt)
	conteo=0
	conteo2=0
	cosa=[None]*tal
	for i in range(tal):
		cosa[i]=[None]*1
	cosa=array(cosa)
	while conteo<tal:

		cosa[conteo,0]=Xtt[conteo]

		conteo=conteo+1
	sol=array(cosa)
	return(sol)
def transp3(Xtt):
	tal=len(Xtt);
	conteo=0
	cosa=[None]*tal
	for i in range(tal):
		cosa[i]=[None]*1
	cosa=array(cosa)
	while conteo<tal:
		cosa[conteo]=Xtt[conteo,0]
		conteo=conteo+1
	sol=array(cosa)
	return(sol)

def determinante(b):
	deter=b[0][0]*b[1][1]*b[2][2]+(b[0][1]*b[1][2]*b[2][0])+(b[0][2]*b[1][0]*b[2][1])-[b[2][0]*b[1][1]*b[0][2]+(b[2][1]*b[1][2]*b[0][0])+(b[2][2]*b[1][0]*b[0][1])]
	if deter==0:
		deter=1
	return deter

def inver(b):
	w=[(1.676,0.6,0.0),(0.0,0.0,7.76),(0.0,9.0,0.0)]
	w=array(w)
	a=w.copy()
	deter=determinante(b)
	
	a[0,0]=(1/deter)*(b[1,1]*b[2,2]-b[1,2]*b[2,1])
	a[0,1]=(1/deter)*(b[0,2]*b[2,1]-b[0,1]*b[2,2])
	a[0,2]=(1/deter)*(b[0,1]*b[1,2]-b[0,2]*b[1,1])
	
	a[1,0]=(1/deter)*(b[1,2]*b[2,0]-b[1,0]*b[2,2])
	a[1,1]=(1/deter)*(b[0,0]*b[2,2]-b[0,2]*b[2,0])
	a[1,2]=(1/deter)*(b[0,2]*b[1,0]-b[0,0]*b[1,2])
	
	a[2,0]=(1/deter)*(b[1,0]*b[2,1]-b[1,1]*b[2,0])
	a[2,1]=(1/deter)*(b[0,1]*b[2,0]-b[0,0]*b[2,1])
	a[2,2]=(1/deter)*(b[0,0]*b[1,1]-b[0,1]*b[1,0])
	
	return a
def dote(Xt,X):
	tal=len(Xt[1]);
	tal2=len(X[1]);
	tal3=len(Xt);
	w=[0.0]*tal3
	for i in range(tal3):
		w[i]=[0.0]*tal2
	w=array(w)
	aw=w.copy()
	conteo=0
	conteo2=0
	conteo3=0
	solucion=0
	while conteo3<tal3:
		while conteo<tal2:
			while conteo2< tal:
				solucion=solucion+Xt[conteo3,conteo2]*X[conteo2,conteo]
				conteo2=conteo2+1
			aw[conteo3,conteo]=solucion
			solucion=0;
			conteo=conteo+1
			conteo2=0
		conteo=0
		conteo3=conteo3+1;
	return(aw)
	
	

def curva(tiempo,datos):
	x=tiempo
	y=array(datos)
	tamaño=len(x)
	h=[1]*tamaño
	dls=[0]*tamaño
	re=0;
	while re<tamaño:
		dls[re]=x[re]*x[re]
		re=re+1;
		
	f=[]
	f.append(lambda x:h)
	f.append(lambda x:x)
	f.append(lambda x:dls)
	Xt=[]
	for fu in f:
		Xt.append(fu(x))
	Xt= array(Xt)
	X=transp(Xt);
	multi=dote(Xt,X)
	multiplicacion=inver(multi)
	multiplicacion1=dote(multiplicacion,Xt)
	ya=transp2(y)
	a = dote(multiplicacion1,ya)
	a=transp3(a)
	return a

def calc(image,hz,dx):
	
	temp=1/hz	
	bs=image
	b=bs[:]
	lalala, numf = labels(b)
	datos=centrol(lalala,dx)
	tiempo=[]
	cpt=0
	while cpt<numf:
		tiempo.append(temp*cpt)
		cpt=cpt+1
	a=curva(tiempo,datos)
	acel=a[2]*2
	return (acel)   
