# Split in Half
""""
Given a string. Split it into two equal parts. Swap these parts and return the result.
If the string has odd characters, the first part should be one character greater than the second part.
Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.

"""
"""
def swap_string(string):
    length = len(string)
    if length % 2 == 0:
        # if the length is even
        first_part = string[:length// 2]
        second_part = string[length // 2:]
        
    else:
        # if the length is odd
        first_part = string[:(length // 2) + 1]
        second_part = string[(length // 2) + 1:]
    # swap the two parts and join them back into a single string
    return second_part + first_part


string = 'aaacbvccc'
result = swap_string(string)
print(result)


"""
#Unique Characters in String
"""
Given a string, determine if it consists of all unique characters.
For example, the string 'abcde' has all unique characters and should return True.
The string 'aabcde' contains duplicate characters and should return False.

"""
"""

def uni_chr(string):
    new=""
    for i in string:
        if i in new:
            return False
        else:
             new=new + i
    return True

string = "ABHHC"
result = uni_chr(string)

if result:
    print("TRUE")
else:
    print("FALSE")
    
"""
