'''
Return true if you can partition the array into two subsets that have equal sum
[1,12,14,3,2] returns true
Because 1+12+3 = 16 and 14+2 = 16
'''

def partition(array, index, part_1, part_2):
    if index == len(array):
        print(part_1)
        print(part_2)
        print()
        if sum(part_1) == sum(part_2):
            print(part_1)
            print(part_2)
            print("found equal")
            return True
        else:
            return False



    part_1.append(array[index])
    if partition(array,index+1,part_1,part_2):
        return True
    part_1.pop()


    part_2.append(array[index])
    if partition(array,index+1,part_1,part_2):
        return True
    part_2.pop()

    return False




a = [1,12,14,3,2] # true
b = [1,3,5,7,1] # false
c = [1,2,3] # true
print(partition(b,0,[],[]))
