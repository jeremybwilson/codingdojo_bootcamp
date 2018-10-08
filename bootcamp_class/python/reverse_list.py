# loop len(list) / 2 times

def reverse_list(list):
  # for i in range(len(list) / 2)
  for i in range(len(list) / 2):
    # swap values
    temp = list[len(list) - 1 - i]
    list[len(list) - 1 - i] = list[i]
    list[i] = temp
  return list


print reverse_list([1,2,3,4,5,6])