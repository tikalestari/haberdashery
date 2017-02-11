#Flight Numbers

def function():
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = input().split()
        bin_nums = []
        for n in nums:
            bin_nums.append("{0:b}".format(int(n)))
        count = 0
        for bn in bin_nums:
            it = int(bn[0])
            for k in range(1,len(bn)):
                it ^= int(bn[k])
            if it == 1:
                count += 1

        print(count)





if __name__ == "__main__":
    function()
