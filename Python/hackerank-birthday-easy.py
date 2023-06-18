import math
import os
import random
import re
import sys
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
def birthday(s, d, m):
    # Write your code here
    sum = c_bar = c_com = 0
    for i in range(len(s)):
        c_bar=1
        sum = s[i]
        for j in range(i+1,len(s)):
            if (c_bar==m):
                break
            sum+=s[j]
            c_bar+=1
        if(sum==d):
            c_com+=1       
    return c_com        

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    first_multiple_input = input().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result = birthday(s, d, m)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
