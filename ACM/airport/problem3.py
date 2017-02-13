def function():
    t = int(input())
    for i in range(t):
        n = int(input())
        num = 0
        hours = 0
        for j in range(n):
            a, b = map(int, input().split())
            num += (a * b)
            hours += b
        print(int(round(num/hours)))


if __name__ == "__main__":
    function()
