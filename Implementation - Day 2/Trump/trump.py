def trump():
    t = int(input())
    for i in range(0,t):
        a, b = map(int, input().split())
        rev = map(int, input().split())
        sum = 0
        for i in rev:
            sum += i
        if int(sum) >= a and int(sum) <= b:
            print ("YES")
        else:
            print ("NO")


if __name__ == "__main__":
    trump()
