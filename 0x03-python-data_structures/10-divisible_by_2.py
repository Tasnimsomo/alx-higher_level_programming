#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for i, j in enumerate(my_list):
        if j % 2 == 0:
            return True
        else:
            return False
