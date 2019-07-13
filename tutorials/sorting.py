# List sorting
# list.sort() returns None, Use sorted() to return a value

list = [2, 43, 32, 56, 78, 90]
s_list = sorted(list)
rs_list = sorted(list, reverse=True)

print('list\t', list)
print('sorted list\t', s_list)
print('reversed list\t', rs_list)

# Sorting tuples

tup = (3, 1, 5, 8, 32, 0)
s_tup = sorted(tup)

print('\ntuple\t', tup)
print('sorted tuple', s_tup)
