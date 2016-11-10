'Determine if there are any two elements in an array that sum to K'
def sum_k(array, k):
    flag = False
    map_of_array = {}
    for num in array:
        map_of_array[num] = None
    for i in range(len(array)):
        first_num = array[i]
        second_num = k - first_num
        if second_num in map_of_array:
            flag = True
    return flag

a = list(map(int, input().strip().split(' ')))
k = int(input())
answer = sum_k(a, k);
print(str(answer))
