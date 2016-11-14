def game():
    t = int(input())
    for i in range(t):
        n, m, k = map(int, input().split())
        cups = [i for i in range(n)]
        for i in range(m):
            command = input()
            if command == "REVERSE":
                cups.reverse()
            else:
                command, pos1, pos2 = command.split()
                temp = cups[int(pos1)]
                cups[int(pos1)] = cups[int(pos2)]
                cups[int(pos2)] = temp
        print(cups.index(int(k)))


if __name__ == "__main__":
    game()
