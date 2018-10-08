def reverse_list(list):
    # loop len(list) / 2 times
    for i in range(len(list) / 2):
        #swap values

        temp = list[len(list) - 1 - i]
        list[len(list) - 1 - i] = list[i]
        list[i] = temp
    return list

print reverse_list([10,9,8,7,6,5,4,3,2,1])