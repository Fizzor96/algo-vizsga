sorozatA = [1, 2, 3, 3, 3, 2, 1, 1, 1, 1]
sorozatB = [1, 2]

def kivalogat(sorA, sorB):
    db = 0
    for i in range(len(sorA)):
        for j in range(len(sorB)):
            if sorB[j] == sorA[i]:
                db = db + 1
    return db

print(kivalogat(sorozatA, sorozatB))