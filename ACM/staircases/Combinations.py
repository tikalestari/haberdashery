def combo(n, memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n in memo:
        return memo[n]

    num_ways = 0

    #    slides combo
    for i in range(0, n):
        num_ways += combo(i,memo)

    #             one step          two step
    num_ways += combo(n-1,memo) + combo(n-2,memo)

    memo[n] = num_ways

    return num_ways
