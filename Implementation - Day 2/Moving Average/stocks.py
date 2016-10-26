def stocks():
    t = int(input())
    for i in range(0,t): 
        print("Test " + str(i+1) + ":")
        l = list(map(int, input().split()))
        s = 0
        d = 1
        for i in l:
            s += i
            print("Day " + str(d) + ":", str(s//d))
            d += 1

if __name__ == "__main__":
    stocks()
