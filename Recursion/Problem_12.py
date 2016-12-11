'''Given an array, return true if two elements sum to k.'''

def two_sum(array, k, index, elements_used):
    if elements_used == 2 and k == 0:
        return True

    if index == len(array):
        return False

    if elements_used == 2:
        return False

    if two_sum(array, k - array[index], index + 1, elements_used + 1):
        return True

    if two_sum(array, k, index + 1, elements_used):
        return True

    return False

print(two_sum([1,2,3,4], 4, 0, 0))
