#Even First
"""
Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
"""

"""

def even_odd(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] % 2 == 0:
            left = left + 1
        else:
            lst[left], lst[right] = lst[right], lst[left]
            right = right - 1

    return lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reordered_list = even_odd(my_list)
print(reordered_list)

"""

#Increment a Number
"""
Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].
"""

"""

def update_list(lst, num):
    carry = 1
    for i in range(len(lst) - 1, -1, -1):
        digit_sum = lst[i] + carry
        if digit_sum < 10:
            lst[i] = digit_sum
            carry = 0
            break
        else:
            lst[i] = digit_sum - 10
            carry = 1

    if carry:
        lst.insert(0, carry)

    return lst


my_list = [9, 9, 9]
updated_list = update_list(my_list, 1)
print("Updated list:", updated_list)

"""