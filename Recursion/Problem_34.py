'''
Return the list of lists that represent the coin combinations
That sum to K
'''
import sys

def coin_combos(coin_set, coin_lists, current_combo, index, k):
    if k == 0:
        current_sorted = sorted(list(current_combo))
        if current_sorted not in coin_lists:
            coin_lists.append(current_sorted)
        return

    if k < 0:
        return

    if index >= len(coin_set):
        return

    #exclude
    coin_combos(coin_set, coin_lists, current_combo, index+1, k)

    #include, index
    current_combo.append(coin_set[index])
    coin_combos(coin_set, coin_lists, current_combo, index, k-coin_set[index])

    #include, index + 1
    coin_combos(coin_set, coin_lists, current_combo, index+1, k-coin_set[index])
    current_combo.pop()

    return

coin_lists = []
c = [1,5,10,25]
coin_combos(c,coin_lists,[],0,10)
print(coin_lists)
