#Selection Sort
#Implement the selection sort algorithm that is sorting in descending order.

# Q1
"""


def sort_desc(l):
    n = len(l)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if l[j] > l[max_idx]:
                max_idx = j

        l[i], l[max_idx] = l[max_idx], l[i]

    return l


l = [64, 25, 12, 22, 11]
sorted_l = sort_desc(l)
print("Sorted array in descending order:", sorted_l)

"""

#Bubble Sort
#Implement the bubble sort algorithm that is sorting in descending order.

"""
#Q2

def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

l = [64, 34, 25, 12, 22, 11, 90]
sorted_l = bubble_sort(l)
print(sorted_l)

"""


#Insertion Sort
#Implement the insertion sort algorithm that is sorting in descending order.
"""

# Q3
def sort_descending(arr):
    n = len(l)

    for i in range(1, n):
        key = l[i]
        j = i - 1
        while j >= 0 and l[j] < key:
            l[j + 1] = arr[j]
            j -= 1
        l[j + 1] = key
    return l


l = [64, 34, 25, 12, 22, 11, 90]
sorted_l = sort_descending(l)
print(sorted_l)

"""

#Merge Sort
#Implement the merge sort algorithm that is sorting in descending order.

"""

# Q4
def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = l[:mid]
    right = l[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_descending(left, right)


def merge_descending(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result = result + left[i:]
    result = result + right[j:]

    return result


l = [64, 34, 25, 12, 22, 11, 90]
sorted_l = merge_sort(l)
print(sorted_l)

"""
