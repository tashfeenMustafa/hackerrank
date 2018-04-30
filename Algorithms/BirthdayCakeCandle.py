#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    #
    # Write your code here.
    #
    candles = sorted (ar)
    count = 0
    diffBetweenTallestCandleAndAge = n - candles[-1]
    for i in range(len(candles)):
        if n - candles[i] == diffBetweenTallestCandleAndAge:
            count += 1
    return count

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
