sor = [1, 2, 5, 7, 9, 12, 4, 6, 8, 11, 13, 20, 15]

def osszegzes(sorozat):
    sum = 0
    for i in range(len(sorozat)):
        sum = sum + sor[i]
    return sum

print(osszegzes(sor))