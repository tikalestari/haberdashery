'Print the max 3 items in a list in one pass'
def max_three(l):
    first = l[0]
    second = l[1]
    third = l[2]
    for i in range(3,len(l)):
        if l[i] > first:
            if second < first:
                if third < second:
                    third = second
                second = first
            first = l[i]
        else:
            if l[i] > second:
                third = second
                second = l[i]
            else:
                if l[i] > third:
                    third = l[i]

    return str(first) + " " + str(second) + " " + str(third)


l = list(map(int, input().strip().split(' ')))
answer = max_three(l);
print(answer)
