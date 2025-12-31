"""
Docstring for scope_and_closure.01_scope

    scope : local scope and global scope 
    
    closure : 
        def chaicoder(num):
             def actual(x):
                return x ** num
            return actual

        f = chaicoder(2)
        g = chaicoder(3)

        print(f(2),g(3))

"""
# username = "thakur"
# def func():
#     # username = "shubham"
#     print(username)
    
# print(username)
# print(func())

# x = 89

# def fun2(y):
#     z = x + y
#     return z

# print(fun2(11) , x)

# x = 29

# def fun3():
#     global x
#     x = 88
    
# print(fun3(),x)

# x = 21

# def f1():
#     x=12
#     def f2():
#         print(x)
#     return f2
    
# f1()

# x = 21

# def f1():
#     x=12
#     def f2():
#         print(x)
#     return f2
    
# result = f1()
# result()

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(2),g(3))