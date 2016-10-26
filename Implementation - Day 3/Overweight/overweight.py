def overweight():
    t = int(input())
    for i in range(0,t):
        count = 0
        a,b,c = map(int, input().split())
        new_list = [0 for i in range(a)]
        for i in range(0,b):
            d,e = map(int, input().split())
            new_list[d] += e
        for j in new_list:
            if int(j) >= c:
                count += 1
        print(count)

if __name__ == "__main__":
    overweight()
