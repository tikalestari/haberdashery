# given an array of ints, consider a bar graph of width 1 and length of the ints in the array
# find the area of water level within the bars

def level(bars):
    level = 0
    for i in range(len(bars)):
        max_left = get_left_max(i, bars)
        max_right = get_right_max(i, bars)
        current_bar = bars[i]
        if current_bar < max_left and current_bar < max_right:
            level += min(max_left, max_right) - current_bar

    print(str(level))


def get_left_max(num, bars):
    max_left = 0
    for i in range(0, num):
        max_left = max(bars[i], max_left)
    return max_left

def get_right_max(num, bars):
    max_right = 0
    for i in range(num + 1, len(bars)):
        max_right = max(bars[i], max_right)
    return max_right

if __name__ == "__main__":
    level([1,3,2,4,1,3,2,4])
