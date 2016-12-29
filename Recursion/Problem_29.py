'''
Print all non-increasing sequences of sum equal to a given number x
Given a number x, print all possible non-increasing sequences with sum equals to x.

Examples:

Input: x = 3
Output: 1 1 1
        2 1
        3

Input: x = 4
Output: 1 1 1 1
        2 1 1
        2 2
        3 1
        4
'''

def sequences(x, seq):
    if x == 0:
        print(seq[1:])
        return

    for i in range(1,x+1):
        sequences(x-i,seq+" "+str(i))


sequences(4,"")
