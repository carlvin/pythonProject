# addition function

def my_sum(num1):
    if num1:
        try:
            return num1 + 5

        except TypeError as err:
            return err
    else:
       return 'Enter a Value'

print(my_sum(30))
