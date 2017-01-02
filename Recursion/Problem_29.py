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

def sequences_helper(x, prev, seq):
    if x == 0:
        print(seq[1:])
        return

    for i in range(1,x+1):
        if seq == "":
            sequences_helper(x-i,i,seq+" "+str(i))
        if i <= prev:
            sequences_helper(x-i,i,seq+" "+str(i))

def sequences(x):
    sequences_helper(x,0,"")

if __name__ == "__main__":
    while True:
        sequences(int(input()))
