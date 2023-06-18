import math
import os
import random
import re
import sys
#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
def gradingStudents(grades):
    # Write your code here
    rounded_grades = []
    for i in grades:
        scr = i
        if (scr%5>=3):
            scr=scr+5-scr%5
            if (scr<40):
                scr = i
        rounded_grades.append(scr)
    return rounded_grades

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = print(gradingStudents(grades))
    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    # fptr.close()