# Declare and initialize variable
f = 0
print(f)

# redeclare
#  f = "abc"
print(f)

# Error: Variables of different types cannot be combined, python is strongly typed
# print("this is a string" + 123)

print("this is a string " + str(123))


# Global and Local Variables
def someFunction():
    global f
    f = "def"
    print(f) # local f

someFunction()
print(f)

del f # undefine variabls in real time
print(f)