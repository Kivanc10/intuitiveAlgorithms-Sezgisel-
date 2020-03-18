# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 22:59:12 2020

@author: Kivanc
"""

#%%
from random import uniform , randint  
import math
import time
import numpy
a=time.time()

#Gezgin Satıcı Problemi
distanceMatrix = [[0 , 29 , 20 , 21 , 16 , 31 , 100 ,12 , 4  , 31],
[29 , 0  , 15 , 29 , 28 , 40 , 72 , 21 , 29 , 41],
[20 , 15 , 0  , 15 , 14 , 25 , 81 , 9  , 23 , 27],                    
[21 , 29 , 15 , 0  , 4 ,  12 , 92 , 12 , 25 , 13],
[16 , 28 , 14 , 4  , 0 ,  16 , 94 , 9  , 20 , 16],
[31 , 40 , 25 , 12 , 16 , 0 ,  95 , 24 , 36 , 3],
[100 ,72 , 81 , 92 , 94 , 95 , 0 ,  90 , 101 ,99],
[12 , 21 , 9 ,  12 , 9  , 24 , 90 , 0  , 15 , 25],
[4  , 29 , 23 , 25 , 20 , 36 , 101 ,15 , 0 ,  35],
[31 , 41 , 27 , 13 , 16 , 3 ,  99,  25,  35,  0]]

def calculateDistance(path):
  index = path[0]             # Düğümler arası uzaklık hesabı
  distance = 0
  for nextIndex in path[1:]:
    distance += distanceMatrix[index][nextIndex]
    index = nextIndex
  return distance # 

def swap(sequence,i,j):
  temp = sequence[i]     #Düğüm yer değiştirme fonksiyonu
  sequence[i]=sequence[j]
  sequence[j]=temp

def localPhremone(ants,a,b):
    ants=ants[0][:]
    swap(ants,a,b)
    return (ants,calculateDistance(ants))

def globalPhremone(ants,a,b,c):
    ants=ants[0][:]
    swap(ants,a,b)
    swap(ants,b,c)
    return (ants,calculateDistance(ants))

    
numAnts=10

worstAnts=int(0.1*numAnts)

bestAnts=int(0.8*numAnts)

alfa=2

beta=2

passMax=10

passMin=0

iterationSize=100

n=len(distanceMatrix)

passMethod=alfa*1/n*beta*(passMax-passMin)

ants=[]

initPath=list(range(0,n))

index=0

transitionProbability=0.9



for i in range(numAnts):
    if index==n-1:
        index=0
    swap(initPath,index,index+1)
    index+=1
    ants.append((initPath[:],calculateDistance(initPath)))
ants.sort(key=lambda x:x[1])

for iterationIndex in range(0,iterationSize):
    goAnts=ants[randint(0,bestAnts)] # göç edicek grup
    randomAntsIndex=randint(0,passMethod)
    if(numpy.random.random()<transitionProbability):
            morePowerAnts=globalPhremone(goAnts,randint(0,n-1),randint(0,n-1),randint(0,n-1))
            if(ants[randomAntsIndex][1]>morePowerAnts[1]):
                ants[randomAntsIndex]=morePowerAnts
    else:
        morePowerAnts=localPhremone(goAnts,randint(0, n - 1),randint(0, n - 1)) # yolları bulamayanalara güncelleme yaptık.
    for i in range(numAnts-worstAnts,numAnts):
        ants[i]=localPhremone(ants[i],randint(0,n-1),randint(0,n-1))
    ants.sort(key=lambda x:x[1])

b=time.time()

print("En iyi yol : ",ants[0][0])   
print("En iyi maliyet =  ",ants[0][1])
print("Algoritma çalışma süresi : ",b-a)

    
        
            
        
    


    
    
    
        
    
    
    
    





    

            
            


        

    
    
