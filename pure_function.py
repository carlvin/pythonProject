#pure function

# def mutiply_by_2(li):
#     new_list = []
#
#     for item in li :
#         new_list.append(item*2)
#     return new_list
#
# print(mutiply_by_2([1,2,3]))

#using maps
my_list = [1,2,3]

def mutiply_by_2(item):
    return item*2
def odd_numbers(item):
    return item % 2 !=0

print(list(filter(odd_numbers,my_list)))

print(list(map(mutiply_by_2,my_list)))