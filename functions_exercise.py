def highest_even(my_list):
    highest_even=[]
    for value in my_list :
        if value % 2 == 0 :
         highest_even.append(value)
    return max(highest_even)


print(highest_even([10,5,8,12,9,2]))