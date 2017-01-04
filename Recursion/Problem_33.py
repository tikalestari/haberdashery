'''
Given a set of coin denominations
Like {1,5,10,25}
You can use any number of each coin
What is the minimum number of coins it takes to make K
'''
import sys

def coins(coin_set, index, k):
    if k == 0:
        return 0

    if k < 0:
        return sys.maxsize

    if index == len(coin_set):
        return sys.maxsize

    #include coin, move on to next index
    return min(1 + coins(coin_set,index+1,k-coin_set[index]), \
    #include coin, index stays
    1 + coins(coin_set,index,k-coin_set[index]), \
    #exclude coin
    coins(coin_set,index+1,k))




c = [1,5,10,25]
print(coins(c,0,100))
