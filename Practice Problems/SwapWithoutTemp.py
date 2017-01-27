'''
Given two variables x and y, swap the variables without
using a temp variable
'''

def swap_1(x,y):
    x = x ^ y
    y = x ^ y
    x = x ^ y
    print("swapped_1  x = "+ str(x))
    print("swapped_1  y = "+ str(y))

def swap_2(x,y):
    x = x + y
    y = x - y
    x = x - y
    print("swapped_2  x = "+ str(x))
    print("swapped_2  y = "+ str(y))



x = 66
y = 55
print("original   x = "+ str(x))
print("original   y = "+ str(y))
swap_1(x,y)
swap_2(x,y)
