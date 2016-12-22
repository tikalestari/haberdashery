'''Given a set, return the number of subsets that sum to K'''

def subset_sum(s,k,index,current_set):
    if index == len(s):
        set_sum = 0
        for element in current_set:
            set_sum += element
        if set_sum == k:
            return 1
        else:
            return 0
    result = 0
    result += subset_sum(s,k,index+1,current_set)
    current_set.append(s[index])
    result += subset_sum(s,k,index+1,current_set)
    current_set.pop()

    return result

s = [1,2,3]
print(subset_sum(s,3,0,[]))
