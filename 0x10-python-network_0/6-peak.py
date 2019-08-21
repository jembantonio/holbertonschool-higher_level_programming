#!/usr/bin/python3
''' Find the peak element
'''


def peak_binary(arr, low, hi):
    # if array is empty
    if low == hi:
        return arr[low]

    # find index of middle element
    mid = low + (hi - low) // 2
    # compare middle element with right elements
    if arr[mid] > arr[mid + 1]:
        return peak_binary(arr, low, mid)
    return peak_binary(arr, mid + 1, hi)


def find_peak(arr):
    if arr:
        return peak_binary(arr, 0, len(arr) - 1)
