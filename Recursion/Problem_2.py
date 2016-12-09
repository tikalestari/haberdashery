# compute the nth fibonnaci number
# 1 1 2 3 5 8 13
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    while True:
        print(fib(int(input())))
