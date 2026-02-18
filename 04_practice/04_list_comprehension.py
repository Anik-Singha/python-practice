# A list comprehension is a compact way to create lists in one line.
# Basic Syntax : [expression for item in iterable if condition]

# E.g. = square numbers
nums = [1, 2, 3, 4]
squares = [x*x for x in nums]
print(squares)      # [1,4,9,16]

# Even numbers
nums = [1,2,3,4,5,6]
evens = [x for x in nums if x % 2 == 0]
print(evens)

# Convert to Uppercase
words = ["data", "engineer", "python"]
words_upper = [x.upper() for x in words]
print(words_upper)

# * if else list comprehension
# print 'even' for even numbers and 'odd' for odd numbers
nums = [1,2,3,4,5,6,8]
result = ["even" if x % 2 == 0 else "odd" for x in nums]
print(result)

#! FLATTEN A 2-D LIST
matrix = [[1,2,3], [4,5,6], [7,8,9]]
result = [num for row in matrix for num in row]
print(result)

"""
ORDER - 
    for row in matrix
        for num in row

"""

#! ADVANCED
# Remove Duplicates (Preserve Order)
lst = [1,2,2,3,1,4]
unique = []
[unique.append(x) for x in lst if x not in unique]
print(unique)       # or lst = list(dict.fromkeys(lst))

# Nested Condition
# output = [4, 6]
nums = [1,2,3,4,5,6]
out = [x for x in nums if x % 2 == 0 and x >3]
print(out)

#! TRICKY QUESTIONS
# what is wrong here
result = [x*x for x in range(5) if x % 2]
# * Ans : This keeps odd numbers only, because if x % 2 means non-zero (True).

# Which is faster
'''
# Method 1
result = []
for x in range(1000000):
    result.append(x)

# Method 2
result = [x for x in range(1000000)]
'''
# ? Method 2 is faster , list comprehension uses refined C code inside