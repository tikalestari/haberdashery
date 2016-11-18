# given an array of ints, consider a bar graph of width 1 and length of the ints in the array
# find the area of water level within the bars

def level(bars):
    level = 0
    max_left = [0 for i in range(len(bars))]
    max_right = [0 for i in range(len(bars))]
    for i in range(1, len(bars)):
        right_index = len(bars) - i - 1
        max_left[i] = max(max_left[i-1], bars[i-1])
        max_right[right_index] = max(max_right[right_index + 1], bars[right_index + 1])

    for i in range(len(bars)):
        current_bar = bars[i]
        if current_bar < max_left[i] and current_bar < max_right[i]:
            level += min(max_left[i], max_right[i]) - current_bar

    print(str(level))


if __name__ == "__main__":
    level([1,3,2,4,1,3,2,4])
