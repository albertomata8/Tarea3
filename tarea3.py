#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 12:19:20 2020

@author: Alberto Mata B74558
"""

def densidadMarginal(lista,posicion):
    "Funcion para obtener la densidad marginal de una x#"
    i=1
    while i<22:
        lista.append(df.iloc[posicion,i])
        i=i+1
    return np.sum(lista)

def allPx(lista):
    "Funcion para obtener en una lista todas las densidades marginales de x"
    x5=[]
    lista.append(densidadMarginal(x5,0))

    x6=[]
    lista.append(densidadMarginal(x6,1))

    x7=[]
    lista.append(densidadMarginal(x7,2))

    x8=[]
    lista.append(densidadMarginal(x8,3))

    x9=[]
    lista.append(densidadMarginal(x9,4))

    x10=[]
    lista.append(densidadMarginal(x10,5))

    x11=[]
    lista.append(densidadMarginal(x11,6))

    x12=[]
    lista.append(densidadMarginal(x12,7))
    
    x13=[]
    lista.append(densidadMarginal(x13,8))
    
    x14=[]
    lista.append(densidadMarginal(x14,9))
    
    x15=[]
    lista.append(densidadMarginal(x15,10))
    
def allPy(lista):
    """Funcion para obtener la densidad marginal de y. Note que se utilizo iloc para 
    facilitar el proceso. En x no se uso debido a que la funcion iloc daba error cuando
    uno le ponia np.sum"""
    
    i=1
    while i<22:
        lista.append(np.sum(df.iloc[:,i]))
        i=i+1
def llenarvalores(lista,limite):
    "Funcion para agregar los valores respectivos de x y y"
    i=5
    while i<limite+1:
        lista.append(i)
        i=i+1
    
import pandas as pd#extraer datos
import numpy as np# calculos matematicos
from matplotlib import pyplot as plt#graficas
from scipy.optimize import curve_fit#curvas de ajuste
from mpl_toolkits.mplot3d import Axes3D#grafica en 3D

"Problema #1"
datos=pd.read_csv('xy.csv', header=0)
df=pd.DataFrame(datos)
Px=[]
Py=[]

allPx(Px)#Mediante esta funcion se llena la lista Px con todas las densidades marginales
allPy(Py)#Mediante esta funcion se llena la lista Px con todas las densidades marginales
x=[]
llenarvalores(x,15)#Mediante esta funcion se llena la lista x con todos sus valores
y=[]
llenarvalores(y,25)#Mediante esta funcion se llena la lista y con todos sus valores

"Se crean las gráficas para ver a que modelo se parecen aproximadamente"
plt.bar(x,Px)
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Distribucion en X')
plt.show()

plt.bar(y,Py)
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Distribucion en Y')
plt.show()
"Observando las curvas se sabe que tiene que ajustarse a una curva gaussiana"
def gaussiana(dom,mu,sigma):#funcion gaussiana
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(dom - mu)**2/(2*sigma**2))

param,_=curve_fit(gaussiana,x,Px)
print("****************************Pregunta 1************************************")
print("La mejor curva de ajuste en X posee los seguientes parametros: ",param)


xajuste=gaussiana(x,param[0],param[1])
plt.bar(x,Px)
plt.plot(x,xajuste, "yellow")
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Mejor curva de ajuste en X')
plt.show()


param2,_=curve_fit(gaussiana,y,Py)
print("La mejor curva de ajuste en Y posee los seguientes parametros: ",param2)
yajuste=gaussiana(y,param2[0],param2[1])
plt.bar(y,Py)
plt.plot(y,yajuste, "yellow")
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Mejor curva de ajuste en Y')
plt.show()

print("**************************** Pregunta 2 ************************************")
"""Pregunta #2:
Ya que se asumen independientes se tiene fx,y(x,y)=fx(x)fy(y), y por ende para 
la función de densidad conjunta que modela los datos, se multiplican ambas funciones.
Se llega al resultado de la ecuacion:"""
X, Y = np.meshgrid(x,y)#Se crea una matriz de coordenadas
"Funcion de densidad conjunta:"
fxy= (1/(2*np.pi*3.29944287*6.02693775))*np.exp(-(((X-9.90484381)**2)/(2*3.29944287**2) + ((Y-15.0794609)**2)/(2*6.02693775**2)))

print("**************************** Pregunta 3 ************************************")
"""Pregunta 3"""
"Correlacion:"
posicionx=0
posiciony=0
correlacion=[]
while posiciony<21:
    while posicionx<11:
        correlacion.append(x[posicionx]*y[posiciony]*df.iloc[posicionx,posiciony+1])
        posicionx=posicionx+1
    posicionx=0
    posiciony=1+posiciony

print("Correlacion",np.sum(correlacion))
"Se sabe que la media en gaussiana es mu"
mediax=param[0] 
mediay=param2[0]
posicionx=0
posiciony=0
covarianza=[]
while posiciony<21:
    while posicionx<11:
        covarianza.append((x[posicionx]-mediax)*(y[posiciony]-mediay)*df.iloc[posicionx,posiciony+1])
        posicionx=posicionx+1
    posicionx=0
    posiciony=1+posiciony
    
print("Covarianza",np.sum(covarianza))

coeficiente= np.sum(covarianza)/(param[1]*param2[1])

print("Coeficiente de correlacion: ",coeficiente)
print("**************************** Pregunta 4 ************************************")
plt.plot(x,xajuste)
plt.xlabel('Valor de X')
plt.ylabel('Densidad marginal en X')
plt.title('Distribucion en X')
plt.show()


plt.plot(y,yajuste)
plt.xlabel('Valor de Y')
plt.ylabel('Densidad marginal en Y')
plt.title('Distribucion en Y')
plt.show()

"Grafica 3D"
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, fxy)
ax.set_title('Densidad conjunta')
plt.show()

