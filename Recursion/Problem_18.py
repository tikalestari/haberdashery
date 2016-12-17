''' given N stairs, the person on the ground
can either step 1 stair or 2 stairs at a time, or a mix of both
count the number of ways to reach the nth stair.
'''

def stair(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stair(n-1) + stair(n-2)

print(stair(3))
