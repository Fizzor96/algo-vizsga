import numpy as np
from numpy import random as rnd
import math

tomb = rnd.randint(100, size=(10, 10))
print(tomb)

def foatloatlag(matrixmeret):
    atlag=0
    for i in range (0, matrixmeret):
        atlag=atlag+tomb[i,i]
    return atlag

print(foatloatlag(len(tomb)))

def foatloatlagelj():
    atlag=0
    for i in range (0, len(tomb)):
        atlag+=tomb[i,i]
    print(atlag)

foatloatlagelj()

x = rnd.randint(100, size=(30))

print(x)