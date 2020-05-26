# -*- coding: utf-8 -*-
#%%
from random import randint
import numpy as np


def randomFlowers(size):
    return [randint(1,nVezir) for _ in range(nVezir)]


def fitness(flower):
    horizontalCollisions=sum([flower.count(queen)-1 for queen in flower])/2
    diagonalCollisions=0
    n=len(flower)
    leftDiagonal=[0]*2*n
    rightDiagonal=[0]*2*n
    for i in range(n):
        leftDiagonal[i+flower[i]-1]+=1
        rightDiagonal[len(flower)-i+flower[i]-2]+=1
    diagonalCollisions=0
    for i in range(2*n-1):
        counter=0
        if leftDiagonal[i]>1:
            counter+=leftDiagonal[i]-1
        if rightDiagonal[i]>1:
            counter+=rightDiagonal[i]-1
        diagonalCollisions+=counter/(n-abs(i-n+1))
    return int(maxFitness-(horizontalCollisions+diagonalCollisions))


def printFlowers(solutions):
    print("solutions = {},fitness = {}".format(str(solutions),fitness(solutions)))


def changed(x):
    n=len(x)
    c=randint(0,n-1) # index için 
    m=randint(1,n) # x için 
    x[c]=m
    return x

def globalPollination(cloneSolution):
    changed(cloneSolution)
    changed(cloneSolution)
    changed(cloneSolution)
    changed(cloneSolution)
    return cloneSolution

def localPollination(cloneSolution):
    changed(cloneSolution)
    changed(cloneSolution)
    return cloneSolution


if __name__ == "__main__":
    nVezir = int(input("Enter count of queen"))
    maxFitness = (nVezir*(nVezir-1))/2
    iteration = 100
    generation = 1
    transitionProbability = 0.8
    solutions = [randomFlowers(nVezir) for _ in range(iteration)]
    cloneSolution = solutions.copy()
    solutions.sort(key = lambda x : x[1])
    bestSolution = solutions[0]
    while not maxFitness in [fitness(n) for n in solutions]:
        print("Generation = {}".format(generation))
        print("Maximum fitness = {}".format(max([fitness(n) for n in solutions])))
        generation+=1
        for i in range(nVezir):
            if np.random.random() < transitionProbability:
                cloneSolution[i] = globalPollination(cloneSolution[i])
            else:
                cloneSolution[i] = localPollination(cloneSolution[i])
            
            if (solutions[i][1] > cloneSolution[i][1]):
                solutions = cloneSolution
            
            solutions.sort(key = lambda x : x[1])
            
            if (bestSolution[i] > solutions[i][1]):
                bestSolution = solutions[i]
        
    flowersOut = []
    for path in solutions:
        print("One of the solutions = ")
        if fitness(path) == maxFitness:
            flowersOut = path
            printFlowers(path)
        
    board = []
        
    for x in range(nVezir):
        board.append([" X "]*nVezir)
    
    for i in range(nVezir):
        board[nVezir-flowersOut[i]][i] = " V "
        
    def printBoard(board):
         for row in board:
             print("".join(row))
        
    printBoard(board)
    print("Best solution = {}".format(bestSolution))
    
        
    
    
    
    
    
    
    
