# -*- coding: utf-8 -*-
#%%
from random import randint

def randomSelectBacterias(size):
    return [randint(1,nVezir) for _ in range(nVezir)]



def fitness(bacterium):
    horizontalCollisions=sum([bacterium.count(queen)-1 for queen in bacterium])/2
    diagonalCollisions=0
    n=len(bacterium)
    leftDiagonal=[0]*2*n
    rightDiagonal=[0]*2*n
    for i in range(n):
        leftDiagonal[i+bacterium[i]-1]+=1
        rightDiagonal[len(bacterium)-i+bacterium[i]-2]+=1
    diagonalCollisions=0
    for i in range(2*n-1):
        counter=0
        if leftDiagonal[i]>1:
            counter+=leftDiagonal[i]-1
        if rightDiagonal[i]>1:
            counter+=rightDiagonal[i]-1
        diagonalCollisions+=counter/(n-abs(i-n+1))
    return int(maxFitness-(horizontalCollisions+diagonalCollisions))


def changed(x):
    n=len(x)
    c=randint(0,n-1)
    m=randint(1,n)
    x[c]=m
    return x


def elimination(bacteria):
    changed(bacteria)
    changed(bacteria)
    changed(bacteria)
    changed(bacteria)
    return bacteria


def kemotaxis(bacteria):
    changed(bacteria)
    changed(bacteria)
    return bacteria

def printBacteria(bacteria):
    print("Bacteria = {},Fitness = {}".format(str(bacteria),fitness(bacteria)))

if __name__ == "__main__":
    nVezir=int(input("Enter count of queens"))
    maxFitness=(nVezir*(nVezir-1))/2
    generation=1
    iteration=100
    bacteria=[randomSelectBacterias(nVezir) for _ in range(iteration)]
    worstBacteria=int((nVezir*0.5))
    bacteria.sort(key=lambda x:x[1])
    while not maxFitness in [fitness(n) for n in bacteria]:
        print("=== Generation = {} ===".format(generation))
        print("=== Maximum fitness = {}".format(max([fitness(n) for n in bacteria])))
        generation+=1
        bestBacterium=bacteria[0]
        for j in range(nVezir):
            morePowerfulBacterium=kemotaxis(bestBacterium)
            if (bacteria[j][1]>morePowerfulBacterium[1]):
                bacteria[j]=morePowerfulBacterium
            for k in range(nVezir-worstBacteria,nVezir):
                bacteria[k]=kemotaxis(bacteria[k])
        bacteria.sort(key=lambda x:x[1])            
        if (randint(0,1000)==0):
            for j in range(nVezir):
                bacteria[j]=elimination(bacteria[j])                
        bacteria.sort(key=lambda x:x[1])
    bacteriaOut=[]
    for n in bacteria:
        if fitness(n)==maxFitness:
            print("One of the solutions : ") 
            bacteriaOut=n
            printBacteria(n)
    
    board=[]
    for x in range(nVezir):
        board.append([" X "]*nVezir)
    
    for i in range(nVezir):
        board[nVezir-bacteriaOut[i]][i]=" V "
    
    def printBoard(board):
        for row in board:
            print("".join(row))
    
    printBoard(board)
    

        
        

    
    
    
    
    