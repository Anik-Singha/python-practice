# ! EASY
# ! ============================
# * 1.STRING INDEXING
s = "DataEngineer"
# Print the first character
print(s[0])
# Print the last character
print(s[-1])
# Print "Engineer" using slicing
print(s[4:])
# Reverse the string using indexing only
print(s[::-1])

# * 2.List Indexing
nums = [10, 20, 30, 40, 50]
# Print the second element
print(nums[1])
# Print the last two elements
print(nums[-2:])
# Replace 30 with 300 using indexing
nums1 = nums
nums1[2] = 300
print(nums1)
# Print elements at even index positions
print(nums[::2])

# * 3.Negative Indexing
text = "Python"
# Print the last character using negative index
print(text[-1])
# Print "tho" using slicing
print(text[2:5])
# Remove the last character using slicing
text = text[:5]     # ? or better text[:-1]
print(text)

# * 4.Nested List Indexing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# Print 5
print(matrix[1][1])
# Print 9
print(matrix[2][2])
# Print [4, 5, 6]
print(matrix[1])
# Print [2, 5, 8] (middle column)
print([matrix[0][1],matrix[1][1],matrix[2][1]])

# ! MEDIUM
# ! ==============================
# * 5.Alternate Characters
s1 = "DataEngineering"
# Print every 2nd character.
print(s1[::2])

# * 6.Swap First & Last
arr = [1, 2, 3, 4, 5]
# Write code to swap first and last element using indexing

# * 7.Extract Domain
email = "anik.singha@gmail.com"
# extract "gmail" and "com" using indexing and slicing only (no split)

# * 8.Flatten Specific Elements
data = [
    ["A", 10],
    ["B", 20],
    ["C", 30]
]
# Using indexing, create: ["A", "B", "C"]

# * 9.Reverse Words Using Slicing
s = "I love Python"
#Reverse the entire string using slicing.
# Then reverse only "Python" using indexing.

# ! HARD
# ! ======================================
# * 10.Diagonal Extraction
matrix = [
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
]
# Extract primary diagonal [11, 22, 33],
# extract secondary diagonal [13, 22, 31] using indexing  only

# * 11.Custom Slice Logic
s = "DataEngineer"
# create Dtanier using slicing logic only (no loops)

# * 12. Rotate List
nums = [1, 2, 3, 4, 5, 6]
# output : [5, 6, 1, 2, 3, 4] using slicing only

# * 13.Multi-Level Index Challenge
data = [
    ["A", [1, 2, 3]],
    ["B", [4, 5, 6]],
    ["C", [7, 8, 9]]
]
#Extract:
# 5
# 9
# [4, 5, 6]
# [2, 5, 8] (middle elements of each inner list)

# * 14. Sliding Window
nums = [1,2,3,4,5,6]
''' output :
    [[1,2,3],
     [2,3,4],
     [3,4,5],
     [4,5,6]]   using indexing logic
'''
