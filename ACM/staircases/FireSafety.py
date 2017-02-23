#!/usr/bin/python
import sys

s, t = map(int, input().strip().split(' '))
ans = []
total = 0
nums = [int(x) for x in input().split(' ')]
for i in nums:
    people = int(t/i)
    ans.append(people)
    total += people

print(total)
for i in ans:
    print(i, end=" ")

print()
