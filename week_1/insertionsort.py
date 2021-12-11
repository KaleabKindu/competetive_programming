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
    for i in range(-1,n):
        num=arr[-1]
        for j in range(n-1,-1,-1):
            if arr[j] > num:
                arr[j+1]=arr[j]
                print(' '.join(str(k) for k in arr))
                arr[j]=num
    print(' '.join(str(k) for k in arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
