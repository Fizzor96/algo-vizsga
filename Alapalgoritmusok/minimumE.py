sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]

def minE(sor):
    ertekM = sor[0]
    for i in range(1, len(sor)):
        if sor[i]<ertekM:
            ertekM = sor[i]
    return ertekM

print(minE(sorozat))