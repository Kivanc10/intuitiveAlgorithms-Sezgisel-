# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:02:05 2020

@author: Kivanc
"""

#%%
from random import uniform,randint,sample # liste karıştırmak için sample,değer üretmek için randint ve uniform
import time # çalışma süresini ölçmek için time

a=time.time()

distanceMatrix = [[0 , 29 , 20 , 21 , 16 , 31 , 100 ,12 , 4  , 31 ],
[29 , 0  , 15 , 29 , 28 , 40 , 72 , 21 , 29 , 41 ],
[20 , 15 , 0  , 15 , 14 , 25 , 81 , 9  , 23 , 27 ],
[21 , 29 , 15 , 0  , 4 ,  12 , 92 , 12 , 25 , 13 ],
[16 , 28 , 14 , 4  , 0 ,  16 , 94 , 9  , 20 , 16 ],                               
[31 , 40 , 25 , 12 , 16 , 0 ,  95 , 24 , 36 , 3 ],
[100 ,72 , 81 , 92 , 94 , 95 , 0 ,  90 , 101 ,99 ],
[12 , 21 , 9 ,  12 , 9  , 24 , 90 , 0  , 15 , 25 ],
[4  , 29 , 23 , 25 , 20 , 36 , 101 ,15 , 0 ,  35,],
[31 , 41 , 27 , 13 , 16 , 3 ,  99,  25,  35,  0 ]]

def calculateCost(solution): # mesafe hesaplayan fonksiyon
    totalDistance=0 # maliyet hesaplayan fonk
    index=solution[0]
    for nextIndex in solution[1:]:
        totalDistance+=distanceMatrix[index][nextIndex]
        index=nextIndex
    return totalDistance

def swap(sequence,i,j): # indis değiştirme fonskyonu
    temp=sequence[i]
    sequence[i]=sequence[j] #indis değiştirme fonk
    sequence[j]=temp

def randF(): # 0 ile 1 arasında rastgele değer üreten fonksiyon.
    return uniform(0.0001,0.9999)
    
goMethods=int(2 + ((randF()-0.5) * 2) * (2.5 - 1.2)) # karıncalar için ilerleme metodu.

def roulettaSelection(bees): # gözcü arıları seçmek için rulet yöntemi
    total=0
    section=0
    for i in range(len(bees)):
        total+=(1/float(bees[i][1])) # toplam uygunluk değeri hesaplama
    probability=[] # olasılık listesi
    for i in range(len(bees)):
        section+=float((1/int(bees[i][1]))/total) # herbirinin seçilme olasılığı(toplam uygunluk değerine bölerek bulunur.)
        probability.append(section) # olasılık listesine eklendi.
    nextGeneration=[] # yeni jenerasyon
    for i in range(numFeeds): # besin sayısı kadar (gözcü arı sayısına eşit) seçim yapma ve seçme
        choice=randF() # random seçimler yapılıyor.
        for j in range(len(probability)):
            if (choice <= probability[j]):
                nextGeneration.append(bees[j])
                break
    temp=sample(nextGeneration,numFeeds) # yeni jenerasyonun içi karıştırıldı ve fonksiyonda döndürüldü
    nextGeneration=temp
    return nextGeneration

def approachtoGood(bees,a,b,c): # çözüm kümelerine uygulanan iyileştirme formülü
    bees=bees[0][:]
    swap(bees,a,b)
    swap(bees,b,c)
    return (bees,calculateCost(bees))

numBees=10 # arı sayısı
workerBees=5 # işçi arı sayısı
iteration=100 # iterasyon sayısı
numFeeds=5 # besin sayısı
limitsOfTry=5 # algoritmanın deneme limiti
n=len(distanceMatrix)  #GSP büyüklüğü
bees=[] # arı için array
firstPath=list(range(0,n)) # çizilin ilk yol(rota)
index=0

for i in range(numBees): # başlangıçta arı sayısı kadar rota oluşturuldu.
    path=sample(firstPath,n)
    bees.append((path,calculateCost(path)))
bees.sort(key=lambda x:x[1]) # en az maliyete göre sıraladık.

def removeBees(bees,a,b,c,d): # rota ortadan kaldırma (eleme) fonksiyonu deneme limitine bağlıdır.
    bees=bees[0][:]
    index1=randint(0,n-1)
    index2=randint(0,n-1)
    index3=randint(0,n-1)
    index4=randint(0,n-1)
    
    swap(bees,index1,index2)
    swap(bees,index2,index3)
    swap(bees,index3,index4)
    
    return (bees,calculateCost(bees))
        
while(iteration!=0):
    count=0 # sayaç
    bestBees=bees[randint(0,goMethods)] # metotla yola çıkacak grup belirlenir.
    for j in range(0,n):
        morePowerBees=approachtoGood(bestBees,randint(0,n-1),randint(0,n-1),randint(0,n-1)) # gidecek gruba iyileştirme uygulanır.
        if (bees[j][1]>morePowerBees[1]): # Elde edilen çözüm değeri önceki çözüm değerinden daha iyi ise listeye alınır.
            bees[j]=morePowerBees # listeye alındı.
        else:
            limitsOfTry+=1 # eğer iyileşme sağlanırsa limit değeri 1 arttırılır.
    bees.sort(key=lambda x:x[1]) # en az maliyete göre sıralanır.
    for i in range(numBees-workerBees,numBees):
        observer=roulettaSelection(bees) # gözcü arılar rulet seçimine göre seçilir.
        for l in range(workerBees,numBees):
            bees[l]=observer[count] # gözcü arılardan az maliyetli olanlar arı listesine alınır.
    count+=1
    if (count>limitsOfTry): # eğer sayaç deneme limitinden fazla ise arılar ortadan kaldırılır.(removeBees fonskiyonu ile)
        for k in range(n):
            bees[k]=removeBees(bees,randint(0,n-1),randint(0,n-1),randint(0,n-1),randint(0,n-1)) # iyileştirilemeyen çözüm kümeleri(rotalar) kaldırıldı.
    bees.sort(key=lambda x:x[1])  # en az maliyete göre sırala.
    iteration-=1
b=time.time()

print("En iyi yol : ",bees[0][0])
print("En iyi maliyet :  ",bees[0][1])
print("Algoritma çalışma süresi : ",b-a)
