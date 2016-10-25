def basics():
    test_num = int(input())
    for i in range(0,test_num-1):
        k = int(input())
        print(str(len(input().split()) - k) + " ", end="")
    k = int(input())
    print(str(len(input().split()) - k))

if __name__ == "__main__":
    basics()
