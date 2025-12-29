"""
Docstring for 03_loops.for_loop
    loops are used for sequentail traversal . for traversing list,string,tuples etc
    
    for value in list:
        #some work
        
    else:
        # work when looop ends
        
    range()
        > starting from 0 by default
        > increments by 1 by default
        > stops before a specified number
        
        range(start?,end,stop?)
        
    pass :
        pass is null statements that does nothing.it is used as a placeholder for future code 
"""

"""
print the elements of the following list using a loop

list = []
for x in range(1,11):
    list.append(x*x)
    
print(list)
"""

"""
search for a number x in this tuple using loop
(1,4,9,16,25,36,49,64,81,100)

my_tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36

found = False
for num in range(10):
    if my_tuple[num] == x:
        print("Found")
        found=True
        break

if not found:
    print("Not Found")
"""

"""
to find the sum of first n numbers

sum = 0
n = 10
for x in range(n,0,-1):
    sum = sum + x
    
print(sum)
"""

"""
to find the factorial of first n numbers

n = 5
factorial = 1
for x in range(5,0,-1):
    factorial = factorial * x

print(factorial)

"""