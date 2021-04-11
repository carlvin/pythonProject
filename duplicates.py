# exercise check for duplicates in list

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicate = []
# for items in some_list :
#     if (some_list.count(items)) > 1 :
#         if items not in duplicate :
#          duplicate.append(items)
# print(duplicate)

#list comprehensions

duplicate = list(set(x for x in some_list if some_list.count(x) > 1))
print(duplicate)