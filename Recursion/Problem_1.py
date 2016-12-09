# given a number n, count the number of numbers between 0 and n,
# inclusive, that are divisible by k. given n and k

'''for i in range(n + 1):
  if i % k == 0:
    count += 1'''

def count(n, k):
    if n < 0:
        return 0
    if n % k == 0:
        return 1 + count(n - 1, k)
    else:
        return count(n-1,k)
