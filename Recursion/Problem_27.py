'''
40. Combination Sum II
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

def combination(numbers,index,current,combos,target):
    if target == 0:
        current_copy = sorted(list(current))
        if current_copy not in combos:
            combos.append(current_copy)
        return

    if index == len(numbers):
        return

    combination(numbers,index+1,current,combos,target)
    num = numbers[index]
    current.append(num)
    combination(numbers,index+1,current,combos,target-num)
    current.pop()

n = [10,1,2,7,6,1,5]
t = 8
combos = []
combination(n,0,[],combos,t)
print(combos)
