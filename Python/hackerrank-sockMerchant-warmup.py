import math
import os
import random
import re
import sys
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#
def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def sockMerchant(n, ar):
    # Write your code here
    clr_num = []
    pair = 0
    count=0

    for i in ar:
        if search(clr_num,i):
            continue
        else:
            count = ar.count(i)
            pair += int(count/2)
            count=0
            clr_num.append(i)
    return pair

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = print(sockMerchant(n, ar))
    # fptr.write(str(result) + '\n')
    # fptr.close()