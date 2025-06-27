#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_elements = set()
    total = 0
    for num in my_list:
        if num not in unique_elements:
            unique_elements.add(num)
            total += num
    return total
