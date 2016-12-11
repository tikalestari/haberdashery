'''
Given an array return T if there is a subset of the array
that sums to K, return F otherwise
array, index, K
subtract from K
'''

def subset_sum(array, k, index):
    if k == 0:
        return True

    if index == len(array):
        return False

    if subset_sum(array, k - array[index], index + 1):
        return True

    if subset_sum(array, k, index + 1):
        return True

    return False
