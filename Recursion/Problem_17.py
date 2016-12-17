'''
Binary search
Return true if value is in array
Divide the array into halves
Hint: the half is nothing when low >= high
'''

def search(array, value, low, high):
    if low >= high:
        return False
    mid = int((low+high)/2)
    if value == array[mid]:
        return True
    elif value < array[mid]:
        return search(array, value, low, mid-1)
    else:
        return search(array, value, mid+1, high)



a = [1,2,3,4,5,6,7,12,14,15,16,17,18,25,26,27,28,47,49,52,54,58,67,76,87,99]
print(search(a,14,0,len(a)-1))
