sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
sorozat.sort()
print(sorozat)

def linkerrend(sor, T):
    i = 0
    while(i<len(sor)) and (T>sor[i]):
        i = i + 1
    return (i<len(sor)) and (T==sor[i]), i

print(linkerrend(sorozat, 6))