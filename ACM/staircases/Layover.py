#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    c,g = input().strip().split(' ')
    c,g = [int(c),int(g)]
    if c > g:
        print("LEFT")
    elif g > c:
        print("RIGHT")
