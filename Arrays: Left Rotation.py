import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    temp=a
    for i in range(d):
        var = temp[0]
        temp.remove(var)
        temp.append(var)
    return temp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
