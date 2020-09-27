sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]

def minH(sor):
    hely = 0
    for i in range(1, len(sor)):
        if sor[i]<sor[hely]:
            hely = i
    return hely

print(minH(sorozat))