def trump():
    t = int(input())
    for i in range(0,t):
        a, b = map(int, input().split())
        rev = map(int, input().split())
        s = 0
        for i in rev:
            s += i
        if a <= s <= b:
            print ("YES")
        else:
            print ("NO")


if __name__ == "__main__":
    trump()
