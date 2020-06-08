sor = [2,5,3,1,4]
sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print("eredeti: ", sorozat)
print("-------------------------")

def beszuro(sorozat):
    c=len(sorozat)-1
    for j in range(c):
        i=j
        x=sorozat[j+1]
        while i>=0 and sorozat[i]>x:
            sorozat[i+1]=sorozat[i]
            i=i-1
        sorozat[i+1]=x
        print("rendez:  ", sorozat)

beszuro(sorozat)