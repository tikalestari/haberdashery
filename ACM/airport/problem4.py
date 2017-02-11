def function():
    t = int(input())
    for i in range(t):
        n = int(input())
        list_1 = []
        list_2 = []
        f = False
        for j in range(n):
            code = input()
            list_1.append(code)
        m = int(input())
        for k in range(m):
            code = input()
            list_2.append(code)
        list_1.sort()
        list_2.sort()
        for code in list_1:
            if code in list_2:
                print(code)
        for code in list_2:
            if code not in list_1:
                print(code)



if __name__ == "__main__":
    function()
