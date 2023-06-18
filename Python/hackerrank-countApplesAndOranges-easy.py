import math
import os
import random
import re
import sys
#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    ap_d = []
    or_d = []
    ap_count = 0 ; or_count = 0
    for i in apples:
        d = a + i
        ap_d.append(d)
    for j in range(0,n):
        d = b + oranges[j]
        or_d.append(d)
    for k in ap_d:
        if (k>=s and k<=t):
            ap_count+=1
    for k in or_d:
        if (k>=s and k<=t):
            or_count+=1
    print(ap_count)
    print(or_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)