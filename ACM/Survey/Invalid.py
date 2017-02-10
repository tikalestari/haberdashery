def invalid():
    t = int(input())
    for i in range(t):
        n = int(input())
        count = 0
        for j in range(n):
            invalid = False
            h, w = map(int, input().split())
            if h < 6 or h > 21:
                invalid = True
            if w < 0 or w > 1024:
                invalid = True
            if invalid:
                count += 1

    print(count)


if __name__ == "__main__":
    invalid()
