# Implement merge sort
'''
[1,4,3,2,5,6]
[1,4,3]    |    [2,5,6]
[1,4] [3]  |    [2,5] [6]
[1] [4]    |    [2] [5]

'''
import random

def merge_sort(lo,hi,array):
    if len(array) == 0:
        return array

    if lo == hi:
        single = []
        single.append(array[lo])
        return single

    mid = int((hi+lo)/2)
    left = merge_sort(lo,mid,array)
    right = merge_sort(mid+1,hi,array)

    return merge(left,right)


def merge(left,right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        while i < len(left):
            result.append(left[i])
            i += 1

    else:
        if j < len(right):
            while j < len(right):
                result.append(right[j])
                j += 1

    return result


def test_merge_sort(num_tests):
    for i in range(num_tests):
        array_len = random.randint(0,11)
        l = [0 for j in range(array_len)]
        for j in range(array_len):
            l[j] = random.randint(0,51)
        print("Original array: "+str(l))
        print("Sorted array: "+str(merge_sort(0, len(l)-1, l)))
        print("---------------------------")


test_merge_sort(3)
