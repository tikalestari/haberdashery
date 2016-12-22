'''find the powerset of a set'''

def powerset(s,index,current_set,power_set):
    if index == len(s):
        power_set.append(list(current_set))
        print(current_set)
        return
    powerset(s, index+1, current_set, power_set)
    current_set.append(s[index])
    powerset(s, index+1, current_set, power_set)
    current_set.pop()

s = [1,2,3]
p = []
powerset(s,0,[],p)
print(p)
