#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    am_pm = s[-2:]
    result = ''
    print (s[:-2])
    if am_pm == 'AM' and s[:2] == '12':
        result = "00" + s[2:-2]
    elif am_pm == 'AM':
        result = s[:-2]

    if am_pm == 'PM' and s[:2] == '12':
        result = s[:-2]
    elif am_pm == 'PM':
        hours = int(s[:2]) + 12
        result = str(hours) + s[2:-2]

    return result

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
