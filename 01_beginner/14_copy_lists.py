# there are 3 types of copy

# normal copy
a = [1,2,3]
b = a
print(b)
b.append(4)
print(a)    # here the location of lists are same, so change in b will change a too

# shallow copy
a = [1,[2,3]]
b = a.copy()
print(b)
b[0] = 5
print(a)    # here changing b[0] to 5 doesn't affect the value in a
b[1][1] = 7
print(a)    # but changing the values inside nested list will affect 'a' too.

# deep copy
import copy
a = [1,[2,3]]
b = copy.deepcopy(a)
print(b)    # here it creates whole new list, so any change inside b will not affect a
