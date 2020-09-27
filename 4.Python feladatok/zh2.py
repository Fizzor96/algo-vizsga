import numpy as np
import random
import uuid

randintt=bool(random.randint(0,1))
mandaszin=("piros","kek","zold")

class Mandalorian:
  def __init__(self):
    self.private=False #Boolean
    self.colour="red" #String
    self.hunts=0 #Int
    self.id=0

  def generate_random(self, mid):
    self.private=bool(random.randint(0,1))
    self.colour=mandaszin[random.randint(0,len(mandaszin)-1)]
    self.hunts=random.randint(0,100)
    self.id=mid
    #ref mem
    #return obj in mem
    return self
  
  def ertekek(self):
    return self.private, self.colour, self.hunts, self.id

num=50
mandalorian_list=[Mandalorian().generate_random(x) for x in np.arange(num+1)]
#for i in range(0, len(mandalorian_list)):
  #print("private: ", mandalorian_list[i].private, " colour: ", mandalorian_list[i].colour, " hunts: ", mandalorian_list[i].hunts, " id: ", mandalorian_list[i].id)



def mandalorian_private(mandalorian_list):
  templist=[]
  for i in range(0, len(mandalorian_list)):
    if mandalorian_list[i].private == True:
      templist.append(mandalorian_list[i])
  return templist

privatelist=mandalorian_private(mandalorian_list)
print("--------------------------------------------------")
print("mandalorian_private:")
for i in range(0, len(privatelist)):
  print(privatelist[i].ertekek())

def mandalorian_not_private(mandalorian_list):
  templist=[]
  for i in range(0, len(mandalorian_list)):
    if mandalorian_list[i].private == False:
      templist.append(mandalorian_list[i])
  return templist

notprivatelist=mandalorian_not_private(mandalorian_list)
print("--------------------------------------------------")
print("mandalorian_not_private:")
for i in range(0, len(notprivatelist)):
  print(notprivatelist[i].ertekek())

def sort_private_hunts_bubble(arr):
  j=0
  while (j < len(arr)-1):
    lastSwap=0
    for i in range(0, len(arr)-1):
      if arr[i].hunts > arr[i+1].hunts:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        lastSwap=i
    j=len(arr)-lastSwap
  return arr

sort_private_hunts_bubble(notprivatelist)
sorted_not_private_list=sort_private_hunts_bubble(notprivatelist)

print("--------------------------------------------------")
print("sort_private_hunts_bubble:")
for i in range(0, len(sorted_not_private_list)):
  print(sorted_not_private_list[i].ertekek())

#hogy értelme legyen a feladatnak, 'hunts' range 0 és 100 között van
#ha újonc, akkor 50? bevetés? felett adjuk hozzá, ha nem újonc, akkor kék színű fejvadász adható hozzá
#újonc = 50 bevetés felett, nem private
#nem újonc = color:kék, private
#újonc = arr1, nem újonc = arr2
def merge_chosen(arr1,arr2):
  #arr3=[0] * (len(arr1)+len(arr2))
  #lista mérete ismeretlen, mert nem tudjuk, hogy mennyi mandalóriait adunk hozzá
  arr3=[]
  i = j = 0
  k=0
  while i < len(arr1) and j <len(arr2):
    #print(k, i, j)
    #print("len arr1: ", len(arr1), "len arr2: ", len(arr2))
    #print(arr1[i].hunts)
    if arr1[i].hunts > 50:
      arr3.append(arr1[i])
      i=i+1
      k=k+1
    else:
      i=i+1
    if arr2[j].colour == "kek":
      arr3.append(arr2[j])
      j=j+1
      k=k+1
    else:
      j=j+1
  return arr3

#tömb mérete megegyezik a résztömbök méretösszegével
#print([0] * (len(privatelist)+len(notprivatelist)))
chosen_list= merge_chosen(notprivatelist,privatelist)
print("--------------------------------------------------")
print("chosen_list:")
for i in range(0, len(chosen_list)):
  print(chosen_list[i].ertekek())

def binary_search_mandalorian(sorted_list):
    E=0
    U=len(sorted_list)
    K=(E+U) // 2
    while E<=U and sorted_list[K].hunts != 19 and sorted_list[K].private != False and sorted_list[K].colour != "zold":
        if sorted_list[K].hunts < 19:
            U=K-1
        else:
            E=K+1
        K=(E+U) // 2
    return (K, sorted_list[K])

traitor_id=binary_search_mandalorian(notprivatelist)
print("--------------------------------------------------")
print("traitor_id:")
print("index: ", traitor_id[0], " mandalorian: ", traitor_id[1].ertekek())