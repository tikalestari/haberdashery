def search():
    t = int(input())
    for i in range(0,t):
        n,m = map(int,input().split())
        letter_to_count_to_web = {}
        count_to_web = {}
        web_to_count = {}
        for i in range(0,n):
            site = input()
            info_line = input().split()
            for i in info_line:
                if i not in letter_to_count_to_web:
                    letter_to_count_to_web[i] = {}
                if site not in letter_to_count_to_web[i]:
                    letter_to_count_to_web[i][site] = 1
                else:
                    letter_to_count_to_web[i][site] += 1


        for i in range(0,m):
            q = input()
            if q not in letter_to_count_to_web:
                print("NONE")
            else:
                sort = sorted(letter_to_count_to_web[q], key=letter_to_count_to_web[q].get, reverse=True) #sort by value
                for i in range(0,len(sort)):
                    print(str(i+1) + ". " + sort[i])

''' map=
    a,
    ['google.com', 2],
    ['tika.com', 3],
    ['whale.com', 2],
    ['cameron.com', 0],
    ['chicken.com', 4]

    b,
    [2, 'google.com'],
    [3, 'tika.com'],
    [2, 'whale.com'],
    [0, 'cameron.com'],
    [4, 'chicken.com']

    map = {}
    map['a'] = {}
    map['a'][website] = 0

    map[website]['a'] = 0
'''


if __name__ == "__main__":
    search()