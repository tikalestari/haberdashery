t = int(input())

for i in range(t):
    dims = [int(elem) for elem in input().split()]
    print(dims[0] * dims[1] * (12 * dims[2]) * ((dims[3] * (dims[3] + 1)) // 2 ))
