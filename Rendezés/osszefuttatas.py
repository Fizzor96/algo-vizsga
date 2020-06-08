sorozat1 = [3, 5, 9, 10, 13, 11, 12]
sorozat2 = [2, 1, 4, 8, 15, 7, 6, 14]

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

print(merge(sorozat1, sorozat2))