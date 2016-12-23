'''
reverse a string recursively
'''
def reverse(s, index):
    if index == len(s)-1:
        return s[index]
    result = reverse(s,index+1) + s[index]

    return result


s = "apple"
print(reverse(s,0))
