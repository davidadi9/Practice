import math
import os
import random
import re
import sys
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def timeConversion(s):
    # Write your code here
    for i in range(len(s)):
        if (s[i]==":"):
            hour=int(s[:i])
            time_str=s[i:]
            break
    print(hour)
    if "PM" in s:
        if (hour<12):
            hour+=12
    elif "AM" in s:
        if (hour==12):
            hour=0
    time_str=str("%.2d"%hour)+time_str.replace("AM","").replace("PM","")
    return time_str

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = print(timeConversion(s))
    # fptr.write(result + '\n')
    # fptr.close()