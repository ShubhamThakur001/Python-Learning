"""
Docstring for 04_functions.lambda

    why we use lambda functions
        > function require only one time in life-time
    
    cube = lambda x: x ** 3 
"""

# cube = lambda x: x ** 3

# print(cube(3))


"""
*args : return tuple [positinal arguments] dont know number of arguments required

def sum_all(*args):
    total=0
    
    for i in args:
        total += i
    return total

print(sum_all(1,2,3))
print(sum_all(1,2))
print(sum_all(1,2,3,4))

"""

"""
**kwargs : return dictonary [key arguments] dont know number of arguments required
"""

def print_kwargs(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
print(print_kwargs(name="shubham",surname="thakur",age=21))
print(print_kwargs(name="shubham",surname="thakur",age=21,number="1232123290"))
print(print_kwargs(name="shubham",surname="thakur",age=21,number="0987667890",gender="male"))
