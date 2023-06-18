import math
import os
import random
import re
import sys
import itertools as it
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#hackerrank-min_max_sum-easy

def miniMaxSum(arr):
    # Write your code here
    # lists = [[]]
    # for i in range(len(arr) + 1):
    #     for j in range(i):
    #         lists.append(arr[j: i])
    # BELOM BISA PAKE LOGIC MANUAL, BRU PK LIBRARY
    the_list = list(it.combinations(arr,4))
    sum_list = []
    for x in the_list:
        sum_list.append(sum(x))    
    print(min(sum_list),max(sum_list))

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)