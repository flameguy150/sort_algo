import pygame
import random




def all_sorts():
    pass
def selection_sort(rectlist):
    global sort_complete
    n = len(rectlist)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            rectlist.highlight = (j, min_idx)
            if rectlist[j].height < rectlist[min_idx].height:
                min_idx = j
        rectlist.swap(rectlist[i], rectlist[min_idx])
        yield True
    rectlist.highlight = (-1, -1)   


def bubble_sort(rectlist):
    global bubble_i
    # global sort_complete
    n = len(rectlist)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            rectlist.highlight = (j, j+1)
            if rectlist[j].height > rectlist[j+1].height:
                rectlist.swap(rectlist[j], rectlist[j+1])
                swapped = True
                yield True
        if swapped == False:
            break
    rectlist.highlight = (-1, -1)        
    # n = len(rectlist)

    
    # sort_complete = True

def insertion_sort(rectlist):
    for i in range(1, len(rectlist)):
        key = rectlist[i]
        j = i-1
    
        while j >= 0 and key.height < rectlist[j].height:
            rectlist.highlight = (j, j+1)
            rectlist.swap(rectlist[j+1], rectlist[j])
            j -= 1
            yield True
        rectlist[j+1] = key
    rectlist.highlight = (-1,-1)

def merge(rectlist, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = rectlist[left + i]
    for j in range(n2):
        R[j] = rectlist[mid + 1 + j]

    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = left  # Initial index of merged subarray

    # Merge the temp arrays back
    # into arr[left..right]
    while i < n1 and j < n2:
        rectlist.highlight = (left + i, mid + 1 + j)
        if L[i].height <= R[j].height:
            rectlist.swap(rectlist[k], L[i])
            i += 1
        else:
            rectlist.swap(rectlist[k], R[j])
            j += 1
        k += 1
        yield True

    # Copy the remaining elements of L[],
    # if there are any
    while i < n1:
        rectlist.highlight = (left + i, left + i)
        rectlist.swap(rectlist[k], L[i])
        i += 1
        k += 1
        yield True

    # Copy the remaining elements of R[], 
    # if there are any
    while j < n2:
        rectlist.highlight = (mid + 1 + j, mid + 1 + j)
        rectlist.swap(rectlist[k], R[j])
        j += 1
        k += 1
        yield True
    rectlist.highlight = (-1, -1)

def merge_sort_(rectlist, left, right):
    if left < right:
        mid = (left + right) // 2

        yield from merge_sort_(rectlist, left, mid)
        # print("merging left side!")
        yield from merge_sort_(rectlist, mid + 1, right)
        # print("merging right side!")
        yield from merge(rectlist, left, mid, right)
        # print("merging final 2 sides!")

def merge_sort(rectlist):
    yield from merge_sort_(rectlist, 0, len(rectlist)-1)


