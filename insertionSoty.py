#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    aux = []
    j = 0
    for i in range(n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and aux < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            print(*arr)
        arr[j+1] = aux
    print(*arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
