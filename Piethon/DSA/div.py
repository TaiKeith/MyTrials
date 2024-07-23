def divisible_by_2(my_list):
    if len(my_list) == 0:
        return None

    new_list = []
    for x in new_list:
        if x % 2 == 0:
            new_list.append(True)
        new_list.append(False)
    return new_list

new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(divisible_by_2(new_list))
