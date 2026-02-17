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
a[0].append(1)
print(a)
