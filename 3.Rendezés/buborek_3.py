sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print(sorozat)

def buborek(sor):
    j=1
    while(j<=len(sor)-1):
        csereH=0
        for i in range(0, len(sor)-j):
            if sor[i]>sor[i+1]:
                c=sor[i]
                sor[i]=sor[i+1]
                sor[i+1]=c
                csereH=i
        j=(len(sor)-csereH)

buborek(sorozat)
print(sorozat)