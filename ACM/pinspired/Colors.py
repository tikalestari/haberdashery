import math
def function():
    t = int(input())
    for i in range(t):
        n, c = input().split()
        n = int(n)
        order_list = []
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
            order_list.append((euc,color))
        sorted(order_list, key=lambda tup: tup[0])
        print("Case "+ str(c)+":")
        for n in order_list:
            print(n[1])

if __name__ == "__main__":
    function()
