# Conway's Game of Life

import numpy as np
import matplotlib.pyplot as plt


def universe(N):
    global universe
    universe=np.zeros((N,N))

def board(x):
    global board
    #board=eval(input("Enter the board as a list of lists : "))
    board=x
    board=np.array(board)

def map(i,j,u):
    if i==0 and j==0:
        mp=u[i:i+2,j:j+2]
    elif i==0:
        mp=u[i:i+2,j-1:j+2]
    elif j==0:
        mp=u[i-1:i+2,j:j+2]
    elif i!=0 and j!=0:
        mp=u[i-1:i+2,j-1:j+2]
    else:
        print('Error 1')
    if u[i,j]:
        nbr=(np.count_nonzero(mp))-1
    elif u[i,j]==0:
        nbr=(np.count_nonzero(mp))
    else:
        print('Error 2')
    return nbr

def cndtn(i,j,u):
    if map(i,j,u)<2 and u[i,j]==1:
        return 0
    elif 2<=map(i,j,u)<=3 and u[i,j]==1:
        return 1
    elif map(i,j,u)>3 and u[i,j]==1:
        return 0
    elif map(i,j,u)==3 and u[i,j]==0:
        return 1
    elif map(i,j,u)!=3 and u[i,j]==0:
        return 0
    else:
        print('Error 3')

def change(u):
    nuniv=np.zeros((len(u),len(u)))
    for i in range(len(u)):
        for j in range(len(u)):
            nuniv[i,j]=cndtn(i,j,u)
    return nuniv

def start(x):
    u=x
    for i in range(30):
        plt.imshow(u,cmap='binary')
        plt.draw()
        plt.pause(0.5)
        u=change(u)


 
universe(88)
board([[0,1,1,0,0,1,1,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0],[1,0,1,0,0,1,0,1],[1,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,1],[0,1,1,0,0,1,1,0],[0,0,1,1,1,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0],[0,0,0,1,1,0,0,0]])
universe[33:45,40:48]=board
start(universe)
