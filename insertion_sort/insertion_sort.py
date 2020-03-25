#!/usr/bin/env python3
'''
My try to implement insertion sort in Python
'''

def insertion_sort(lst):
    # lst is a list of integer
    
    for i in range(1, len(lst)):
        for j in reversed(range(1,i+1)):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break

    return lst

