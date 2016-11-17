# given an array of ints and index pairs, find sum of elements in each pair.
def sum_pair():
    nums = list(map(int, input().split()))
    n = int(input())
    prefix_sum = [nums[0]]
    j = 0
    for i in range(1,len(nums)):
        prefix_sum.append(nums[i] + prefix_sum[j])
        j += 1
    for i in range(n):
        a,b = map(int, input().split())
        if a == 0:
            print(prefix_sum[b])
        else:
            print(prefix_sum[b] - prefix_sum[a-1])


if __name__ == "__main__":
    sum_pair()
