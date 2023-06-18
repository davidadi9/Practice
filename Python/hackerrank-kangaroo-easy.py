import math
import os
import random
import re
import sys

# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    d1 = x1 ; d2 = x2
    flg = "NO"
    if ((x2>=x1 and v2>v1) or (x1>=x2 and v1>v2)):
        flg = "NO"
    else:
        if (d1<d2 and v1>v2):
            while(d1<d2):
                d1+=v1
                d2+=v2
        else:
            while(d2<d1 and v2>v1):
                d1+=v1
                d2+=v2
        if(d1==d2):
            flg = "YES"
    return flg
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    x1 = int(first_multiple_input[0])
    v1 = int(first_multiple_input[1])
    x2 = int(first_multiple_input[2])
    v2 = int(first_multiple_input[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()