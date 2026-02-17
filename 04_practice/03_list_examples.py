#! WHAT WILL BE THE OUTPUTS
a = [1, 2, 3]
b = a
b.append(4)
print(a)        # [1, 2, 3, 4]
# Lists are mutable.
# b = a does not create a new list — both variables reference the same object.

a = [1, 2, 3]
b = a[:]
b.append(4)
print(a)        # [1, 2, 3]
# a[:] creates a shallow copy, so modifying b doesn’t affect a.

lst = [1, 2, 3]
print(lst * 2)      # [1, 2, 3, 1, 2, 3]
# ? * repeats the list, it does NOT multiply elements.

a = [[1, 2], [3, 4]]
b = a.copy()
b[0][0] = 99
print(a)        # [[99, 2], [3, 4]]
# .copy() creates a shallow copy. Inner lists are still shared.

lst = [1, 2, 3]
print(lst.append(4)) # None
print(lst)          # [1, 2, 3, 4]
# .append() modifies the list in place and returns None.

# lst = lst.append(4)  # ❌ lst becomes None

a = [1, 2, 3]
a = a + [4, 5]
print(a)
#? VS
a = [1, 2, 3]
a += [4, 5]
print(a)
# both return [1, 2, 3, 4, 5] but += modifies the list while the 1st one create new list

# ! HARD

a = [[]] * 3
print(a)
a[0].append(2)
print(a)    # output : [[1],[1],[1]]

# *  why this is dangerous
def func(lst=[]):
    lst.append(1)
    return lst

print(func())       # out : [1]
print(func())       # out : [1,1]   Default mutable arguments are created once, not every function call.

# what is the output
a = [1, 2, 3]
print(id(a))
a += [4]
print(id(a))

#! IMP
# * 1. Remove duplicates but preserve order
lst = [1,2,2,3,1,4]
# BEST
lst = list(dict.fromkeys(lst))
print(lst)

# or
l = []
for i in lst:
    if i not in l:
        l.append(i)
print(l)