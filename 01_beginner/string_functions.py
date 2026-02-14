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
# # TODO : cleaning using replace()
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

# * operator // 'string' * number - repeats multiple times
