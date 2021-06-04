# define a basic function
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function returns a value
def cube(x):
    return x * x * x

# function with default value for argument
def power(num, x = 1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#  function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

func1()
print(func1()) # func1 doesn't return a value, outputs None
print(func1) # prints string memory location
func2(10, 20)
print(func2(10,20)) # does not return a value
print(cube(3))
print(power(2))
print(power(2,3)) # => 8
print(power(x = 3, num = 2)) # named parameters can be interpreted even if in wrong order
print(multi_add(10, 4, 5, 10, 4))