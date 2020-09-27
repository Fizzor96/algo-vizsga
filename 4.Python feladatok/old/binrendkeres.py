import numpy as np
from numpy import random as rnd

sorozat=rnd.randint(100, size=(30))

def binrendkeres(sor, szam):
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
    g = 0

    if len(t2)%2 == 0:
        g = int(len(t2)/2)
        if t2[g] <= szam:
            for i in range (g, len(t2)):
                if t2[i] == szam:
                    k = i
        elif t2[g] > szam:
            for i in range (g, 0, -1):
                if t2[i] == szam:
                    k = i
    elif len(t2)%2 != 0:
        g = int((len(t2)-1)/2)
        if t2[g] <= szam:
            for i in range(g, len(t2)):
                if t2[i] == szam:
                    k = i
        elif t2[g] > szam:
            for i in range (g, 0, -1):
                if t2[i] == szam:
                    k = i
    print(t2)
    return k

print (binrendkeres(sorozat, 15))