import numpy as np
from numpy import random as rnd
import random

sorozat=rnd.randint(100, size=(30))
sorozat2=np.array([1, 3, 5])
concArr1 = [11, 11, 23, 36, 41, 48, 48, 50, 50, 50]
concArr2 = [23, 36, 40, 46, 49]

def vaneparosfor(sor):
    paros=False
    for i in range(len(sor)):
        if sor[i]%2==0:
            paros=True
    return paros

def vaneparoswhile(sor):
    i=0
    paros=False
    while i < (len(sor)):
        if sor[i]%2==0:
           paros=True
        i=i+1
    return paros

def holvan(sor, szam):
    keresett=-1
    for i in range (len(sor)):
        if sor[i]==szam:
            keresett = i
    return keresett

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

def keresetthely(sor, szam):
    k = -1
    for i in range(0, len(sor)):
        if sor[i] == szam:
            k = i
    return k

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

def feltoltrendezve(rndintervallum, tombhossz):
    r = []
    a = 0
    i = 0
    r.append(random.randint(1, rndintervallum))
    while len(r) != tombhossz:
        a = random.randint(1, rndintervallum)
        if r[i] <= a:
            r.append(a)
            #print(r)
            i = i + 1
    #print("A tömbünk mérete: " + str(len(r)))
    print(r)
    return r

def szamegyenlo(szam, marr):
    d = 0
    p = False
    while d != len(marr):
        if szam == marr[d]:
            p = True
        else:
            p = False
        d = d + 1
    return p

def bennevane (ez, ebben):
    k = []
    #print("EZ = " + str(ez[i]))
    #print("EBBEN = " + str(ebben[b]))
    for i in range(len(ez)):
        k.append(szamegyenlo(ez[i], ebben))
    #print(len(k))
    print("K = " + str(k))
    return k

print (sorozat)
print (sorozat2)
print (vaneparosfor(sorozat))
print (vaneparosfor(sorozat2))
print (vaneparoswhile(sorozat))
print (vaneparoswhile(sorozat2))
print (holvan(sorozat, 22))
print(rendez(sorozat))
print(keresetthely(rendez(sorozat), 22))
print(rendkeres(sorozat, 22))
print (binrendkeres(sorozat, 15))

firstArr = feltoltrendezve(50, 20)
print(firstArr)
#print(len(firstArr))
secondArr = feltoltrendezve(50, 10)
print(secondArr)
#print(len(secondArr))
tftomb = bennevane(secondArr, firstArr)
print(tftomb)
#print(len(tftomb))


#sorozat=rnd.randint(100, size=(10))
#sorozat2=np.array([1, 2, 3, 4, 5, 6, 12, 3, 51, 20, 42, 31, 52, 60])
#sorozat3=np.array([3, 2, 1, 4, 5, 6, 9 ,4])
#sorozat4=np.array([2, 4, 1, 3])
#s1=np.array([2, 4, 1, 3])
#s2=[2, 4, 1, 3]