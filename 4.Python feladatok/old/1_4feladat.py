import numpy as np
from numpy import random as rnd
import math

sorozat=rnd.randint(100, size=(10))
#sorozat2=np.array([1, 2, 3, 4, 5, 6, 12, 3, 51, 20, 42, 31, 52, 60])
#sorozat3=np.array([3, 2, 1, 4, 5, 6, 9 ,4])
#sorozat4=np.array([2, 4, 1, 3])
#s1=np.array([2, 4, 1, 3])
#s2=[2, 4, 1, 3]

def rendez(sor):
    t1 = []
    t2 = []
    #tömb->lista
    for a in range (0, len(sor)):
        t1.append(sor[a])
    for b in range (0, len(sor)):
        #print(i)
        minert = t1[0]
        for b in range (0, len(t1)):
            if t1[b] < minert:
                minert = t1[b]
        #print(minert)
        t1.remove(minert)
        t2.append(minert)
    return t2

print(sorozat)
print(rendez(sorozat))

def keresetthely(sor, szam):
    k = -1
    for i in range(0, len(sor)):
        if sor[i] == szam:
            k = i
    return k

print(keresetthely(rendez(sorozat), 22))

def rendkeres(sor, szam):
    t1 = []
    t2 = []
    #tömb->lista
    for a in range (0, len(sor)):
        t1.append(sor[a])
    for b in range (0, len(sor)):
        #print(i)
        minert = t1[0]
        for b in range (0, len(t1)):
            if t1[b] < minert:
                minert = t1[b]
        #print(minert)
        t1.remove(minert)
        t2.append(minert)
    k = -1
    for i in range(0, len(t2)):
        if t2[i] == szam:
            k = i
    return k

print(rendkeres(sorozat, 22))
