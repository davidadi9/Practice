import math
import os
import random
import re
import sys
import tempfile
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
def getTotalX(a, b):
    # Write your code here
    min_num = min(a)
    max_num = min(b)
    temp = []
    count=0
    print(min_num,max_num)
    for i in range(min_num,max_num+1,min_num):
        for j in b:
            flg_apd=0
            if (j%i==0):
                for k in a:
                    if (i%k==0 and i/k>=1):
                        flg=1
                    else:
                        flg=0
                        break
                if (flg==1):
                    flg_apd=1
                    for x in temp:
                        if (x==i):
                            flg_apd=0
                            break            
            else:
                flg_apd=0
                break
        if (flg_apd==1):
                temp.append(i)
    
    print(temp)
    count=len(temp)
    return count
        
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    print(total)
    # fptr.write(str(total) + '\n')
    # fptr.close()