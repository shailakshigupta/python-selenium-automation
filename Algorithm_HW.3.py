#Below The Arithmetical Mean
"""
When given a list, the program should return a list of all the elements below the original list’s arithmetical mean. The arithmetical mean is the sum of all elements divided by the number of elements.
Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
"""

"""

def arth_mean(input_list):
    sum = 0
    for i in input_list:
        sum = sum + i
    mean = sum / len(input_list)
    new_list = []
    for i in input_list:
        if i <= mean:
            new_list.append(i)

    return mean, new_list


l = [1, 3, 5, 6, 4, 10, 2, 3]
mean, new_list = arth_mean(l)
print("Mean:", mean)
print("New list:", new_list)
print(f"The input is {l}")

"""

#Two Lowest Elements
"""
When given a list of elements, find the two lowest elements.
They can be equal to each other or different.
Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
"""
"""


def first_two(lst):
    lowest = min(lst[0], lst[1])

    second_lowest = max(lst[0], lst[1])


    for i in range(2, len(lst)):
        if lst[i] < lowest:
            second_lowest = lowest
            lowest = lst[i]
        elif lst[i] < second_lowest:
            second_lowest = lst[i]

    return lowest, second_lowest


my_list = [198, 3, 4, 9, 10, 9, 2]
low1, low2 = first_two(my_list)
print("Lowest elements:", low1, low2)

"""