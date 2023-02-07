#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count = 0 #in a plain
    valley_count = 0
    prev = 0
    flag = False
    
    for i in path:
        if i == "D":
            count -= 1
            if flag:
                if count == 0 and prev < 0:
                    valley_count += 1
       
        elif i == "U":
            count += 1
            if flag:
                if count == 0 and prev < 0:
                    valley_count += 1
        

        prev = count
        flag = True

    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
