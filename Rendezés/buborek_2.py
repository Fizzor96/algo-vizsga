sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print(sorozat)

def buborek(sor):
    j = 1
    csere = True
    while(j<=len(sor)-1) and (csere):
        csere=False
        for i in range(0, len(sor)-j):
            if sor[i] > sor[i+1]:
                c=sor[i]
                sor[i]=sor[i+1]
                sor[i+1]=c
                csere=True
        j=j+1

buborek(sorozat)
print(sorozat)