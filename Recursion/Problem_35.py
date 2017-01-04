'''
Knapsack Problem
You're given two lists and K
The first list contains the weights for all of the items
The second list contains the VALUE for the items, how much they are worth
Consider them to be items in a house or something that you want to steal
And your bag can only fit weight K, no more or the bag breaks
So you want to maximize the value you take
Where the weight of all the items you take is less than or equal to K
If you get confused, it's called the knapsack problem

Approach:
find all the combination of items that can fit in K
find the max of all those combinations
'''

def knapsack(prices, weights, index, value, k):
    if k == 0:
        return value
    if k < 0:
        return -1
    if index >= len(prices):
        return value

    #include
    return max(knapsack(prices,weights,index+1,value+prices[index],k-weights[index]), \
        #exclude
        knapsack(prices,weights,index+1,value,k))



p = [10,20,30,40,50]
w = [1,1,1,1,1]
k = 2
print(knapsack(p,w,0,0,k))
