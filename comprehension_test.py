# example 1
# Constructing output list WITHOUT
# Using List comprehensions
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
#
# # #using for loop
# # output_list  = []
# #
# # for x in input_list:
# #     if x % 2 == 0:
# #         output_list.append(x)
# # print(set(output_list))
#
# # # using comprehensions
# #
# # output_list = [x for x in input_list if (x % 2 == 0)]
# #
# # print(output_list)
# #
# # #exampl 2
#
# ###create an output list of squares between 0 9
# output_list = []
# for x in range(1, 10):
#     output_list.append(x ** 2)
# print(output_list)
#
# ##using comprehension
#
# print([x ** 2 for x in range(1, 10)])

# dictionary comprehension
input_list = [1, 2, 3, 4, 5, 6, 7]
# output_dict = {}
# for v in input_list:
#     if v % 2 != 0:
#         output_dict[v] = v ** 3
# print(output_dict)

#using comprehensions

print({v:v ** 3 for v in input_list if v % 2 != 0})

#using for loop example 2

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

#map states with there corresponding capital
# output_dict ={}
# for k,v in zip(state,capital):
#     output_dict[k] =v
# print(output_dict)

#using  comprehension

output_dict = {k:v for (k,v) in zip(state,capital)}
print(output_dict)
