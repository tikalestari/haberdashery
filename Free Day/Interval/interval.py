def intervals():
    t = int(input())
    for i in range(t):
        n = int(input())
        interval_list = []
        for i in range(0,n):
            start, end = map(int,input().split())
            tup = (start, end)
            interval_list.append(tup)
        if len(interval_list) == 0:
            return 0
        ans = 0
        interval_list.sort()
        stack = [interval_list[0]]
        for interval in interval_list:
            temp = stack.pop()
            if temp[1] >= interval[0]:
                stack.append([temp[0], max(temp[1], interval[1])])
            else:
                stack.append(temp)
                stack.append(interval)
        for interval in stack:
            ans += int(interval[1]) - int(interval[0])
        print(ans)

if __name__ == '__main__':
    intervals()
