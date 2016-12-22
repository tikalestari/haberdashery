'''find the powerset of a set'''


# 1,2,3,4,5
# include 1, exclude 1
# index += 1
# include 2, exclude 2
# index += 1
# include 3, exclude 3
# ...
# [1,3,4]
# add current list to list of lists (i.e. add set to powerset)
def powerset(s,index,current_set,power_set):
    if index == len(s):
        power_set.append(list(current_set))
        print(current_set)
        return
    powerset(s, index+1, current_set, power_set)
    current_set.append(s[index])
    powerset(s, index+1, current_set, power_set)
    current_set.pop()


#s = Set([1,2,3])
s = [1,2,3]
p = []
powerset(s,0,[],p)
print(p)


'''
{{},{1},{2},{3},{1,2},{2,3},{1,3},{1,2,3}}
'''
