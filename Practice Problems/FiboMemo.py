def fibo(n, memo):
    if n not in memo():
        if n == 0:
            memo[n] = 0
        elif n == 1:
            memo[n] = 1
        else:
            memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
    return memo[n]
