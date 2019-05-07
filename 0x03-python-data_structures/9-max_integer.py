def max_integer(my_list=[]):
    if my_list is None:
        return
    max = my_list[0]

    for num in my_list:
        if (max < num):
            max = num
    return max

