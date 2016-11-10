'Determine if there are any two elements in an array that sum to K'
def sum_k(array, k):
    map_of_array = {}
    for num in array:
        map_of_array[num] = None
    for i in range(len(array)):
        first_num = array[i]
        second_num = k - first_num
        if second_num in map_of_array:
            return True
    return False

def sum_k_faster(array, k):
    pointer_a = 0
    pointer_b = len(array) - 1
    while(pointer_a < pointer_b):
        sum_two = array[pointer_a] + array[pointer_b]
        if sum_two == k:
            return True
        if sum_two > k:
            pointer_b -= 1
        if sum_two < k:
            pointer_a += 1
    return False

a = list(map(int, input().strip().split(' ')))
k = int(input())
answer2 = sum_k_faster(a, k);
print(str(answer2))
