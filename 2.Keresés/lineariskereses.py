sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]

def linkeres(sor, T):
    i = 0
    while (i<len(sor)) and (sor[i] != T):
        i = i + 1
    return i, i<len(sor)

print(linkeres(sorozat, 4))