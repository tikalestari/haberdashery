'''
We have a number of bunnies and each bunny has two big floppy ears.
We want to compute the total number of ears across all the bunnies recursively
(without loops or multiplication).

bunnyEars(0) → 0
bunnyEars(1) → 2
bunnyEars(2) → 4
'''

def bunnies(n):
    if n == 0:
        return 0
    return 2 + bunnies(n - 1)

if __name__ == "__main__":
    while True:
        print(bunnies(int(input())))
