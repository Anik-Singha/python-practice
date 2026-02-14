# name = 'Anik'
# print(type(name))       #  type() - to check the datatypes
#
# age = 20
# print('My age is ' +  str(age))     # str() - to convert other datatype to srt
#
# print(len(name))        # len() - to check length of the str
#
# text = '''
# Python is easy to learn.
# Python is powerful.
# Many people love python.
# '''
# print(text.count('Python'))     # count() - returns how often a word appears in str, return int value
# print(text.lower().count('python')) # out = 3
#
# # Transformation
# price = '1234,56'
# print(price.replace(',', '.'))  # replace(old,new) swaps part of the text with something new
#
# phone = '813-2800-326'
# print(phone.replace('-', ''))   # example use case, cleaning phone number
#
# price = "$1,299.99"
# print(price.replace('$', '').replace(',',''))   # example case 2
#
# #  cleaning using replace()
# phone1 = "+49 (176) 123-4567"
# print(phone1.replace('+', '00').replace(' ', '').replace('(', '').replace(')', '').replace('-', ''))
#
# # + operator : joins(concatenates) two strings into one
# first_name = 'John'
# last_name = 'Doe'
# full_name = first_name + ' ' + last_name
# print(full_name)
#
# # f-strings : modern, super easy way to format and  build strings "f" stands for formatted
# p_name = "Sam"
# p_age = 34
# is_student = False
# print(f"{p_name} is {p_age} years old and student status is {is_student}")
#
# # split() : separate one value to multiple values using a common seperator , it will give lists
# stamp = "12-02-2026 07:00"
# print(stamp.split(" "))
#
# filename = "test.csv"
# # Open and read the file
# with open(filename, "r") as file:
#     data = file.read()
#     # This splits the contents of the file by commas
#     print(data.split(","))

# ?  * operator // 'string' * number - repeats multiple times
print("ha" * 3)

# INDEXING AND SLICING / start position is included but end is not
# string[start:end:step]
text = "Python"
print(text[0:5:2])  # out : Pto

print(text[0:5:1]) # out : Pytho / steps of 1 take every letter
print(text[::3])    # out : Ph / start from P and jump 3 steps
print(text[::-1])   # out : nohtyP / reverses the string

# ? Whitespace Cleanup
text = " Engineering".lstrip()  # remove space from left
print(text)
text = "Engineering ".rstrip()  # remove space from right
print(text)
text = " Engineering ".strip()  # remove spaces from both sides
print(text)                     # * strip() will not remove space in between words e.g 'data engineer'

text = '###abc###'.strip("#")
print(text)                     # * we can pass the desired characters we want to remove

# ? CASE CONVERSIONS // upper(), lower()
text = 'python PROGRAMMING'
print(text.upper())
print(text.lower())

# ? SEARCH
phone = '+91-8132-800-326'
print(phone.startswith('+91'))  # startswith() to check from start

email = "anik@gmail.com"
print(email.endswith('@gmail.com')) #endswith() to check from end

print("@" in email) # in to check in the middle

# ---------------------------------------
# Partial Extraction Using find()
# ---------------------------------------
phone1 = "+48-176-12345"
phone2 = "48-654-16548"
phone3 = "0048-654-16548"

print(phone1[phone1.find("-") + 1:])  # ➜ 176-12345
print(phone2[phone2.find("-") + 1:])  # ➜ 654-16548
print(phone3[phone3.find("-") + 1:])  # ➜ 654-16548

print(phone1.find("-"))              # ➜ 3
                                     # ? we can use words inside find e.g.'python' and it will find the first index of
                                     #   similar word

# ? VALIDATION
country = "India"
print(country.isalpha())    # isalpha() checks if the string has only alphabets
country1 = "India1"
print(country1.isalpha())   # out : false

phoneno = "8132800834"
print(phoneno.isnumeric())  # isnumeric() to check numbers , it will not accept float too, result false