import numpy as np
import math

grid=np.array([
    [5,6,2,5,7,6],
    [7,7,1,9,4,3],
    [6,4,2,12,5,5],
    [3,3,1,7,6,5],
    [8,4,6,6,6,3],
    [5,8,2,1,4,4]
])

gridlen=len(grid)
 

def printarr(n):
    for i in range (0, n):
        for a in range (0, n):
            print(grid[i,a])


printarr(gridlen)