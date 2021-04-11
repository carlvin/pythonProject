print("Hello World")

print ("usa")
print ("Canada")
print ("France")
print ("Germany")
print ("Japan")

#print (8 * "\n")

print("welcome to Guru")

# python variables
# variable declaraion
a=200
print(a)

a="Days of code"
b=100
print("a")

print(str(b)+ a)

#global vs local varibles

f = 100
print(f)

def something():
    global f
    f = "this is python"
    #del f
    print(f)

something()
print(f)
