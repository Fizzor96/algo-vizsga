sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]

def strazsas(sor, T):
    i = 0
    sor.append(T)
    while (sor[i] != T):
        i = i + 1
    return i, i<len(sor)

print(strazsas(sorozat, 111))
    