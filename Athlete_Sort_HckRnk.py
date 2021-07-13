#!/bin/python3

import operator
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    # nm = input().split()

    # n = int(nm[0])

    # m = int(nm[1])

    arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]

    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    # k = int(input())

    k = 2



    def sort_table(arr, col=0):
        return sorted(arr, key=operator.itemgetter(col))


    
    for row in sort_table(arr, k):
        print(' '.join(str(i) for i in row))


