# walrus operator

a = "calvin is cool"

if (n := len(a)) > 10:
    print(f'the number of words is {n}.')
while n := len(a) > 10:
    a = a[:-1]

print(a)


def test():
    print("test")
