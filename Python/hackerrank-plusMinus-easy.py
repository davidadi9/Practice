import math
import os
import random
import re
import sys
#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    pos = 0 ; neg = 0 ; zer = 0
    for x in arr:
        if x < 0:
            neg+=1
        elif x == 0:
            zer +=1
        else:
            pos+=1
    pos_ratio = pos/len(arr)
    neg_ratio = neg/len(arr)
    zer_ratio = zer/len(arr)

    print("%.6f"%pos_ratio)
    print("%.6f"%neg_ratio)
    print("%.6f"%zer_ratio)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)