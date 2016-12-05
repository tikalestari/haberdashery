'''Given a list of songs (a playlist), play each of the songs (print them).
However, when selecting which song to play, you must do it randomly and not
select the same song twice. When you have played every song, you are done.'''
from random import randint

def shuffle(array):
    count = len(array) - 1
    while count >= 0:
        random_index = randint(0, count)
        print(array[random_index])
        last_element = array[count]
        random_element = array[random_index]
        array[random_index] = last_element
        array[count] = random_element
        count -= 1

    print("\nDone")

if __name__ == "__main__":
    shuffle(["Hey", "My", "Name", "Is", "Tika"])
