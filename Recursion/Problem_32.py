'''
Max sum subarray
'''

def max_sub(array, left, right):
    if left > right:
        return 0

    if left == len(array) or right == len(array):
        return sum(array[left:right])

    return max(sum(array[left:right]), max_sub(array,left+1,right), max_sub(array,left,right+1) )



a = [1,2,3,4,-3]
print(max_sub(a,0,0))
