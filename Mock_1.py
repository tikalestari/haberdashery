def add_one(number_list):
    index = len(number_list)-1
    while index >= 0:
        if number_list[index] == 9:
            number_list[index] = 0
            index -= 1
        else:
            number_list[index] += 1
            break

    if number_list[0] == 0:
        return [1] + number_list

    return number_list
 
