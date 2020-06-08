sorozat = [3, 5, 9, 10, 33, 2 , 4, 6, 8, 11, 12]
print(sorozat)

def koktel(sor):
    n = len(sor)
    csere = True
    eleje = 0
    vege = n-1
    while(csere == True):
        csere = False
        for i in range(eleje, vege):
            if sor[i] > sor[i+1]:
                sor[i], sor[i+1] = sor[i+1], sor[i]
                csere = True
        if csere == False:
            break
        csere = False
        vege = vege - 1
        for i in range(vege-1, eleje-1, -1):
            if sor[i] > sor[i+1]:
                sor[i], sor[i+1] = sor[i+1], sor[i]
                csere = True
        eleje = eleje + 1

koktel(sorozat)
print(sorozat)