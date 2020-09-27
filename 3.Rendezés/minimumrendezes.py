sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print(sorozat)

def minimumrendezes(sor):
    for j in range(0, len(sor)-1):
        minI=j
        for i in range(j+1, len(sor)):
            if sor[i] < sor[minI]:
                minI=i
        if minI != j:
            c = sor[minI]
            sor[minI] = sor[j]
            sor[j] = c

minimumrendezes(sorozat)
print(sorozat)