def lottery():
    t = int(input())
    for i in range(0,t):
        a,b = map(int,input().split())
        names = {}
        count = {}
        flag = 0
        for i in range(0,a):
            first,last = input().split()
            names[last] = first
        for i in range(0,b):
            last = input()
            if last not in count:
                count[last] = 1
            else:
                count[last] += 1
        for l,c in count.items():
            if c == 1:
                flag = 1
                print(names[l],l)
        if not flag:
            print("NONE")

if __name__ == "__main__":
    lottery()
