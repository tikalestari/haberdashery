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



if __name__ == "__main__":
    function()
