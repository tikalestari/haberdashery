def fraud():
    t = int(input())
    for i in range(0,t):
        user_id = {}
        id_trans = {}
        trans = {}
        sort = []
        n,m = map(int,input().split())
        for i in range(0,n):
            a,b = input().split()
            user_id[b] = [a,0]
        for i in range(0,m):
            a,b = input().split()
            if a not in id_trans:
                id_trans[a] = [b]
            else:
                id_trans[a].append(b)
        for i in range(0,m):
            a,b = input().split()
            trans[a] = int(b.replace("$",""))
        for i in id_trans:
            for j in range(0, len(id_trans[i])):
                user_id[i][1] += trans[id_trans[i][j]]
        for key, value in user_id.items():
            if value[1] >= 100000:
                sort.append(value[0])

        sort = sorted(sort)
        if len(sort) > 0:
            for i in sort:
                print(i)
        else:
            print("NONE")

if __name__ == "__main__":
    fraud()
