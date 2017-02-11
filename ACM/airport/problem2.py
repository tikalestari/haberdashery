def function():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        inp = input()
        nums = inp.split()
        nums.sort()
        l = n-m
        ans = 0
        for j in range(l):
            ans += int(nums[j])

        print(ans)



if __name__ == "__main__":
    function()
