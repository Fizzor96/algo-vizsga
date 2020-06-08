sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print("kezdő")
print(sorozat)
print("----------------------------------------")

def rendez(sor):
    for j in range(0, len(sor)-1):
        for i in range(j+1, len(sor)):
            if sor[i] < sor[j]:
                c = sor[i]
                sor[i] = sor[j]
                sor[j] = c
            print(sor)
        #print(sor)

rendez(sorozat)
print("----------------------------------------")
print("végső")
print(sorozat)