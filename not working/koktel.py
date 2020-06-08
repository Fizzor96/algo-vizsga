sorozat = [3, 5, 9, 10, 33, 2 , 4, 6, 8, 11, 12]
print(sorozat)

def koktel(sor):
    eleje = 1
    vege = len(sor) - 1
    voltcsere = True
    cserehelye = vege
    while voltcsere:
        voltcsere = False
        for j in range(eleje, vege):
            csere = sor[j]
            sor[j] = sor[j+1]
            sor[j+1] = csere
            cserehelye = j
            voltcsere = True
        vege = cserehelye
        for j in range(vege, eleje):
            if sor[j] < sor[j-1]:
                csere = sor[j]
                sor[j] = sor[j-1]
                sor[j-1] = csere
                cserehelye = j
                voltcsere = True
        eleje = cserehelye

koktel(sorozat)
#print(sorozat)