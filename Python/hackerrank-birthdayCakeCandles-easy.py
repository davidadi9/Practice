import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    count=0
    max = candles[0]
    for x in candles:
        if (x>max):
            max = x
        elif (x==max):
            count+=1
    if count==0:
        count+=1
    return count
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = print(birthdayCakeCandles(candles))

    # fptr.write(str(result) + '\n')

    # fptr.close()