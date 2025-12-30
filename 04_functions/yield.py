"""
    yield in python : yiels also remember previous state and it value
    
"""

def even_generator(limits):
    for i in range(2,limits+1,2):
        yield i
        
for num in even_generator(10):
    print(num)