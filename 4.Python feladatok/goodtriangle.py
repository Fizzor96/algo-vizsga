import math

class Point():
    def __init__(self, x, y):
        self.x=x
        self.y=y

#adjunk meg egy pontot
point=Point(1.5,2)

#a háromszög pontjai
a=Point(6,0)
b=Point(0,0)
c=Point(3,4)

if a.y!=0:
    tgalph=(a.x)/(a.y)
else:
    tgalph=1
if c.x !=0:
    tgbet=c.y/c.x
else:
    tgbet=1
if a.x!=0:
    tggamm=((c.y-a.y)/a.x)
else:
    tggamm=1

k1=Point(point.x, tgalph*point.x)
k2=Point(point.y/tgbet, point.y)
k3=Point((-((point.y-a.y)/tggamm))+a.x, point.y)

print("point.x: " + str(point.x) + " ,point.y: " + str(point.y) + " ,k1.x: " + str(k1.x) + " ,k1.y: " + str(k1.y) + " ,k2.x: " + str(k2.x) + " ,k2.y: " + str(k2.y) + " ,k3.x: " + str(k3.x) + " ,k3.y: " + str(k3.y))

def bennevan():
    if point.y > k1.y and point.x > k2.x and point.x < k3.x:
        return print("benne vna a háromszögben!")
def nincsbenne():
    if point.y < k1.y or point.x < k2.x or point.x > k3.x or point.y > c.y:
        return print("nincs benne a háromszögben!")
def rajtavan():
    if point.x == k1.x and point.y == k1.y or point.x == k2.x and point.y == k2.y or point.x == k3.x and point.y == k3.y:
        return print("a pont rajta van a háromszög vonalán!")

bennevan()
nincsbenne()
rajtavan()

#if point.y > k1.y and point.x > k2.x and point.x < k3.x:
#    print("benne vna a háromszögben!")
#elif point.y < k1.y or point.x < k2.x or point.x > k3.x or point.y > c.y:
#    print("nincs benne a háromszögben!")
#elif point.x == k1.x and point.y == k1.y or point.x == k2.x and point.y == k2.y or point.x == k3.x and point.y == k3.y:
#    print("a pont rajta van a háromszög vonalán!")
#else:
#    print("hülye vagyok a feladathoz!")