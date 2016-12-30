# Implement quick sort
import random
def quick_sort(lo,hi,array):
    if len(array) == 0:
        return array

    if lo == hi:
        single = []
        single.append(array[lo])
        return single

    pivot = lo

    left = []
    equal = []
    equal.append(array[pivot])
    right = []

    for i in range(lo+1,hi):
        if array[i] < array[pivot]:
            left.append(array[i])
        elif array[i] > array[pivot]:
            right.append(array[i])
        elif array[i] == array[pivot]:
            equal.append(array[i])

    return quick_sort(0,len(left),left) + equal + quick_sort(0,len(right),right)

def test_quick_sort(num_tests):
    for i in range(num_tests):
        array_len = random.randint(0,11)
        l = [0 for j in range(array_len)]
        for j in range(array_len):
            l[j] = random.randint(0,51)
        print("Original array: "+str(l))
        print("Sorted array:   "+str(quick_sort(0, len(l), l)))
        print("---------------------------")


test_quick_sort(3)
