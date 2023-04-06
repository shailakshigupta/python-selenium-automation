
# 1. Compute the sum of digits in all numbers from 1 to n.

def sum_of_digits(n : int):
    j=0
    for i in range(1,n+1):
        j=j+i
    return j



a=sum_of_digits(10)
print(a)

# 2. Find the max number from 3 values.

def max(max_number):    
    j = 0
    for i in max_number:
        if j < i:
            j = i
        else:
            pass
    return j

max([123,339,21])


# 3. Count odd and even numbers.


def odd_even(n):
    even = ""
    odd = ""
    for i in range(0,len(n),1):
        if (int(n[i]) % 2 == 0):
            even = even + n[i]
        else:
            odd = odd + n[i]

    return even,odd

a=odd_even("238645791")
print(f"Even:{a[0]} , Odd:{a[1]}")




















