import math
import os
import random
import re
import sys
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    # Write your code here
    c_max = c_min = 0
    min_max_rec = []
    for i in range(len(scores)):
        temp = scores[i]
        if (i==0):
            min = temp
            max = temp
        else:
            if (temp>max):
                c_max+=1
                max = temp
            elif (temp<min):
                c_min+=1
                min = temp
    min_max_rec.append(c_max)
    min_max_rec.append(c_min)
    return min_max_rec

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))
    result = breakingRecords(scores)
    for j in result:
        print(j,end=" ")
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()