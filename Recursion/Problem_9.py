'''
We have bunnies standing in a line, numbered 1, 2, ...
The odd bunnies (1, 3, ..) have the normal 2 ears.
The even bunnies (2, 4, ..) we'll say have 3 ears,
because they each have a raised foot.
Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

bunnyEars2(0) → 0
bunnyEars2(1) → 2
bunnyEars2(2) → 5
'''


def bunnies(n):
    if n == 0:
        return 0
    elif n % 2 == 1:
        return 2 + bunnies(n - 1)
    else:
        return 3 + bunnies(n - 1)

if __name__ == "__main__":
    while True:
        print(bunnies(int(input())))
