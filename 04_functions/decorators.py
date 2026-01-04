"""
Docstring for 04_functions.decorators
Decorator :

"""
import time
# def greet(func):
#     def wrapper(*args,**kwargs):
#         print("Starting...")
#         func(*args,**kwargs)
#         print("Ending...")
#     return wrapper

# @greet
# def hello():
#     print("Decorator Functiond example")
    
# @greet
# def add(a,b):
#     print(a+b)   

# hello()
# add(2,3)

# Problem : Timing Function Execution
    # write a decorator that measures the time a function takes to executes
    
# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in {end-start,".2f"} time")
#         return result
#     return wrapper
# @timer
# def example(n):
#     time.sleep(n)
    
# example(2)

"""
Problem : Debugging function calls
    > create a decorator to print the function name and the values of its arguments every time the function is called

def debug(func):
    def wrapper(*args , **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v} " for k,v in kwargs.items())
        print(f"calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs) 
    return wrapper

@debug
def greet(name,greeting="hello"):
    print(f"{greeting} {name}")
    
greet("Shubham",greeting="hey !")
"""

"""
Problem : Cache return values
    implement a decorator that caches the return values of a function,so that when it's called with the same arguments , the cached values is returned instead of re-executing the functions
"""
# def cache(func):
#     cache_value = {}
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result=func(*args)
#         cache_value[args]=result
#         return result
#     return wrapper


# @cache
# def long_running_function(a,b):
#     time.sleep(5)
#     return a + b

# print(long_running_function(2,3))
# print(long_running_function(2,3))
# print(long_running_function(5,3))

