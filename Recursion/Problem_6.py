# given n and k, press red -1, blue x2, find min number of button clicks
# it takes to get to k
# n = 12, k = 18
#


def button(n,k):
    if n == k:
        return 1
    if n > k:
        return 1 + button(n-1,k)
    if n < (k/2):
        return 1 + button(n*2,k)
    return 1 + min(button(n-1,k), button(n*2,k))


if __name__ == "__main__":
    while True:
        print(button(int(input()),int(input())))
