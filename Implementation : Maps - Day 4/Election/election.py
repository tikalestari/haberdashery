def election():
    t = int(input())
    for i in range(0,t):
        letters = {}
        n = int(input())
        for i in range(0,n):
            a,b = input().split()
            if len(a) != len(b):
                print("NO")
            else:
                if check(a,b):
                    print("YES")
                else:
                    print("NO")

def check(a,b):
    letters_a = {}
    letters_b = {}
    for i in a:
        if i not in letters_a:
            letters_a[i] = 1
        else:
            letters_a[i] += 1
    for i in b:
        if i not in letters_b:
            letters_b[i] = 1
        else:
            letters_b[i] += 1
    return letters_a == letters_b

if __name__ == "__main__":
    election()
