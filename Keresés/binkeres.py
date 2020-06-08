sorozat = [3, 5, 9, 10, 33, 2, 5 , 4, 6, 8, 11, 12]
sorozat.sort()
print(sorozat)

def binkeres(sor, T):
    eleje = 0
    vege = len(sor)
    kozepe = (int)((eleje + vege) / 2)
    while (eleje <= vege and sor[kozepe]!=T):
        if T<sor[kozepe]:
            vege = kozepe - 1
        else:
            eleje = kozepe + 1
        kozepe = (int)((eleje + vege) / 2)
    return "helye: ", kozepe, " erteke: ", sor[kozepe]

print(binkeres(sorozat, 6))