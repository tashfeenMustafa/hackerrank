#!/bin/python3

import os
import sys

#
# Complete the dynamicArray function below.
#
def dynamicArray(n, queries):
    #
    # Write your code here.
    #
    s = [[] for x in range(n)]
    lastAnswer = 0
    res = []
    for i in range(len(queries)):
        query = queries[i][0]
        x = queries[i][1]
        y = queries[i][2]
        if query == 1:
            # do this
            s[((x ^ lastAnswer) % n)].append(y)
        elif query == 2:
            # do this
            size = len(s[((x ^ lastAnswer) % n)])
            lastAnswer = s[((x ^ lastAnswer) % n)][y % size]
            print (lastAnswer)
            res.append(lastAnswer)

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
