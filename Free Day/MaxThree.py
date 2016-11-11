'Print the max 3 items in a list in one pass. Only positive numbers.'
def max_three(l):
    first = -1
    second = -1
    third = -1
    for i in range(len(l)):
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
