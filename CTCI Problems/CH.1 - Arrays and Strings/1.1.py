'''Implement an algorithm to determine if a string has all
unique characters. What if you can't use additional
data structures?'''

def unique_1(s):
    check = 0
    for i in s:
        val = ord(i) - ord('a')
        if check & (1 << val) > 0:
            return False
        else:
            check |= (1 << val)
    return True

if __name__ == '__main__':
    while True:
        print(unique_1(input()))
