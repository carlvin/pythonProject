#generators

#create a range function

class MyGen():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def __iter__(self):
        #print('whooooo')
        return self

    def __next__(self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


for i in MyGen(0,100):
    print(i)