def overweight():
    t = int(input())
    for i in range(0,t):
        count = 0
        a,b,c = map(int, input().split())
        cats = {}
        for i in range(0,b):
            d,e = map(int, input().split())
            if d not in cats:
                cats[d] = e
            else:
                cats[d] += e
        for cat, weight in cats.items():
            if weight >= c:
                count += 1
        print(count)

if __name__ == "__main__":
    overweight()
