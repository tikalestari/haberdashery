def stocks():
    t = int(input())
    for i in range(0,t): #iterate through input
        print("Test " + str(i+1) + ":")
        l = list(map(int, input().split()))
        s = 0
        d = 1
        for i in l:
            s += i
            print("Day " + str(d) + ":", str(s//d))
            d += 1

        #for i in l:
        #    d = 1
        #    print("Day " + str(d) + ": ", end="")
        #    s = 0
        #    for j in range(0, d):
        #        s += l[j]
        #    print(s // i)
        #    d += 1



if __name__ == "__main__":
    stocks()
