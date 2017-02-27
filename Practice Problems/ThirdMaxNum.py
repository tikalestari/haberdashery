'''Given a non-empty array of integers,
return the third maximum number in this array.
If it does not exist, return the maximum number.
The time complexity must be in O(n).
'''
import sys
def third_max(l):
    sorted_list = sorted(l)
    index = len(sorted_list) - 1
    counter = 1
    current_max = sorted_list[index]

    if len(sorted_list) < 3:
        return current_max

    while index >= 0 and counter < 3:
        if sorted_list[index] < current_max:
            current_max = sorted_list[index]
            counter += 1
        else:
            index -= 1

    return current_max








print(third_max([3,2,1]))
print(third_max([1,2]))
print(third_max([2,2,3,1]))
