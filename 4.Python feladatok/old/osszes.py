import numpy as np
from numpy import random as rnd

sorozat=rnd.randint(100, size=(30))
sorozat2=np.array([1, 3, 5])

print (sorozat)

def vaneparosfor(sor):
    paros=False
    for i in range(len(sor)):
        if sor[i]%2==0:
            paros=True
    return paros

a = vaneparosfor(sorozat)
b = vaneparosfor(sorozat2)
print (a)
print (b)


def vaneparoswhile(sor):
    i=0
    paros=False
    while i < (len(sor)):
        if sor[i]%2==0:
           paros=True
        i=i+1
    return paros

c = vaneparoswhile(sorozat)
d = vaneparoswhile(sorozat2)
print (c)
print (d)


def holvan(sor, szam):
    keresett=-1
    for i in range (len(sor)):
        if sor[i]==szam:
            keresett = i
    return keresett

e = holvan(sorozat, 22)
print (e)



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


   
