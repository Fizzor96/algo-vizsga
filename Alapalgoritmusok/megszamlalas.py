sor = [1, 2, 5, 7, 9, 12, 4, 6, 8, 11, 13, 20, 15, 5, 5, 5]

def megszamlalas(sorozat):
    db = 0
    for i in range(len(sorozat)):
        #T tulajdonságú elem pl. 5
        if sorozat[i] == 5:
            db = db + 1
    return db

print(megszamlalas(sor))