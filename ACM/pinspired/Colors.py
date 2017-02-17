import math
def function():
    t = int(input())
    for i in range(t):
        n, c = input().split()
        n = int(n)
        order_list = {}
        query = c[1:]
        r_q = int(query[0:2], 16)
        g_q = int(query[2:4], 16)
        b_q = int(query[4:6], 16)
        for j in range(n):
            color = input()
            r_c = int(color[1:3], 16)
            g_c = int(color[3:5], 16)
            b_c = int(color[5:7], 16)
            euc = math.sqrt(math.pow(r_q - r_c,2)+math.pow(g_q - g_c,2)+math.pow(b_q - b_c,2))
            if euc in order_list:
                order_list[euc].append(color)
            else:
                order_list[euc] = [color]
        sorted_list = sorted(order_list.items())
        print("Case "+ str(c)+":")
        for tup in sorted_list:
            if len(tup[1]) > 1:
                tup[1].sort()
            for item in tup[1]:
                print(item)

if __name__ == "__main__":
    function()
