sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
print(sorozat)

def shellSort(sor):
    gap=len(sor)
    n = gap // 2
    while n > 0:
        for i in range(n, gap):
            temp = sor[i]
            j = i
            while j >= n and sor[j-n] > temp:
                sor[j] = sor[j-n]
                j -= n
            sor[j] = temp
        n //= 2

shellSort(sorozat)
print(sorozat)
