from sorter import swap

""" 
sort by height

need to animate


"""

def selection_sort(rectlist):
    n = len(rectlist)
    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if rectlist[j] < rectlist[min_idx]:
                min_idx = j
        
        swap(rectlist[i], rectlist[min_idx])
        rectlist[i], rectlist[min_idx] = rectlist[min_idx], rectlist[i]