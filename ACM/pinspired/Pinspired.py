def puns():
    not_pun_words = {"pin", "pins", "pinned", "pinning", "pinner", "pinners"}
    t = int(input())
    for i in range(t):
        count = 0
        sentence = input().lower().split()
        for word in sentence:
            if word not in not_pun_words and "pin" in word:
                count += 1
        print(str(count))


if __name__ == "__main__":
    puns()
