def merge():
    array_1 = sorted(list(map(int, input().split())))
    array_2 = sorted(list(map(int, input().split())))
    ans = []
    i = 0
    j = 0

    while(i < len(array_1) or j < len(array_2)):
        if i >= len(array_1):
            while j < len(array_2):
                ans.append(array_2[j])
                j += 1
        elif j >= len(array_2):
            while i < len(array_1):
                ans.append(array_1[i])
                i += 1
        elif array_1[i] < array_2[j]:
            ans.append(array_1[i])
            i += 1
        elif array_1[i] > array_2[j]:
            ans.append(array_2[j])
            j += 1
        else:
            ans.append(array_1[i])
            ans.append(array_2[j])
            i += 1
            j += 1

    print(ans)

if __name__ == "__main__":
    merge()
