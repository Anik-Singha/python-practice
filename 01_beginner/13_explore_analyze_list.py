from operator import index

numbers = [1,2,3,4,5,3,2,4]
print("Max: ",max(numbers))
print("Min: ",min(numbers))
print("Sum: ",sum(numbers))
print("Length: ",len(numbers))

print("All numbers: ",all(numbers))     # True
print("All", all([1,2,3,0]))            # False, 0 is considered as empty value
print("Any", any([1,2,3,0]))            # True

print("Count: ",numbers.count(4))       # Good way to find if the values are unique or contain duplicates

print("Index: ",numbers.index(4))       # Find the first index where it appeared first

#! ADD , REMOVE, UPDATE
# add to the list
lst = [1,2,3,4,5,3,2,4]
# lst = lst.append(9)   # first type
lst.append(9)
print(lst)              # This will return None for first type, as .append completes the task and result None

lst.insert(3,11)
print(lst)

# remove item from list
# remove everything
l = [1,2,3,4,5,3,2,4]
l.clear()
print(l)

# by value
l = [1,2,3,4,5,3,2,4]
l.remove(3)
print(l)

# by position
l = [1,2,3,4,5,3,2,4]
l.pop(5)    # if no number is defined, it will remove the last item, also it will return the deleted item as result
print(l)

# update
l = [1,2,3,4,5,3,2,4]
l[1] = 20
print(l)

# * Sorting Data
num = [1,2,3,4,5,3,2,4]
num.sort()
print(num)

# reverse
num.sort(reverse=True)
print(num)

# sorted() , creates a copy where the data is sorted correctly
num = [1,2,3,4,5,3,2,4]
num_sorted = sorted(num)
print(num_sorted)
print(num)
rev = sorted(num, reverse=True)
print(rev)

# Flipping the list
lst = [1,2,3,4,5,3,2,4]
lst.reverse()
l1 = list(lst.reversed())          # reversed() creates an iterator object not list, we need to convert it
print(lst)
