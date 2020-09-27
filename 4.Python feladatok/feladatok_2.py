import numpy as np
from numpy import random as rnd

nplist1=np.arange(0,12)
nplist2=np.arange(12,30)
simalista=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

nemrendezett = rnd.randint(100, size=(20))
nemrendezett2 = nemrendezett

mergelist1 = rnd.randint(21, size=(10))
mergelist2 = rnd.randint(21, size=(10))

def linear_search(s_list, s_element):
  i=0
  temp=-1
  while (i<len(s_list)):
    if (s_list[i] == s_element):
      temp=i
      break
    i=i+1
  return temp

print("linkeres1: ", linear_search(nplist2, 20))

def linear_search_2(s_list, s_element):
    i=0
    while (i<len(s_list)) & (s_list[i] != s_element):
        i=i+1
    return (i, i < len(s_list))

print("linkeres2: ", linear_search_2(nplist1, 6))

def sentinel_linear_search(s_list, s_element):
    sentinel_list=s_list.copy()
    sentinel_list.append(s_element)
    i=0
    while ( sentinel_list[i] is not s_element):
        i=i+1
    return (i, i < len(s_list))

print("strázsás keres: ", sentinel_linear_search(simalista, 13))

def numpy_sentinel_linear_search(s_list, s_element):
    temp=np.append(s_list, s_element)
    i=0
    while (temp[i] != s_element):
        i=i+1
    return i, i < len(temp)-1   

print("numpy strázsás keres: ", numpy_sentinel_linear_search(nplist1, 15))

# // operator = floor division
def bin_search(sorted_list, item):
    E=0
    U=len(sorted_list)
    K=(E+U) // 2
    while E<=U and sorted_list[K] is not item:
        if item < sorted_list[K]:
            U=K-1
        else:
            E=K+1
        K=(E+U) // 2
    return (K, E<=U)

print("binkeres: ", bin_search(simalista, 10))

def binrendkeres(sor, szam):
  # k értéke -1, ha nincs benne a sorozatban, egyébként visszaadja a keresett elem indexét/helyét tárolja
  k = -1
  # g értéke a sorozat középső elemének indexét/helyét tárolja
  g = 0
  #megvizsgáljuk, hogy a sorozat hosszértéke páros-e, ha nem, akkor mást csinálunk
  if len(sor)%2 == 0:
    g = int(len(sor)/2)
    if sor[g] <= szam:
      for i in range (g, len(sor)):
        if sor[i] == szam:
          k = i
    elif sor[g] > szam:
      for i in range (g, 0, -1):
        if sor[i] == szam:
          k = i
  elif len(sor)%2 != 0:
    g = int((len(sor)-1)/2)
    if sor[g] <= szam:
      for i in range(g, len(sor)):
        if sor[i] == szam:
          k = i
    elif sor[g] > szam:
      for i in range (g, 0, -1):
        if sor[i] == szam:
          k = i
  return k

print("binkeres donó: ", binrendkeres(simalista, 6))

def selection_sort_elj(unsorted_list): 
  for i in range(len(unsorted_list)):
    min=i
    for j in range(i+1,len(unsorted_list)):
      if unsorted_list[j] < unsorted_list[min]:
        min=j
    if min is not i:
      temp=unsorted_list[min]
      unsorted_list[min]=unsorted_list[i]
      unsorted_list[i]=temp

selection_sort_elj(nemrendezett2)
print("nemrendezett2: ", nemrendezett2)

def selection_sort(unsorted_list):
  sajt = unsorted_list
  for i in range(len(sajt)):
    min=i
    for j in range(i+1,len(sajt)):
      if sajt[j] < sajt[min]:
        min=j
    if min is not i:
      temp=sajt[min]
      sajt[min]=sajt[i]
      sajt[i]=temp
  return sajt

print("rendezett: ", selection_sort(nemrendezett))

def selection_sort2(unsorted_list): 
  sorted_list=unsorted_list.copy()
  for i in range(len(sorted_list)):
    min=i
    for j in range(i+1,len(sorted_list)):
      if sorted_list[j] < sorted_list[min]:
        min=j
    if min is not i:
        sorted_list[min], sorted_list[i] = sorted_list[i], sorted_list[min]
  return sorted_list

print("rendezett: ", selection_sort2(nemrendezett))

def bubble_sort(arr):
  j=0
  while (j < len(arr)-1):
    lastSwap=0
    for i in range(0, len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        lastSwap=i
    j=len(arr)-lastSwap
  return arr

print("bubi: ", bubble_sort(nemrendezett))

def insertion_sort(arr):
  for j in range(len(arr)):
    cursor=arr[j]
    pos=j
    while pos>0 and cursor < arr[pos-1]:
      arr[pos] = arr[pos-1]
      pos= pos-1
    arr[pos]=cursor
  return arr

print("beszúró: ", insertion_sort(nemrendezett))

def shell_sort(arr):
  D=len(arr) // 2
  while D>0:
    for i in range(D, len(arr)):
      j=i
      while j>=D and arr[j-D] > arr[i]:
        print(j)
        arr[j-D],  arr[i] = arr[i], arr[j-D]
        j=j-D
    D=D//2
  return arr

print("shell: ", shell_sort(nemrendezett))

def merge(arr1, arr2):
  arr3=[0] * (len(arr1)+len(arr2))
  i = j = 0
  k=-1
  while i < len(arr1) and j <len(arr2):
    k=k+1
    if arr1[i] < arr2[j]:
      arr3[k]=arr1[i]
      i=i+1
    elif arr1[i] > arr2[j]:
      arr3[k]=arr2[j]
      j=j+1
    else:
      arr3[k]=arr1[i]
      i=i+1
      k=k+1
      arr3[k]=arr2[j]
      j=j+1
  while i < len(arr1):
    k=k+1
    arr3[k]=arr1[i]
    i=i+1
  while j <len(arr2):
    k=k+1
    arr3[k]=arr2[j]
    j=j+1
  return arr3

print("merge: ", merge(mergelist1, mergelist2), " len: ", len(merge(mergelist1, mergelist2)))
print("mergelist1: ", mergelist1)
print("mergelist2: ", mergelist2)