'''
Given a set of coin denominations
Like {1,5,10,25}
You can use any number of each coin
What is the minimum number of coins it takes to make K
'''
import sys

def coins(coin_set, index, coin_counter, k):
    if k == 0:
        return coin_counter

    if k < 0:
        return sys.maxsize

    if index == len(coin_set):
        return sys.maxsize

    return min(coins(coin_set,index+1,coin_counter+1,k-coin_set[index]), coins(coin_set,index,coin_counter+1,k-coin_set[index]), coins(coin_set,index+1,coin_counter,k))




c = [1,5,10,25]
print(coins(c,0,0,13))
