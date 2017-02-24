import sys


t = int(input().strip())
for a0 in range(t):
    x,y = map(int, input().split(' '))
    e = int(input().strip())
    min_dist = sys.maxsize
    min_coor = (0,0)
    ans = (0,0)
    if e > 0:
        for a1 in range(e):
            eX,eY = map(int,input().split(' '))
            dist = abs(x-eX)+abs(y-eY)
            if dist < min_dist:
                ans = (eX,eY)
                min_dist = dist

    print("("+str(ans[0])+","+str(ans[1])+")")
