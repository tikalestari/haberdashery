def search():
    t = int(input())
    for i in range(0,t):
        n,m = map(int,input().split())
        letter_map = {}
        for i in range(0,n):
            site = input()
            info_line = input().split()
            for i in info_line:
                if i not in letter_map:
                    letter_map[i] = {}
                if site not in letter_map[i]:
                    letter_map[i][site] = 1
                else:
                    letter_map[i][site] += 1

        for i in range(0,m):
            q = input()
            if q not in letter_map:
                print("NONE")
            else:
                sort = sorted(letter_map[q], key=letter_map[q].get, reverse=True) #sort by value
                for i in range(0,len(sort)):
                    print(str(i+1) + ". " + sort[i])

if __name__ == "__main__":
    search()
